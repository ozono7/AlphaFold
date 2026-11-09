# AlphaFold — Predicción de estructura de proteínas en Google Colab

Scripts completos y listos para usar en Google Colab (ColabFold), para
predecir estructuras de proteínas de interés biotecnológico, sin
supercomputadora y sin instalar nada.

**Autor:** Dr. José Juan Torres Martínez
**Docente de Ciencias Químicas, UASLP**

## Base

Todos los scripts usan **ColabFold** (AlphaFold2 en Google Colab):

https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

ColabFold es gratuito y corre en la nube de Google. Solo necesitas una
cuenta de Google y la secuencia de aminoácidos de tu proteína.

## Cómo se usa

1. Abre el enlace de ColabFold de arriba.
2. Pega la secuencia de aminoácidos (en formato de una letra) en la celda
   `query_sequence`.
3. Ejecuta las celdas en orden (Runtime > Run all).
4. Descarga los resultados (estructura PDB, puntajes pLDDT y PAE).
5. Analiza los resultados con los scripts de este repositorio: Python
   (02 y 05) o R (02b).

## Organismo de trabajo

*Chlorella vulgaris* (microalga verde), con énfasis en enzimas de la
biosíntesis de lípidos y ácidos grasos.

## Scripts

| # | Archivo | Tema |
|---|---|---|
| 01 | `01-primera-prediccion.md` | Tu primera predicción: la subunidad beta de la acetil-CoA carboxilasa (ACCD) de *Chlorella vulgaris* |
| 02 | `02-interpretar-plddt-pae.py` | Interpretar pLDDT y PAE: ¿la predicción es confiable? (Python) |
| 02b | `02b-interpretar-plddt-pae-en-R.R` | Interpretar pLDDT y PAE en R: ¿la predicción es confiable? (versión en R del script 02) |
| 03 | `03-comparar-variantes.md` | Comparar dos variantes de una enzima (silvestre vs mutante) |
| 04 | `04-complejo-proteina-proteina.md` | Predecir un complejo proteína-proteína |
| 05 | `05-preparar-docking.py` | Preparar la estructura para docking molecular (Python) |
| 06 | `06-anotar-dominios.md` | Anotar dominios y motivos en la estructura predicha |
| — | `Práctica` | Práctica: predecir estructuras de septinas (individuales, truncadas, dímeros y trímero) |

## Obtener una secuencia de UniProt

Si no tienes la secuencia, descárgala de UniProt con su acceso (accession).
Por ejemplo, para ACCD de *Chlorella vulgaris* (P56293):

```
https://rest.uniprot.org/uniprotkb/P56293.fasta
```

Abre ese enlace en el navegador y copia la secuencia (sin la línea que
empieza con `>`).
