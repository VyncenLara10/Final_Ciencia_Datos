# Defensa oral (18 minutos) — Proyecto Spotify

> Guion propuesto para organizar la exposición. Los roles son una propuesta y deben validarse con el grupo antes de declarar contribuciones definitivas.

| Tiempo | Expositor sugerido | Diapositivas | Demostración |
|---|---|---|---|
| 0–4 min | Vyncen Lara | 1–3 | Problema, objetivos y dataset público (32,833 filas originales, 26,229 limpias) |
| 4–8 min | Roger Monterroso | 4–6 | Reglas de limpieza y EDA, correlaciones, sesgos |
| 8–13 min | Juan Marcos | 7–9 | Clustering, clasificación (accuracy ≈58.7%, AUC ≈0.87) y popularidad (R²≈0.16) |
| 13–18 min | Jose Ronquillo | 10–12 | Dashboard en vivo, filtros, conclusiones y limitaciones |

## Mensaje principal de cada diapositiva

1. Portada: pregunta central, fuente y equipo.
2. Investigación: género y popularidad no son lo mismo.
3. Dataset: Spotify/TidyTuesday, filas, variables y temporalidad.
4. Depuración: faltantes, duplicados, ingeniería de variables.
5. Géneros: medias y distribuciones de energía, bailabilidad y valencia.
6. Limitaciones: género de playlist, cero popularidad, representación.
7. Aprendizaje no supervisado: clusters de sonido y solapamiento de géneros.
8. Clasificación de género: comparar cinco modelos, precisión y AUC.
9. Popularidad: RMSE, MAE y R²; por qué 0.16 no explica el éxito.
10. Dashboard: filtrar género, año, popularidad y mostrar interactividad.
11. Conclusiones: audio explica rasgos musicales mejor que éxito.
12. Reproducibilidad: scripts, Quarto, fuentes, preguntas.

## Preguntas posibles y respuestas breves

**¿Por qué limpiar duplicados?** Una canción repetida en playlists podría sesgar distribuciones y crear filtraciones si aparece a la vez en entrenamiento y prueba; se eligió una sola aparición por canción.

**¿El género es una verdad de Spotify?** No. Es una etiqueta de la playlist, utilizada como proxy y señalada como limitación.

**¿Qué significa accuracy 58.7 %?** La proporción correcta en la evaluación reportada; compararla con un azar de 1/6 solo es ilustrativo si las clases están equilibradas.

**¿Qué significa R² 0.16?** En el conjunto evaluado, el modelo explica aproximadamente 16 % de la variación de popularidad, y no demuestra causalidad.

**¿Por qué usar dos lenguajes?** Python facilita limpieza, clustering y clasificación; R facilita pruebas inferenciales, visualización y regresión.

**¿Es reproducible?** Los datos y fuentes, código R/Python, informe Quarto y dashboard están versionados. Los HTML previos permiten verificar resultados históricos.

## Lista de comprobación antes de presentar

- Abrir el HTML unificado después de ejecutar `quarto render reports/informe_final.qmd`.
- Ejecutar `streamlit run dashboard/app.py` y comprobar filtros.
- Comprobar métricas del CSV y ausencia de errores en cada entorno.
- Preparar capturas de respaldo del dashboard por si falla internet.
