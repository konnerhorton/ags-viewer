# AGS Viewer

A [Streamlit](https://streamlit.io/) app to explore an [`.ags` geotechnical data](https://www.ags.org.uk/data-format/) file.

As of 2023-12-03 this is very much a work in progress. Some functionality goals for this are:

- [X] Allow the user to upload a `.ags` file and validate it. Use the [ags-validator](https://gitlab.com/ags-data-format-wg/agsi-validator-library) built by the [AGS working group](https://gitlab.com/ags-data-format-wg)
- [ ] If coordinate / grid information exists, plot the boreholes on a map. There could be some functionality for the user to input the correct grid information if not available in the `.ags`.
- [ ] Show some gross data on the file:
  - [ ] Summary counts of Borings, Samples, Tables, Records
  - [ ] Show waffle chart (or similar) of length of geology represented

- [ ] Have a selection of summary charts to show values on a geology basis:
  - [ ] Histogram with normal distribution (or log for permeability data).
  - [ ] Grain size distribution box plots.
  - [ ] RQD or other rock properties (on a box plot or similar).

Example file is provided by the [AGS working group](https://gitlab.com/ags-data-format-wg/ags-python-library/-/tree/main/examples?ref_type=heads)
