# AGS Viewer

A [Streamlit](https://streamlit.io/) app to explor an [`.ags` geotechnical data](https://www.ags.org.uk/data-format/) file.

As of 2023-12-03 this is very much a work in progress. Some functionality goals for this are:

1. Allow the user to upload a `.ags` file and perform some vailidations on it:
    - It is, in fact, an `.ags` file. Use the [ags-validator](https://gitlab.com/ags-data-format-wg/agsi-validator-library) built by the [AGS working group](https://gitlab.com/ags-data-format-wg)
    - Check for conflicts in geology (provide a warning to the user):
        - Samples do not bridge geologic cotacts.
        - There are no gaps in geology.
        - Geology zones don't extend past the limits of the borehole.
2. Show some gross data on the file:
    - Summary counts of Borings, Samples, Tables, Records
    - Show waffle chart (or similar) of length of geology represented
3. Have a selection of summary charts to show values on a geology basis:
    - Histogram with normal distribution (or log for permeability data).
    - Grain size distribution box plots.
    - RQD or other rock properties (on a box plot or similar).

Example file is provided by the [AGS working group](https://gitlab.com/ags-data-format-wg/AGS_X.0)