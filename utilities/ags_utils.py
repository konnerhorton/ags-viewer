# Import third party libraries
import pandas as pd
from python_ags4 import AGS4


def ags_to_dfs(ags):
    # Load `.ags` as dict-like objects of tables and headings
    tables, headings = AGS4.AGS4_to_dataframe(ags)

    # Remove the top two rows in the tables and store as df's in a dict
    dfs = {i: tables[i].loc[2:] for i in tables.keys()}
    return dfs


AGS_VERBOSE_MAP = {
    "PROJ": "Project Information",
    "ABBR": "Abbreviation Definitions",
    "DICT": "User Defined Groups and Headings",
    "FILE": "Associated Files",
    "TRAN": "Data File Transmission Information / Data Status",
    "TYPE": "Definition of Data Types",
    "UNIT": "Definition of Units",
    "CLSS": "Classification tests",
    "CONG": "Consolidation Tests - General",
    "CONS": "Consolidation Tests - Data",
    "CORE": "Coring Information",
    "GEOL": "Field Geological Descriptions",
    "GRAG": "Particle Size Distribution Analysis - General",
    "GRAT": "Particle Size Distribution Analysis - Data",
    "SCPG": "Static Cone Penetration Tests - General",
    "SCPT": "Static Cone Penetration Tests - Data",
    "SCPP": "Static Cone Penetration Tests - Derived Parameters",
    "LOCA": "Location Details",
    "DETL": "Stratum Detail Descriptions",
    "SAMP": "Sample Information",
    "GCHM": "Geotechnical Chemistry Testing",
    "LDEN": "Density tests",
    "LLPL": "Liquid and Plastic Limit Tests",
    "LNMC": "Water/Moisture Content Tests",
    "LPDN": "Particle Density Tests",
    "LPEN": "Laboratory Hand Penetrometer Tests",
    "TREG": "Triaxial Tests - Effective Stress - General",
    "TRET": "Triaxial Tests - Effective Stress - Data",
    "TRIG": "Triaxial Tests - Total Stress - General",
    "TRIT": "Triaxial Tests - Total Stress - Data",
    "GRAD": "Particle size distribution data",
    "RELD": "Relative density test",
    "STCN": "Static cone penetration test",
}

REFERENCE_TABLES = ["PROJ", "ABBR", "DICT", "TRAN", "TYPE", "UNIT"]
