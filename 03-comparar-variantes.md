# 03. Comparar dos variantes de una enzima (silvestre vs mutante)

**Autor:** Dr. José Juan Torres Martínez — Docente de Ciencias Químicas, UASLP

## La pregunta

¿Un cambio de un aminoácido (mutación puntual) cambia la estructura de la
enzima? En este ejercicio predecimos la misma enzima en dos versiones
(silvestre y mutante) y comparamos sus estructuras.

## Proteína

ACCD de *Chlorella vulgaris* (UniProt P56293), la misma del script 01.

## Paso 1. Obtener la secuencia silvestre

Descarga la secuencia en FASTA:

```
https://rest.uniprot.org/uniprotkb/P56293.fasta
```

## Paso 2. Crear la variante mutante

Elige un residuo del sitio activo o de interés y cámbialo. Por ejemplo,
cambia una lisina (K) por alanina (A): la posición 150 de ACCD es una
lisina, así que el cambio se anota `K150A` (lisina 150 por alanina).
Edita esa letra en la secuencia (la posición 123, por ejemplo, es una
leucina, no una lisina: revisa siempre el residuo en la secuencia antes
de anotar el cambio).

Guarda la secuencia mutante en un archivo aparte. **No inventes el
efecto**: la predicción te dirá si la estructura cambia o no.

## Paso 3. Predecir ambas versiones en ColabFold

Abre ColabFold:

https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

Haz dos corridas: una con la secuencia silvestre (jobname
`ACCD_silvestre`) y otra con la mutante (jobname `ACCD_mutante`).

Usa las mismas opciones en ambas corridas para que la comparación sea
válida.

## Paso 4. Comparar

Descarga los archivos `.pdb` (rank_1) y los `.json` (pLDDT) de ambas
corridas.

1. **pLDDT:** corre el script 02 con cada JSON y compara los promedios.
   Si el pLDDT promedio cae mucho en la mutante, la mutación
   desestabiliza la proteína.
2. **Estructura:** abre ambos PDB en un visor (PyMOL, ChimeraX o el visor
   de Colab) y superpónlos. Fíjate si el sitio activo cambia de forma.
3. **RMSD:** si tienes PyMOL, calcula el RMSD entre ambas estructuras
   (`align ACCD_mutante, ACCD_silvestre`). Un RMSD bajo (< 1 Å) indica
   que la estructura global no cambió; un RMSD alto indica un cambio
   importante.

## Interpretación

- Una mutación puntual rara vez cambia toda la estructura; lo habitual es
  que cambie la zona local o la estabilidad.
- Si el pLDDT local cae alrededor del residuo mutado, esa región se volvió
  menos confiable o más flexible.
- AlphaFold predice estructura, no función: un cambio estructural no
  prueba por sí solo un cambio de actividad. Para eso hacen falta
  experimentos.

## Qué aprendimos

- Para comparar dos variantes hay que predecirlas en las mismas
  condiciones: misma proteína, mismo programa y mismas opciones; si no,
  no se sabe si la diferencia viene de la mutación o de la corrida.
- El pLDDT por residuo y el RMSD entre las dos estructuras dicen si la
  mutación cambió la estructura: un RMSD bajo (< 1 Å) indica que la
  estructura global no cambió.
- Una mutación puntual rara vez cambia toda la estructura; lo habitual
  es que cambie la zona local o la estabilidad.
