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
- Dominios: el dominio carboxiltransferasa N-terminal, residuos 32–302.
- Sitios de unión a zinc (Zn2+): residuos 36, 39, 55 y 58 (dedo de
  zinc, residuos 36–58).
- Regiones de interés.

Anota los rangos de residuos de cada dominio. Ojo: la biotina no se une
a ACCD; la biotina la lleva la proteína transportadora BCCP, otra
subunidad del complejo. En ACCD, los sitios de unión anotados son de
zinc, no de biotina.

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

## Qué aprendimos

- La anotación de dominios (UniProt, InterPro) es independiente de
  AlphaFold: viene de homología y de firmas de secuencia.
- En ACCD, el dominio carboxiltransferasa cubre los residuos 32–302 y
  los sitios de unión a zinc son los residuos 36, 39, 55 y 58.
- Cruzar los dominios con el pLDDT dice qué partes funcionales de la
  proteína están bien predichas y cuáles hay que interpretar con
  cautela.
