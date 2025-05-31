# HDFC Dashboard Customization Guide

This guide explains how to customize your HDFC data visualizations for CEO presentations.

## Key Features Implemented

1. **Manual Customization Options**
   - Chart titles and subtitles
   - Axis labels
   - Column titles
   - Value formatting and precision
   - Color schemes and background styles

2. **Visual Enhancements for CEO Presentations**
   - Professional color palettes designed for impact
   - Shadow effects on value labels for better visibility
   - Advanced formatting based on data type (percentages, integers, decimals)
   - Gradient color options for more sophisticated look
   - Optimized spacing and layout
   - Custom column titles with intelligent line breaks
   - Image export for PowerPoint integration

3. **Smart Formatting Features**
   - Automatic percentage detection and formatting
   - Dynamic decimal precision based on value magnitude
   - Type-aware value display (count vs. percentage)
   - Title text wrapping for readability
   - Intelligent subplot layout calculation

## How to Customize Your Charts

### Basic Customization

```python
fig, axes = plot_bar_chart(
    df=your_data,
    columns=your_data.columns[:2],
    title="Your Custom Title",
    subtitle="Your Custom Subtitle",
    xlabel="X-Axis Label",
    ylabels="Y-Axis Label",
    color_scheme='hdfc_brand'  # Try 'corporate', 'vibrant', 'pastel', etc.
)
```

### Advanced Customization

```python
# Custom column titles
column_titles = {
    "Original Column Name 1": "Custom\nTitle 1",
    "Original Column Name 2": "Custom\nTitle 2"
}

# Custom value formatting
value_format = {
    "Column1": {'is_percentage': True, 'precision': 1},
    "Column2": {'is_percentage': False, 'precision': 0}
}

fig, axes = plot_bar_chart(
    df=your_data,
    columns=your_data.columns,
    title="Custom Title",
    subtitle="Custom Subtitle",
    column_titles=column_titles,
    value_format=value_format,
    color_scheme='gradient_blue',
    bg_style='presentation',
    bar_edge_color='white',
    bar_edge_width=0.5,
    bar_alpha=0.85,
    annotate_offset=(0, 8)  # Adjust label position
)
```

### Creating Complete Dashboards

For comprehensive dashboards with multiple chart groups:

```python
# Define column groups for the dashboard
column_groups = [
    your_data.columns[:2].tolist(),
    your_data.columns[2:6].tolist(),
    your_data.columns[6:10].tolist()
]

# Define custom titles for each group
custom_titles = {
    0: "Title for Group 1",
    1: "Title for Group 2",
    2: "Title for Group 3"
}

# Create the dashboard
dashboard = create_dashboard(
    df=your_data,
    sheet_name="Your Sheet Name",
    column_groups=column_groups,
    output_path="path/to/save/images",
    custom_titles=custom_titles,
    color_schemes=['hdfc_brand', 'corporate', 'gradient_blue'],
    bg_style='presentation'
)
```

## Command Line Usage

You can also generate dashboards from the command line:

```
python generate_dashboard.py --file HDFC_modified.xlsx --output ./exports --style presentation --colors hdfc_brand
```

## Additional Customization Options

- **Bar styling**: Adjust width, edge color, edge width, and opacity
- **Grid options**: Show/hide and adjust transparency
- **Value display**: Control font size, position, rotation
- **Layout**: Auto-calculate or manually specify subplot arrangements
- **Figure size**: Default or custom dimensions
- **Export**: Save as PNG, JPG, PDF, or SVG

Refer to the `hdfc_viz.py` module documentation for complete details on all available options.
