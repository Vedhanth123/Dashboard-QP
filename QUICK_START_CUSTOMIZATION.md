# HDFC Dashboard Customization - Quick Start

This guide focuses specifically on how to customize the visualizations for CEO presentations, covering all the new features that have been implemented.

## Ways to Customize Your Visualizations

### 1. Interactive Streamlit Dashboard
The easiest way to create custom visualizations:

```bash
streamlit run hdfc_dashboard.py
```

Key customization features:
- Custom titles and subtitles
- Custom column titles
- Axis labels
- Color schemes
- Background styles
- Value formatting
- Chart layout options
- Export to high-resolution images

### 2. Jupyter Notebook
For more programmatic control with code examples:

Open `CEO_Dashboard.ipynb` in Jupyter or VS Code to see working examples of:
- Basic customization
- Advanced formatting
- Complete dashboard creation
- Export options

### 3. Python API (hdfc_viz module)
For maximum flexibility and programmatic use:

```python
from hdfc_viz import plot_bar_chart, create_dashboard

# Example 1: Simple customization
fig, axes = plot_bar_chart(
    df=your_dataframe,
    columns=['Column1', 'Column2'],
    title="Your Custom Title",
    subtitle="Your Custom Subtitle",
    color_scheme="hdfc_brand"
)

# Example 2: Full customization
fig, axes = plot_bar_chart(
    df=your_dataframe,
    columns=['Column1', 'Column2'],
    title="Your Custom Title",
    subtitle="Your Custom Subtitle",
    column_titles={
        "Column1": "Custom Title 1",
        "Column2": "Custom Title 2"
    },
    xlabel="X-Axis Label",
    ylabels="Y-Axis Label",
    color_scheme="corporate",
    bg_style="presentation",
    value_format={
        "Column1": {"is_percentage": True, "precision": 1},
        "Column2": {"is_percentage": False, "precision": 0}
    }
)
```

## Common Customization Tasks

### Customizing Chart Titles
```python
plot_bar_chart(
    # ...other parameters...
    title="Main Title Here",
    subtitle="Subtitle Text Here"
)
```

### Customizing Column Titles
```python
plot_bar_chart(
    # ...other parameters...
    column_titles={
        "Original Column Name 1": "Custom Title\nWith Line Break",
        "Original Column Name 2": "Another Custom Title"
    }
)
```

### Choosing Color Schemes
Available color schemes:
- `"corporate"`: Professional blue to orange gradient
- `"vibrant"`: Bold, distinct colors
- `"pastel"`: Soft, muted colors
- `"hdfc_brand"`: HDFC brand colors
- `"gradient_blue"`: Blue gradient
- `"gradient_red"`: Red gradient

```python
plot_bar_chart(
    # ...other parameters...
    color_scheme="hdfc_brand"  # Choose from options above
)
```

### Customizing Axis Labels
```python
plot_bar_chart(
    # ...other parameters...
    xlabel="Work Status",
    ylabels="Number of Employees"  # Can be string or dict mapping columns to labels
)
```

### Formatting Values
```python
plot_bar_chart(
    # ...other parameters...
    value_format={
        "Column1": {"is_percentage": True, "precision": 1},
        "Column2": {"is_percentage": False, "precision": 0}
    }
)
```

### Bar Style Customization
```python
plot_bar_chart(
    # ...other parameters...
    bar_width=0.7,  # 0.0-1.0
    bar_edge_color="white",
    bar_edge_width=0.5,
    bar_alpha=0.9  # Transparency (0.0-1.0)
)
```

### Background Style Options
- `"default"`: Clean style with light grid
- `"minimal"`: Minimal style with no grid
- `"classic"`: Dark grid background
- `"presentation"`: Optimal style for presentations

```python
plot_bar_chart(
    # ...other parameters...
    bg_style="presentation"
)
```

## Command Line Usage

```bash
# Generate dashboards for all sheets
python generate_dashboard.py --file HDFC_modified.xlsx --output ./exports

# With custom styling
python generate_dashboard.py --file HDFC_modified.xlsx --output ./exports --style presentation --colors hdfc_brand
```

## Interactive Dashboard Usage

1. Launch the dashboard:
   ```bash
   streamlit run hdfc_dashboard.py
   ```

2. Use the sidebar options to:
   - Select Excel file and sheet
   - Choose columns to display
   - Set title and subtitle
   - Customize column titles
   - Set axis labels
   - Choose color scheme
   - Configure bar style
   - Set value formatting
   - Adjust layout

3. Click "Generate Plot" to create the visualization

4. Export to high-resolution images using the export options below each chart
