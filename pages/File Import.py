# Import standard libraries


# Import third party libraries
import pandas as pd
from python_ags4 import AGS4
import streamlit as st


# Import local libries
from utilities.ags_names import AGS_VERBOSE_MAP


input_ags = "data/East West Rail BGS Pre October 2018 upload (partial).ags"

tables, headings = AGS4.AGS4_to_dataframe(
    "data/East West Rail BGS Pre October 2018 upload (partial).ags"
)

table_dict = {k: v for k, v in AGS_VERBOSE_MAP.items() if k in headings.keys()}
table_list_text = "\n".join([f"- {k} - {v}" for k, v in table_dict.items()])

st.write(table_list_text)
