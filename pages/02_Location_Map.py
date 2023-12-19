# Import third party libraries
import pandas as pd
import plotly.express as px
from pyproj import Transformer
import streamlit as st

# Import local libries
from utilities.ags_utils import ags_to_dfs
from utilities.ags_utils import AGS_VERBOSE_MAP

st.title("Location Map")

st.markdown(
    """Here, you can use the sidebar (to the left) to provide the Coordinate Reference System (CRS) to use for your project. The CRS you select should be one of those available at [epsg.io](https://epsg.io/). If you're project can not be represented by a standard value from [epsg.io](https://epsg.io/), you will have to use the closest approximation (and don't put too much stock in the precision on the map). This could be the case for Canada and Australia, where the use of grid shift files is common."""
)

crs_from = None
df = None
transformer = None
crs_to = "EPSG:4326"
crs_from = "EPSG:27700"

with st.sidebar:
    st.markdown(
        "Identify the Coordinate Reference System (CRS) to use for your `.ags.` file. Use ONLY the numbers listed at [epsg.io](https://epsg.io/). For example, the sample data set uses EPSG:27700, so you would input `27700` in the space below."
    )
    crs_from = st.text_input(label="Input your CRS")


try:
    df = st.session_state.ags_data["LOCA"]
except:
    st.write(
        "Please check to make sure you've uploaded an `.ags` file. If you do not have an `.ags` file to test out, you can use the sidebar to go to the `File Import` page and rerun it so that the sample file loads."
    )

try:
    transformer = Transformer.from_crs(crs_from, crs_to, always_xy=True)
except:
    st.write("Please input a valid EDPS")

if df is not None and not df.empty and transformer and crs_from:
    for c in ["LOCA_NATE", "LOCA_NATN"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df[["Lon", "Lat"]] = df.apply(
        lambda x: transformer.transform(x["LOCA_NATE"], x["LOCA_NATN"]),
        axis=1,
        result_type="expand",
    )
    df = df.loc[df["LOCA_NATE"].notnull()]

    st.plotly_chart(
        px.scatter_mapbox(
            df,
            lat="Lat",
            lon="Lon",
            mapbox_style="open-street-map",
            height=600,
            hover_data={"LOCA_ID": True, "Lat": ":.2f", "Lon": ":.2f"},
        )
    )
else:
    if df is not None:
        if transformer:
            st.write(
                "Looks like there is no CRS code, or the code you have entered is not a valid. Please used the sidebar to input your project's CRS."
            )
