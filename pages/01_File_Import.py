# Import standard libraries
import io
import os
import tempfile


# Import third party libraries
import pandas as pd
from python_ags4 import AGS4
import streamlit as st


# Import local libries
from utilities.ags_utils import ags_to_dfs
from utilities.ags_utils import AGS_VERBOSE_MAP


# Identify example file
EXAMPLE_AGS_PATH = "data/East West Rail BGS Pre October 2018 upload (partial).ags"
AGS_VALIDATION_RESULTS = None
# Prompt user for input file
with st.sidebar:
    ags_input = st.file_uploader(
        "Upload your `.ags` file",
        type=".ags",
    )

if ags_input:
    with tempfile.NamedTemporaryFile(
        delete=False, suffix=os.path.splitext(ags_input.name)[1]
    ) as tmp_file:
        tmp_file.write(ags_input.getvalue())
        PROJECT_AGS_PATH = tmp_file.name
else:
    PROJECT_AGS_PATH = EXAMPLE_AGS_PATH

try:
    AGS_VALIDATION_RESULTS = AGS4.check_file(PROJECT_AGS_PATH)
except:
    st.write(
        "Sorry, looks like this is not `.ags` compatible. Please check the contents and try again."
    )

if AGS_VALIDATION_RESULTS:
    for k in AGS_VALIDATION_RESULTS.keys():
        st.write(k)
        st.dataframe(AGS_VALIDATION_RESULTS[k], use_container_width=True)
    st.session_state.ags_data = ags_to_dfs(PROJECT_AGS_PATH)

# PROJECT_AGS_RAW = create_file_like_object(EXAMPLE_AGS_PATH)

# st.header("Upload and validate your file")
# st.markdown(
#     """Use the sidebar (to the left) to upload your `.ags` file. The `AGS4.check_file()`
#     function will validate the file. Output from `check_file()` will be displayed below
#     as tables under their respective rule labels. Metadata for the file is shown last.
#     If the only table visible is the metadata table, then the file is `.ags` compatible."""
# )
# st.markdown(
#     """
#     It may be the case that `check_file()` cannot be run on the uploaded file. In this
#     case an error message will appear below without and output tables."""
# )
# st.markdown(
#     """For a complete list of rules, refer to the documentation available at the
#     [AGS website](https://www.ags.org.uk/data-format/ags4-data-format/ags-4-1/)"""
# )
# st.markdown(
#     """Once your file is uploaded and validated, use the sidebar to navigate to other pages to explore your data."""
# )


# load_ags()


# def validate_ags():
#     global AGS_VALIDATION_RESULTS
#     try:
#         AGS_VALIDATION_RESULTS = AGS4.check_file(PROJECT_AGS_PATH)
#         # st.session_state.ags_data = ags_to_dfs(PROJECT_AGS_PATH)
#         # st.write(AGS4.AGS4_to_dataframe(PROJECT_AGS_PATH))
#         st.write(PROJECT_AGS_PATH)

#     except:
#         st.write(
#             "Sorry, looks like this is not `.ags` compatible. Please check the contents and try again."
#         )


# def display_ags_results():
#     try:
#         for k in AGS_VALIDATION_RESULTS.keys():
#             st.write(k)
#             st.dataframe(AGS_VALIDATION_RESULTS[k], use_container_width=True)
#     except:
#         st.write("no dice")


# validate_ags()
# display_ags_results()
