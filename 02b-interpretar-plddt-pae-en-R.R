# ==========================================================================
# 02b. Interpretar pLDDT y PAE en R: ¿la predicción es confiable?
# ==========================================================================
# Autor: Dr. José Juan Torres Martínez
# Docente de Ciencias Químicas
# Universidad Autónoma de San Luis Potosí (UASLP)
# México
#
# Material académico para estudiantes
# Serie "AlphaFold" — Script 02b (versión en R del script 02)
#
# Descripción: Lee el archivo JSON que genera ColabFold (con el pLDDT por
#   residuo), grafica la confianza a lo largo de la secuencia y resume qué
#   fracción de la proteína está bien predicha. También grafica el mapa de
#   calor de la matriz PAE (predicted aligned error), si el JSON la incluye.
#
# Uso: corre este script en RStudio o Positron con el archivo .json de
#   ColabFold en la misma carpeta. Cambia el nombre del archivo en la
#   variable archivo_json.
#
# Requisitos: tidyverse y jsonlite.
#   Instálalos con: install.packages(c("tidyverse", "jsonlite"))
# ==========================================================================

# --------------------------------------------------------------------------
# 1. Cargar paquetes
# --------------------------------------------------------------------------
library(tidyverse)
library(jsonlite)

# --------------------------------------------------------------------------
# 2. Leer el archivo JSON de ColabFold
# --------------------------------------------------------------------------
# El archivo se llama algo como:
# ACCD_Chlorella_scores_rank_001_alphafold2_ptm_model_1_seed_000.json
archivo_json <- "ACCD_Chlorella_scores_rank_001_alphafold2_ptm_model_1_seed_000.json"

datos <- fromJSON(archivo_json)

# pLDDT por residuo (un valor por aminoácido)
plddt <- datos$plddt
n_residuos <- length(plddt)

cat("Residuos:", n_residuos, "\n")
cat("pLDDT promedio:", round(mean(plddt), 1), "\n")
cat("pLDDT mínimo:", round(min(plddt), 1), "\n")
cat("pLDDT máximo:", round(max(plddt), 1), "\n")

# --------------------------------------------------------------------------
# 3. Resumen por rangos de confianza
# --------------------------------------------------------------------------
# pLDDT > 90: muy confiable. 70-90: confiable. 50-70: baja. < 50: muy baja.
resumen <- tibble(
  rango = c("Muy alta (>90)", "Alta (70-90)", "Baja (50-70)", "Muy baja (<50)"),
  residuos = c(
    sum(plddt > 90),
    sum(plddt >= 70 & plddt <= 90),
    sum(plddt >= 50 & plddt < 70),
    sum(plddt < 50)
  )
) %>%
  mutate(porcentaje = round(100 * residuos / n_residuos, 1))

print(resumen)

# --------------------------------------------------------------------------
# 4. Gráfica: pLDDT por residuo
# --------------------------------------------------------------------------
tabla_plddt <- tibble(
  residuo = seq_len(n_residuos),
  plddt = plddt
)

grafica_plddt <- ggplot(tabla_plddt, aes(x = residuo, y = plddt)) +
  # Fondo por rangos de confianza
  annotate("rect", xmin = 1, xmax = n_residuos, ymin = 90, ymax = 100,
           fill = "#2166ac", alpha = 0.15) +
  annotate("rect", xmin = 1, xmax = n_residuos, ymin = 70, ymax = 90,
           fill = "#5ab4ac", alpha = 0.15) +
  annotate("rect", xmin = 1, xmax = n_residuos, ymin = 50, ymax = 70,
           fill = "#fdae61", alpha = 0.15) +
  annotate("rect", xmin = 1, xmax = n_residuos, ymin = 0, ymax = 50,
           fill = "#d73027", alpha = 0.15) +
  geom_line(color = "#1a1a1a", linewidth = 0.7) +
  labs(
    x = "Residuo (posición en la secuencia)",
    y = "pLDDT",
    title = "Confianza de la predicción (pLDDT) por residuo — ACCD, Chlorella vulgaris"
  ) +
  ylim(0, 100) +
  xlim(1, n_residuos) +
  theme_bw()

