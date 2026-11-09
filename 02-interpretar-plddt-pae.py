"""
02. Interpretar pLDDT y PAE: ¿la predicción es confiable?
================================================================
Autor: Dr. José Juan Torres Martínez
Docente de Ciencias Químicas, UASLP

Descripción: Lee el archivo JSON que genera ColabFold (con el pLDDT por
residuo), grafica la confianza a lo largo de la secuencia y resume qué
fracción de la proteína está bien predicha. También lee la matriz PAE
(predicted aligned error) y grafica su mapa de calor.

Uso: corre este script en Google Colab (o en tu computadora) con el
archivo .json de ColabFold en la misma carpeta. Cambia el nombre del
archivo en la variable ARCHIVO_JSON.

Requisitos: numpy, matplotlib.
En Colab ya están instalados. En tu computadora:
    pip install numpy matplotlib
================================================================
"""

import json
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. Leer el archivo JSON de ColabFold
# ---------------------------------------------------------------------------
# El archivo se llama algo como: ACCD_Chlorella_scores_rank_001_alphafold2_ptm_model_1_seed_000.json
ARCHIVO_JSON = "ACCD_Chlorella_scores_rank_001_alphafold2_ptm_model_1_seed_000.json"

with open(ARCHIVO_JSON, "r") as f:
    datos = json.load(f)

# pLDDT por residuo (una lista con un valor por aminoácido)
plddt = np.array(datos["plddt"])
n_residuos = len(plddt)

print(f"Residuos: {n_residuos}")
print(f"pLDDT promedio: {plddt.mean():.1f}")
print(f"pLDDT mínimo: {plddt.min():.1f}")
print(f"pLDDT máximo: {plddt.max():.1f}")

# ---------------------------------------------------------------------------
# 2. Resumen por rangos de confianza
# ---------------------------------------------------------------------------
# pLDDT > 90: muy confiable. 70-90: confiable. 50-70: baja. < 50: muy baja.
rangos = {
    "Muy alta (>90)": np.sum(plddt > 90),
    "Alta (70-90)": np.sum((plddt >= 70) & (plddt <= 90)),
    "Baja (50-70)": np.sum((plddt >= 50) & (plddt < 70)),
    "Muy baja (<50)": np.sum(plddt < 50),
}

print("\nResiduos por rango de confianza:")
for nombre, conteo in rangos.items():
    print(f"  {nombre}: {conteo} ({100 * conteo / n_residuos:.1f}%)")

# ---------------------------------------------------------------------------
# 3. Gráfica: pLDDT por residuo
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 4))

# Fondo por rangos de confianza
ax.axhspan(90, 100, color="#2166ac", alpha=0.15)
ax.axhspan(70, 90, color="#5ab4ac", alpha=0.15)
ax.axhspan(50, 70, color="#fdae61", alpha=0.15)
ax.axhspan(0, 50, color="#d73027", alpha=0.15)

ax.plot(np.arange(1, n_residuos + 1), plddt, color="#1a1a1a", linewidth=1)
ax.set_xlabel("Residuo (posición en la secuencia)")
ax.set_ylabel("pLDDT")
ax.set_title("Confianza de la predicción (pLDDT) por residuo — ACCD, Chlorella vulgaris")
ax.set_ylim(0, 100)
ax.set_xlim(1, n_residuos)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("02_plddt_por_residuo.png", dpi=300)
plt.show()

# ---------------------------------------------------------------------------
# 4. Mapa de calor de PAE (si el archivo incluye la matriz PAE)
# ---------------------------------------------------------------------------
# La matriz PAE indica el error esperado en la posición relativa entre dos
# residuos. Valores bajos (azul/verde) = posición relativa confiable.
# Valores altos (rojo) = posición relativa incierta.
if "pae" in datos:
    pae = np.array(datos["pae"])
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(pae, cmap="viridis", vmin=0, vmax=30)
    ax.set_xlabel("Residuo")
    ax.set_ylabel("Residuo")
    ax.set_title("PAE (predicted aligned error, Å) — ACCD, Chlorella vulgaris")
    plt.colorbar(im, ax=ax, label="PAE (Å)")
    plt.tight_layout()
    plt.savefig("02_mapa_pae.png", dpi=300)
    plt.show()
else:
    print("\nEl archivo JSON no incluye la matriz PAE.")

# ---------------------------------------------------------------------------
# Interpretación
# ---------------------------------------------------------------------------
# - Si la mayor parte de la proteína tiene pLDDT > 70, la predicción es
#   confiable en su conjunto.
# - Regiones con pLDDT < 50 suelen ser desordenadas o flexibles; no
#   interpretes su forma como definitiva.
# - En el PAE, bloques azules/verdes en la diagonal indican dominios bien
#   definidos; bloques rojos entre dominios indican orientación incierta.
