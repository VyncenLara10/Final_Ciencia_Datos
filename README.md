# Proyecto final de Ciencia de Datos: 30,000 canciones de Spotify

**Pregunta central:** ¿qué dicen las características de audio de una canción sobre su género y su popularidad?

**Datos:** *30,000 Spotify Songs* (TidyTuesday, 21-01-2020), obtenidos de la API de Spotify con `spotifyr`.
Fuente: https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-01-21

## Estructura

```
Proyecto_Spotify/
├── data/
│   ├── spotify_songs.csv          # base cruda (32,833 filas)
│   └── spotify_limpio.csv         # base limpia que exporta Python (26,229 canciones)
├── 01_analisis_python.qmd         # Parte 1 (Python): limpieza, EDA, clustering, clasificación de género
├── 01_analisis_python.html        # Parte 1 ya ejecutada
├── 01_analisis_python.ipynb       # la misma Parte 1 como notebook, con resultados
├── 02_analisis_r.Rmd              # Parte 2 (R): frecuencias, pruebas de hipótesis, modelos de popularidad
├── 02_analisis_r.html             # Parte 2 ya ejecutada
└── powerbi/                       # Parte 3: datos, medidas DAX, tema y guía del dashboard
```


## Técnicas aplicadas

| Tema del curso | Dónde |
|---|---|
| Carga, tipos de datos y diccionario de variables | Python A |
| Nulos, duplicados y nulos disfrazados | Python B.1 a B.3, R A |
| Imputación (eliminar vs. mediana vs. KNN) | Python B.3 |
| Outliers (IQR) y winsorización | Python B.5 |
| Tabla de frecuencias agrupada (Sturges), histograma y ojiva | R B |
| Estadística descriptiva, correlación y visualización | Python C y D |
| ANOVA, Kruskal-Wallis, χ², prueba t y correlación de Spearman | R C |
| Clustering K-Means (codo, silueta, PCA) | Python E |
| Clasificación multiclase (logística, Naive Bayes, árbol, RF, boosting) con ROC/AUC | Python F |
| Regresión (lineal, Random Forest, Gradient Boosting) con RMSE, MAE y R² | R D |
| Clasificación binaria con curva ROC y umbral de Youden | R E |
| Dashboard interactivo | Power BI |

## Resultados principales

* De 32,833 filas quedan **26,229 canciones únicas**. Las 2,264 canciones con popularidad 0 son un nulo disfrazado.
* El género se puede predecir con el audio con **58.7 % de exactitud** (el azar daría 16.7 %; AUC = 0.87, Gradient Boosting).
* La popularidad casi no depende del sonido: el mejor modelo explica solo el **16 %** de su variación (R² = 0.16).
* Conclusión: el audio dice **cómo suena** una canción, pero no **qué tan exitosa** será.
