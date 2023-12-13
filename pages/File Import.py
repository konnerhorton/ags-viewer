# Import standard libraries
import tempfile


# Import third party libraries
import pandas as pd
from python_ags4 import AGS4
import streamlit as st


# Import local libries
from utilities.ags_names import AGS_VERBOSE_MAP

# Identify example file
example_ags = "data/East West Rail BGS Pre October 2018 upload (partial).ags"
file_path = example_ags

st.header("Upload and validate")
st.markdown(
    """Use the sidebar (to the left) to upload your `.ags` file. The `AGS4.check_file()`
    function will validate the file. Output from `check_file()` will be displayed below
    as tables under their respective rule labels. Metadata for the file is shown last.
    If the only table visible is the metadata table, then the file is `.ags` compatible."""
)
st.markdown(
    """  
    It may be the case that `check_file()` cannot be run on the uploaded file. In this
    case an error message will appear below without and output tables."""
)
st.markdown(
    """For a complete list of rules, refer to the documentation available at the
    [AGS website](https://www.ags.org.uk/data-format/ags4-data-format/ags-4-1/)"""
)

# Prompt user for input file
with st.sidebar:
    ags_input = st.file_uploader(
        "Upload your `.ags` file",
        type=".ags",
    )


if ags_input:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(ags_input.getvalue())
        file_path = tmp_file.name

try:
    results = AGS4.check_file(file_path)
    for k in results.keys():
        st.write(k)
        st.dataframe(results[k], use_container_width=True)

except:
    st.write(
        "Sorry, looks like this is not `.ags` compatible. Please check the contents and try again."
    )
