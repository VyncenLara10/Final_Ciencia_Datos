# Proyecto final de Ciencia de Datos · Spotify

**Pregunta:** ¿Qué nos dicen las características de audio sobre el género de playlist y la popularidad de una canción?

**Equipo:** Vyncen Lara, Roger Monterroso, Juan Marcos y Jose Ronquillo.

## Datos y procedencia

- Fuente abierta: [TidyTuesday · 2020-01-21, Spotify Songs](https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-01-21).
- Origen histórico: información de Spotify recuperada con `spotifyr`. Revisar la documentación y las condiciones de uso del origen; no se afirma aquí una licencia independiente distinta de la fuente enlazada.
- `data/spotify_songs.csv`: 32,833 observaciones originales. La unidad original es canción en playlist y puede repetirse.
- `data/spotify_limpio.csv`: 26,229 canciones después de limpieza y deduplicación; generada por el análisis Python original.
- `powerbi/spotify_powerbi.csv` y otras tablas: insumos para dashboard y métricas exportadas.

**Precauciones:** el género corresponde a la **playlist**, no necesariamente a la canción; la popularidad es histórica (2020) y su valor 0 fue interpretado en el trabajo original como faltante. Esta decisión debe discutirse como supuesto y no como hecho garantizado. Los modelos muestran asociaciones, no causalidad. Evitar extrapolar al catálogo completo de Spotify.

## Archivos principales

| Ruta | Propósito |
|---|---|
| `01_analisis_python.qmd`, `.ipynb`, `.html` | Limpieza, exploración, clustering, clasificación y resultados |
| `02_analisis_r.Rmd`, `.html` | Inferencia, frecuencias, regresión de popularidad y clasificación binaria |
| `reports/informe_final.qmd` | Informe Quarto integrador con chunks ejecutables R y Python |
| `dashboard/app.py` | Dashboard interactivo Streamlit, equivalente permitido a Power BI |
| `powerbi/` | Dataset de dashboard, métricas de modelos, paleta de colores |
| `docs/presentacion_guion.md` | Guion de 15–20 minutos y preguntas para la defensa |
| `docs/AUTORIA.md` | Propuesta de responsabilidades pendiente de confirmación |

## Instalación y reproducción

Requisitos: Python 3.10+, R 4.2+, Quarto instalado en el sistema y acceso al conjunto de archivos ya versionado. Desde la **raíz del repositorio**, crear el entorno:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
Rscript R-packages.R
```

Configurar `reticulate` para que R detecte el Python de `.venv` si fuera necesario (por ejemplo, exportar `RETICULATE_PYTHON` con la ruta absoluta al ejecutable `python` de ese entorno). El informe integrador se construye desde la raíz:

```bash
quarto render reports/informe_final.qmd --to html
```

Esto produce `reports/informe_final.html`. Los informes completos originales ya están versionados como `01_analisis_python.html` y `02_analisis_r.html`. Para volver a entrenar sus modelos, ejecutar los fuentes originales desde la raíz con sus dependencias (la ejecución puede consumir más tiempo y memoria).

Ejecutar el dashboard:

```bash
streamlit run dashboard/app.py
```

Streamlit mostrará una URL local (habitualmente `http://localhost:8501`). Los filtros alteran las visualizaciones de canciones, **no** vuelven a entrenar modelos: las tablas de métricas representan la evaluación original.

## Metodología

1. **Comprensión:** Spotify, categorías de playlists, descripción de audio y popularidad.
2. **Limpieza:** descartar nombre/artista faltantes, ordenar y deduplicar, crear año/década/duración; documentar supuestos sobre popularidad 0.
3. **EDA:** distribuciones, correlaciones, perfiles por género y relaciones multivariadas.
4. **Modelado:** K-Means, clasificadores multiclase y regresores de popularidad, con evaluación apropiada.
5. **Comunicación:** informe Quarto integrador R + Python, dashboard con filtros y defensa oral.

## Resultados reportados por los artefactos originales

- Clasificación de género: **Gradient Boosting ~58.66 %** de exactitud y **AUC ~0.866**.
- Popularidad: **Gradient Boosting R² ~0.1624**, RMSE ~18.81.
- Interpretación: las variables de audio distinguen parcialmente géneros, pero explican poco de la popularidad.

Los CSV de `powerbi/` y los informes originales son la fuente numérica para estas cifras. Sus métricas no son verificadas nuevamente al abrir el dashboard.

## Defensa y contribuciones

Ver `docs/presentacion_guion.md` para una propuesta de exposición de 18 minutos y `docs/AUTORIA.md` para la distribución preliminar de tareas; **el grupo debe verificar los roles reales antes de entregar**.

## Entrega

Publicar `reports/informe_final.html` una vez renderizado, comprobar el funcionamiento del dashboard y preparar el material visual de defensa. Streamlit es una alternativa permitida por la rúbrica al archivo `.pbix`; en esta versión **no se incluye un archivo nativo Power BI**.
