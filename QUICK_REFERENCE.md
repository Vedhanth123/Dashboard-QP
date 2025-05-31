# HDFC Visualization Tools Quick Reference

This guide provides a quick reference for using the HDFC data visualization tools.

## Available Tools

### 1. Jupyter Notebook
- `CEO_Dashboard.ipynb`: Interactive examples in Jupyter
- `Dashboard.ipynb`: Original visualization notebook

### 2. Python Modules
- `hdfc_viz.py`: Core visualization library with customizable functions
- `generate_dashboard.py`: Command-line tool for batch processing
- `generate_examples.py`: Script to create example visualizations
- `hdfc_dashboard.py`: Interactive Streamlit dashboard application

### 3. Documentation
- `README.md`: Project overview and basic usage
- `CUSTOMIZATION_GUIDE.md`: Detailed customization options
- `ENHANCEMENT_SUMMARY.md`: Summary of implementation features

## Quick Start Commands

### Generate Dashboard Images
```powershell
python generate_dashboard.py --file HDFC_modified.xlsx --output ./exports
```

### Generate Example Visualizations
```powershell
python generate_examples.py
```

### Launch Interactive Dashboard
```powershell
streamlit run hdfc_dashboard.py
```

## Key Functions Reference

### Plot a Single Chart Group
```python
from hdfc_viz import plot_bar_chart

fig, axes = plot_bar_chart(
    df=data,
    columns=columns_to_plot,
    title="Your Chart Title",
    color_scheme='hdfc_brand'
)
```

### Create a Complete Dashboard
```python
from hdfc_viz import create_dashboard

dashboard = create_dashboard(
    df=data,
    sheet_name="Sheet Name",
    column_groups=[list_of_columns_group1, list_of_columns_group2]
)
```

## Color Schemes
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

## Common Parameters

### Basic Configuration
- `df`: DataFrame with data
- `columns`: Columns to visualize
- `title`, `subtitle`: Chart titles
- `color_scheme`: Color palette
- `bg_style`: Background style

### Layout and Size
- `figsize`: Figure dimensions (width, height)
- `layout`: Subplot arrangement (rows, cols)
- `sharey`: Whether to share y-axis scale

### Value Display
- `show_values`: Show values on bars
- `value_format`: Formatting specifications
- `value_rotation`: Rotation of value labels

### Bar Style
- `bar_width`: Width of bars (0-1)
- `bar_edge_color`: Color of bar edges
- `bar_edge_width`: Width of bar edges
- `bar_alpha`: Opacity of bars (0-1)

### Export Options
- `save_path`: Path to save the figure
- `dpi`: Resolution for saved figure
- `show_plot`: Whether to display the plot

## Example Usage

### Basic Chart with Custom Title
```python
plot_bar_chart(
    df=data,
    columns=data.columns[:2],
    title="Cohort Analysis",
    subtitle="January 2025"
)
```

### Professional Chart with Custom Formatting
```python
plot_bar_chart(
    df=data,
    columns=data.columns,
    title="Quarterly Performance",
    color_scheme='hdfc_brand',
    bg_style='presentation',
    bar_edge_color='white',
    value_format={'Column1': {'is_percentage': True}}
)
```
