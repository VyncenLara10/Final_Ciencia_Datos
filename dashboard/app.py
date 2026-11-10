"""Dashboard interactivo de Spotify. Ejecutar: streamlit run dashboard/app.py"""
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "powerbi" / "spotify_powerbi.csv"
CLASIF = ROOT / "powerbi" / "resultados_clasificacion.csv"
POPULAR = ROOT / "powerbi" / "resultados_popularidad.csv"
st.set_page_config(page_title="Spotify | Ciencia de Datos", page_icon="🎵", layout="wide")
st.title("Spotify: género, sonido y popularidad")
st.caption("Proyecto final · Fuente: TidyTuesday 2020 · La etiqueta de género corresponde a la playlist, no necesariamente a la canción.")

@st.cache_data
def cargar(path):
    return pd.read_csv(path, encoding="utf-8-sig")

if not DATA.exists():
    st.error(f"No se encontró {DATA}. Ejecuta desde el repositorio clonado.")
    st.stop()
df = cargar(DATA)
with st.expander("Columnas disponibles", expanded=False):
    st.write(list(df.columns))
genre_col = next((c for c in ["genero", "playlist_genre"] if c in df.columns), None)
pop_col = next((c for c in ["popularidad", "track_popularity"] if c in df.columns), None)
year_col = next((c for c in ["anio", "year"] if c in df.columns), None)
cluster_col = next((c for c in ["nombre_cluster", "cluster"] if c in df.columns), None)
if not genre_col:
    st.error("La tabla no tiene una columna de género reconocible.")
    st.stop()
df[genre_col] = df[genre_col].fillna("Sin género").astype(str)
st.sidebar.header("Filtros interactivos")
generos = sorted(df[genre_col].unique())
seleccion = st.sidebar.multiselect("Género de playlist", generos, default=generos)
view = df[df[genre_col].isin(seleccion)].copy()
if year_col:
    years = pd.to_numeric(df[year_col], errors="coerce")
    valid_years = years.dropna()
    if not valid_years.empty:
        low, high = int(valid_years.min()), int(valid_years.max())
        periodo = st.sidebar.slider("Año de lanzamiento", low, high, (low, high))
        view = view[pd.to_numeric(view[year_col], errors="coerce").between(*periodo)]
if pop_col:
    view[pop_col] = pd.to_numeric(view[pop_col], errors="coerce")
    rango = st.sidebar.slider("Popularidad", 0, 100, (0, 100))
    view = view[view[pop_col].between(*rango) | (view[pop_col].isna() & (rango == (0, 100)))]
if cluster_col:
    grupos = sorted(df[cluster_col].dropna().astype(str).unique().tolist())
    chosen = st.sidebar.multiselect("Cluster de audio", grupos, default=grupos)
    view = view[view[cluster_col].astype(str).isin(chosen)]
if view.empty:
    st.warning("No hay registros con los filtros actuales.")
    st.stop()
c1,c2,c3,c4 = st.columns(4)
c1.metric("Canciones filtradas", f"{len(view):,}")
c2.metric("Géneros", view[genre_col].nunique())
c3.metric("Popularidad media", f"{view[pop_col].mean():.1f}" if pop_col and view[pop_col].notna().any() else "N/D")
c4.metric("Canciones con popularidad", f"{view[pop_col].notna().sum():,}" if pop_col else "N/D")
tab1,tab2,tab3,tab4=st.tabs(["Panorama", "Perfiles de audio", "Modelos", "Datos y limitaciones"])
with tab1:
    left,right=st.columns(2)
    with left:
        conteo=view[genre_col].value_counts().rename_axis("Género").reset_index(name="Canciones")
        st.plotly_chart(px.bar(conteo,x="Género",y="Canciones",color="Género",title="Canciones por género"),use_container_width=True)
    with right:
        if pop_col:
            st.plotly_chart(px.histogram(view.dropna(subset=[pop_col]),x=pop_col,color=genre_col,nbins=25,title="Distribución de popularidad"),use_container_width=True)
    if year_col:
        temporal=view.assign(_anio=pd.to_numeric(view[year_col],errors="coerce")).dropna(subset=["_anio"])
        temporal=temporal.groupby(["_anio",genre_col]).size().reset_index(name="Canciones")
        st.plotly_chart(px.line(temporal,x="_anio",y="Canciones",color=genre_col,title="Registros por año de lanzamiento"),use_container_width=True)
with tab2:
    audio=[c for c in ["danceability","energy","speechiness","acousticness","instrumentalness","liveness","valence"] if c in view]
    if audio:
        elegido=st.selectbox("Característica musical",audio)
        st.plotly_chart(px.box(view,x=genre_col,y=elegido,color=genre_col,points=False,title=f"Distribución de {elegido} por género"),use_container_width=True)
        perfil=view.groupby(genre_col)[audio].mean(numeric_only=True)
        st.plotly_chart(px.imshow(perfil,aspect="auto",color_continuous_scale="Viridis",title="Promedios de características (0 a 1)"),use_container_width=True)
    if "energy" in view and "danceability" in view:
        sample=view.sample(min(2500,len(view)),random_state=42)
        st.plotly_chart(px.scatter(sample,x="danceability",y="energy",color=genre_col,opacity=.5,hover_data=[c for c in ["track_name","track_artist"] if c in sample],title="Bailabilidad frente a energía (muestra reproducible)"),use_container_width=True)
with tab3:
    if CLASIF.exists():
        c=cargar(CLASIF)
        st.subheader("Clasificación de género · Python")
        st.dataframe(c,use_container_width=True,hide_index=True)
        st.plotly_chart(px.bar(c,x="Modelo",y="Exactitud (accuracy)",title="Exactitud por modelo",range_y=[0,1]),use_container_width=True)
    if POPULAR.exists():
        p=cargar(POPULAR)
        st.subheader("Popularidad · R")
        st.dataframe(p,use_container_width=True,hide_index=True)
        reg=p.dropna(subset=["R2"]) if "R2" in p else pd.DataFrame()
        if not reg.empty:
            st.plotly_chart(px.bar(reg,x="Modelo",y="R2",title="Varianza explicada (R²)"),use_container_width=True)
    st.info("Las métricas son resultados previamente exportados por los análisis originales; no se reentrena al cambiar los filtros.")
with tab4:
    st.markdown("""**Unidad de análisis:** después de la deduplicación, una canción por identificador/nombre-artista.
**Sesgos:** playlist y género no equivalen a una clasificación musical universal; la muestra no representa todo Spotify.
**Popularidad:** instantánea histórica de 2020; los registros con valor 0 se interpretaron como dato faltante según el procedimiento original, decisión discutible que debe explicarse.
**Modelos:** asociación no implica causalidad; no se puede concluir que las variables de audio causen el éxito.
**Fuente:** [TidyTuesday · 2020-01-21](https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-01-21).
**Reproducibilidad:** se usan las tablas versionadas en `powerbi/`; el dashboard no llama a APIs privadas.""")
    st.download_button("Descargar registros filtrados (CSV)", view.to_csv(index=False).encode("utf-8-sig"), "spotify_filtrado.csv", "text/csv")
