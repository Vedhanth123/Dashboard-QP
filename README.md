# HDFC Data Analysis Dashboard

This project provides enhanced visualization tools for HDFC data analysis, designed specifically for creating visually appealing and customizable charts for executive presentations.

## Features

- **Customizable Titles and Labels**: Easily set chart titles, subtitles, and axis labels
- **Professional Color Schemes**: Multiple pre-defined color palettes optimized for presentations
- **Smart Value Formatting**: Automatic or manual formatting for percentages, integers, and decimals
- **Enhanced Visual Styles**: Different background styles, grid options, and bar customizations
- **Export Capabilities**: Save high-resolution images for presentations
- **CEO-level Visualizations**: Professionally designed charts ready for executive presentations
- **Interactive Dashboard**: Real-time customization with Streamlit interface
- **Example Generator**: Script to create sample visualizations for all sheets

## Quick Start

1. Open the `CEO_Dashboard.ipynb` notebook for examples of how to use the visualization module.
2. Use the `hdfc_viz.py` module in your own notebooks for custom visualizations.
3. Launch the interactive dashboard with `streamlit run hdfc_dashboard.py`
4. Generate example visualizations with `python generate_examples.py`

## Core Functions

### `plot_bar_chart()`

Creates customizable bar charts with the following key parameters:

- `df`: DataFrame containing data to plot
- `columns`: List of columns to visualize
- `title`, `subtitle`: Main chart titles
- `column_titles`: Custom titles for each column
- `xlabel`, `ylabels`: Axis labels
- `color_scheme`: Color palette to use
- `bg_style`: Background style
- `show_values`: Whether to display values on bars
- `value_format`: Formatting options for values
- `save_path`: Path to save the figure
- `layout`: Subplot layout configuration

### `create_dashboard()`

Creates a complete dashboard with multiple chart groups:

- `df`: Data to visualize
- `sheet_name`: Excel sheet name
- `column_groups`: Groups of columns to plot together
- `custom_titles`, `custom_subtitles`: Titles for each group
- `custom_column_titles`: Column titles for each group
- `value_formats`: Formatting options by column
- `output_path`: Base path for saving charts

## Color Schemes

The following color schemes are available:
- `corporate`: Professional blue to orange gradient
- `vibrant`: Bold, distinct colors
- `pastel`: Soft, muted colors
- `hdfc_brand`: HDFC brand colors
- `gradient_blue`: Blue gradient
- `gradient_red`: Red gradient

## Background Styles

- `default`: Clean style with light grid
- `minimal`: Minimal style with no grid
- `classic`: Dark grid background
- `presentation`: Optimal style for presentations

## Example

```python
from hdfc_viz import plot_bar_chart

# Plot with custom titles and colors
fig, axes = plot_bar_chart(
    df=data,
    columns=data.columns[:2],
    title="Cohort-wise Head Count Distribution",
    subtitle="Analysis of CAP LRM and CAP 12 Cohorts",
    column_titles={
        "CAP LRM cohort": "LRM Cohort\nHead Count",
        "CAP 12  cohort": "Cohort 12\nHead Count"
    },
    xlabel="Work Status",
    ylabels="Number of Employees",
    color_scheme='hdfc_brand',
    bg_style='presentation',
    bar_edge_color='white',
    bar_edge_width=0.5
)
```

## Export Options

You can export individual charts or entire dashboards as high-resolution images:

```python
# Export a single chart
plot_bar_chart(..., save_path="my_chart.png", dpi=300)

# Export a full dashboard
create_dashboard(..., output_path="dashboard_", dpi=300)
```