print(grafica_plddt)
ggsave("02b_plddt_por_residuo.png", grafica_plddt, width = 12, height = 4, dpi = 300)

# --------------------------------------------------------------------------
# 5. Mapa de calor de PAE (si el archivo incluye la matriz PAE)
# --------------------------------------------------------------------------
# La matriz PAE indica el error esperado en la posición relativa entre dos
# residuos. Valores bajos = posición relativa confiable. Valores altos =
# posición relativa incierta.
if (!is.null(datos$pae)) {
  pae <- datos$pae
  tabla_pae <- as_tibble(pae, .name_repair = "minimal") %>%
    mutate(fila = row_number()) %>%
    pivot_longer(
      cols = -fila,
      names_to = "columna",
      values_to = "pae"
    ) %>%
    mutate(columna = as.integer(gsub("V", "", columna)))

  grafica_pae <- ggplot(tabla_pae, aes(x = columna, y = fila, fill = pae)) +
    geom_raster() +
    scale_fill_viridis_c(limits = c(0, 30), name = "PAE (Å)") +
    labs(
      x = "Residuo",
      y = "Residuo",
      title = "PAE (predicted aligned error, Å) — ACCD, Chlorella vulgaris"
    ) +
    theme_bw() +
    coord_fixed()

  print(grafica_pae)
  ggsave("02b_mapa_pae.png", grafica_pae, width = 6, height = 5, dpi = 300)
} else {
  cat("\nEl archivo JSON no incluye la matriz PAE.\n")
}

# --------------------------------------------------------------------------
# Interpretación
# --------------------------------------------------------------------------
# Gráfica 1: pLDDT por residuo
# - Eje X: posición del residuo en la secuencia (1 a N, donde N es la
#   longitud de la proteína). Cada punto es un aminoácido.
# - Eje Y: pLDDT, de 0 a 100, adimensional (no tiene unidades: es un
#   puntaje de confianza). > 90 es muy confiable, 70-90 es confiable,
#   50-70 es confianza baja, < 50 es no confiable.
# - Lo que se aprecia: las regiones donde la línea está arriba (pLDDT
#   alto) están bien predichas; donde cae por debajo de 50, la predicción
#   no es confiable (suele ser una región desordenada o flexible).
# - Qué significa: si la mayor parte de la proteína tiene pLDDT > 70,
#   la predicción es confiable en su conjunto.
#
# Gráfica 2: mapa de calor de PAE
# - Eje X y eje Y: posición del residuo (ambos ejes son residuos).
# - Color: PAE (predicted aligned error), en Ångströms (Å). Un Å es
#   10^-10 metros, la escala de los átomos. Valores bajos (azul/verde)
#   significan que la posición relativa entre esos dos residuos es
#   confiable; valores altos (rojo) significan que es incierta.
# - Lo que se aprecia: bloques de valores bajos en la diagonal indican
#   dominios bien definidos; bloques de valores altos entre dominios
#   indican que su orientación relativa es incierta.
# - Qué significa: el PAE dice qué tan segura es la posición relativa
#   entre partes de la proteína, no solo cada residuo por separado.
#
# --------------------------------------------------------------------------
# Qué aprendimos
# --------------------------------------------------------------------------
# - El pLDDT (0-100, adimensional) dice qué tan confiable es la posición
#   de cada aminoácido. Por encima de 70, la predicción es confiable.
# - El PAE (en Ångströms) dice qué tan confiable es la posición relativa
#   entre dos residuos. Valores bajos son buenos.
# - Las regiones con pLDDT < 50 suelen ser desordenadas o flexibles: no
#   interpretes su forma como definitiva.
# - Cada gráfico lleva su interpretación: qué es cada eje (con unidades),
#   qué patrón se ve y qué significa.
