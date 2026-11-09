# 06. Anotar dominios y motivos en la estructura predicha

**Autor:** Dr. José Juan Torres Martínez — Docente de Ciencias Químicas, UASLP

## La pregunta

¿Qué partes de la proteína son dominios funcionales y dónde están los
motivos importantes? En este ejercicio cruzamos la estructura predicha
con la anotación de dominios de UniProt e InterPro.

## Paso 1. Consultar la anotación en UniProt

Abre la entrada de ACCD de *Chlorella vulgaris*:

```
https://rest.uniprot.org/uniprotkb/P56293.txt
```

Busca las líneas que empiezan con `FT` (feature table). Ahí verás:
- Dominios (por ejemplo, el dominio carboxiltransferasa).
- Sitios de unión (biotina, sustrato).
- Regiones de interés.

Anota los rangos de residuos de cada dominio.

## Paso 2. Consultar InterPro

Abre:

```
https://www.ebi.ac.uk/interpro/protein/UniProt/P56293
```

InterPro agrupa la anotación de dominios de varias bases de datos
(Pfam, SMART, PROSITE). Anota los dominios y sus rangos.

## Paso 3. Cruzar dominios con pLDDT

Corre el script 02 para obtener el pLDDT por residuo y compáralo con
los rangos de dominios:

- ¿Los dominios catalíticos tienen pLDDT alto? (Lo habitual: sí.)
- ¿Hay regiones sin dominio anotado con pLDDT bajo? (Suelen ser
  regiones desordenadas o conectores flexibles.)
- ¿Algún motivo funcional cae en una región de pLDDT bajo? Si es así,
  interpreta esa zona con cautela.

## Paso 4. Visualizar

Abre el PDB en un visor (PyMOL, ChimeraX) y colorea por dominio:
un color por dominio, según los rangos anotados. Esto da una imagen
clara de la arquitectura de la proteína y es una figura lista para
una presentación o un artículo.

## Interpretación

- La anotación de dominios es independiente de AlphaFold: viene de
  homología y de firmas de secuencia. Que un dominio tenga pLDDT alto
  refuerza la confianza en esa región.
- Si un dominio anotado tiene pLDDT bajo, puede ser un dominio
  flexible o una predicción incierta; no lo descartes, pero no
  interpretes su forma como definitiva.
