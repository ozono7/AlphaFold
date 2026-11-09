# 01. Tu primera predicción: ACCD de *Chlorella vulgaris* en ColabFold

**Autor:** Dr. José Juan Torres Martínez — Docente de Ciencias Químicas, UASLP

## La proteína

**Acetil-CoA carboxilasa, subunidad beta (ACCD)** de *Chlorella vulgaris*.
Es una enzima clave en la biosíntesis de ácidos grasos: cataliza el primer
paso comprometido (acetil-CoA → malonil-CoA). Si quieres entender por qué
una microalga acumula lípidos, esta enzima es un buen punto de partida.

- **UniProt:** P56293 (ACCD_CHLVU)
- **Organismo:** *Chlorella vulgaris*
- **Longitud:** 411 aminoácidos
- **Función:** carboxiltransferasa, parte del complejo acetil-CoA carboxilasa

## Paso 1. Obtener la secuencia

Abre en el navegador:

```
https://rest.uniprot.org/uniprotkb/P56293.fasta
```

Copia la secuencia de aminoácidos (todas las líneas excepto la que empieza
con `>`) y pégala en un archivo de texto. Debe quedar como una sola cadena
de letras (sin espacios ni saltos de línea).

## Paso 2. Abrir ColabFold

Abre este enlace en Google Colab:

https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

Si es tu primera vez, Colab te pedirá permiso para usar la GPU. Acepta
(Runtime > Change runtime type > GPU).

## Paso 3. Pegar la secuencia

En la celda `query_sequence`, borra el ejemplo y pega tu secuencia. En la
celda `jobname`, escribe un nombre, por ejemplo `ACCD_Chlorella`.

Deja el resto de las opciones como están la primera vez:
- `num_relax`: 0 (más rápido; el refinamiento lo haremos después)
- `template_mode`: none
- `msa_mode`: mmseqs2_uniref_env

## Paso 4. Ejecutar

Runtime > Run all. La predicción tarda entre 5 y 20 minutos, según la
longitud de la proteína y la cola de Colab.

## Paso 5. Descargar los resultados

Al terminar, ColabFold genera:
- Un archivo `.pdb` con la estructura (el modelo rank_1 es el mejor).
- Un archivo `.json` con los puntajes pLDDT por residuo.
- Un archivo con la matriz PAE (predicted aligned error).
- Una imagen con la estructura coloreada por pLDDT.

Descarga el `.pdb` y el `.json` a tu computadora. Los analizaremos en el
script 02.

## Qué significa el resultado (resumen)

- **pLDDT > 90:** región muy confiable.
- **pLDDT 70–90:** confiable.
- **pLDDT 50–70:** confianza baja.
- **pLDDT < 50:** no confiable (probable desorden).

En el script 02 graficaremos el pLDDT por residuo para ver qué partes de
ACCD están bien predichas y cuáles no.
