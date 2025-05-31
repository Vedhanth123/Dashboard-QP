"""
HDFC Data Visualization Module
----------------------------
Enhanced visualization module for HDFC data analysis with CEO-level presentation quality.
Features:
- Customizable titles, labels, and annotations
- Multiple color schemes and visual styles
- Smart formatting based on data types
- Layout options for different presentation needs
"""

# Export all functions and variables
__all__ = ['plot_bar_chart', 'create_dashboard', 'COLOR_SCHEMES', 'BG_STYLES']

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patheffects as path_effects
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm
import matplotlib.ticker as mticker
import textwrap

# Set default style settings
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

# Color schemes - professionally designed palettes
COLOR_SCHEMES = {
    'corporate': ["#003f5c", "#2f4b7c", "#665191", "#a05195", "#d45087", "#f95d6a", "#ff7c43", "#ffa600"],
    'vibrant': ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f"],
    'pastel': ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494", "#b3b3b3"],
    'hdfc_brand': ["#ED232A", "#0033A0", "#808080", "#FF6600", "#003366", "#FFCC00", "#00CCFF", "#009900"],
    'gradient_blue': ["#f7fbff", "#deebf7", "#c6dbef", "#9ecae1", "#6baed6", "#4292c6", "#2171b5", "#084594"],
    'gradient_red': ["#fff5f0", "#fee0d2", "#fcbba1", "#fc9272", "#fb6a4a", "#ef3b2c", "#cb181d", "#99000d"]
}

# Background styles
BG_STYLES = {
    'default': {'style': 'whitegrid', 'grid_alpha': 0.3},
    'minimal': {'style': 'white', 'grid_alpha': 0.0},
    'classic': {'style': 'darkgrid', 'grid_alpha': 0.1},
    'presentation': {'style': 'white', 'grid_alpha': 0.2}
}

def _format_value(value, is_percentage=False, precision=None):
    """Format values appropriately based on type and magnitude."""
    if pd.isna(value):
        return "N/A"
    
    if is_percentage:
        if precision is None:
            if abs(value) < 0.01:
                precision = 2
            else:
                precision = 1
        return f'{value:.{precision}%}'
    
    # If value is very close to an integer and >= 10
    if abs(value - round(value)) < 0.01 and value >= 10:
        return f'{int(value):,}'
    
    # Select precision based on value magnitude if not specified
    if precision is None:
        if abs(value) < 0.01:
            precision = 4
        elif abs(value) < 0.1:
            precision = 3
        elif abs(value) < 1:
            precision = 2
        elif abs(value) < 10:
            precision = 1
        else:
            precision = 0 if abs(value) % 1 < 0.01 else 2
    
    # Format with appropriate precision
    if precision == 0:
        return f'{int(value):,}'
    else:
        return f'{value:.{precision}f}'

def _wrap_text(text, width=20):
    """Wrap text to specified width."""
    return '\n'.join(textwrap.wrap(text, width=width))

def _get_gradient_colors(color_scheme, num_categories):
    """Get a gradient of colors for a given color scheme."""
    if isinstance(color_scheme, list):
        # Use provided list of colors
        colors = color_scheme
    elif color_scheme in COLOR_SCHEMES:
        # Use predefined color scheme
        colors = COLOR_SCHEMES[color_scheme]
    else:
        # Default to corporate scheme
        colors = COLOR_SCHEMES['corporate']
    
    # Ensure we have enough colors
    if len(colors) < num_categories:
        # Create a gradient from the first and last colors
        base_cmap = LinearSegmentedColormap.from_list("custom", [colors[0], colors[-1]])
        return [base_cmap(i/float(num_categories-1)) for i in range(num_categories)]
    
    # Return the needed number of colors
    return colors[:num_categories]

def plot_bar_chart(
    df, columns, 
    index_name=None,
    title=None, 
    subtitle=None,
    column_titles=None,
    xlabel=None,
    ylabels=None,
    color_scheme='corporate',
    bg_style='default',
    show_values=True,
    value_format=None,  # Dict with 'is_percentage' and optional 'precision' for each column
    value_rotation=0,
    figsize=None,
    layout=None,  # Tuple (rows, cols) or 'auto'
    sharey=False,
    save_path=None,
    dpi=300,
    show_plot=True,
    title_fontsize=20,
    subtitle_fontsize=16,
    column_title_fontsize=14,
    label_fontsize=12,
    value_fontsize=10,
    grid=True,
    legend=False,
    bar_width=0.7,  # Control bar width (0-1)
    bar_edge_color=None,  # Edge color for bars
    bar_edge_width=0,  # Edge width for bars
    bar_alpha=0.9,  # Opacity of bars
    annotate_offset=(0, 5)  # Offset for value annotations (x, y)
):
    """
    Create customizable bar charts for HDFC data analysis.
    
    Parameters:
    -----------
    df : pandas DataFrame
        The DataFrame containing the data to plot
    columns : list
        List of column names to plot
    index_name : str, optional
        Name for the index (x-axis category)
    title : str, optional
        Main chart title
    subtitle : str, optional
        Chart subtitle (smaller text below title)
    column_titles : dict, optional
        Dictionary mapping column names to custom titles
    xlabel : str, optional
        Label for x-axis
    ylabels : dict or str, optional
        Labels for y-axis (dict maps column names to labels, or single str for all)
    color_scheme : str or list, optional
        Name of predefined color scheme or list of colors
    bg_style : str, optional
        Background style ('default', 'minimal', 'classic', 'presentation')
    show_values : bool, optional
        Whether to show values on bars
    value_format : dict, optional
        Dict specifying formatting for each column {'col_name': {'is_percentage': bool, 'precision': int}}
    value_rotation : int, optional
        Rotation angle for value labels on bars
    figsize : tuple, optional
        Figure size (width, height)
    layout : tuple or str, optional
        Subplot layout as (rows, cols) or 'auto'
    sharey : bool, optional
        Whether to share y-axis scale across subplots
    save_path : str, optional
        Path to save the figure
    dpi : int, optional
        Resolution for saved figure
    show_plot : bool, optional
        Whether to display the plot
    title_fontsize : int, optional
        Font size for main title
    subtitle_fontsize : int, optional
        Font size for subtitle
    column_title_fontsize : int, optional
        Font size for individual column titles
    label_fontsize : int, optional
        Font size for axis labels
    value_fontsize : int, optional
        Font size for value annotations
    grid : bool, optional
        Whether to show grid lines
    legend : bool, optional
        Whether to show legend
    bar_width : float, optional
        Width of bars (0-1)
    bar_edge_color : str, optional
        Color of bar edges
    bar_edge_width : float, optional
        Width of bar edges
    bar_alpha : float, optional
        Opacity of bars (0-1)
    annotate_offset : tuple, optional
        Offset position for value annotations (x, y)
    """
    # Prepare the data
    data = df.copy()
    if isinstance(columns, str):
        columns = [columns]
    
    # Ensure columns exist in the dataframe
    valid_columns = [col for col in columns if col in data.columns]
    if not valid_columns:
        raise ValueError(f"None of the specified columns exist in the dataframe. Available columns: {data.columns.tolist()}")
    
    # Set index name if provided
    if index_name:
        data.index.name = index_name
    
    # Determine appropriate figure size if not specified
    if figsize is None:
        # Calculate based on number of subplots
        width = min(16, max(8, len(valid_columns) * 4))
        height = min(10, max(5, len(valid_columns) * 2))
        figsize = (width, height)
    
    # Determine layout if not specified
    if layout is None or layout == 'auto':
        if len(valid_columns) <= 2:
            layout = (1, len(valid_columns))
        elif len(valid_columns) <= 4:
            layout = (2, 2)
        else:
            cols = min(3, len(valid_columns))
            rows = (len(valid_columns) + cols - 1) // cols
            layout = (rows, cols)
    
    # Set style
    style_settings = BG_STYLES.get(bg_style, BG_STYLES['default'])
    sns.set_theme(style=style_settings['style'])
    
    # Create subplots
    fig, axes = plt.subplots(layout[0], layout[1], figsize=figsize, sharey=sharey)
    
    # Ensure axes is always a flattened array
    if layout[0] == 1 and layout[1] == 1:
        axes = np.array([axes])
    axes = np.array(axes).flatten()
    
    # Process each column and create plots
    for i, col in enumerate(valid_columns):
        if i >= len(axes):  # Safety check
            break
            
        ax = axes[i]
        
        # Determine if this column represents percentage data
        is_percentage = False
        precision = None
        
        if value_format and col in value_format:
            is_percentage = value_format[col].get('is_percentage', False)
            precision = value_format[col].get('precision', None)
        else:
            # Auto-detect percentage columns
            is_percentage = '%' in col.lower()
        
        # Get appropriate colors
        colors = _get_gradient_colors(color_scheme, len(data))
          # Create the bar plot (updated for newer Seaborn API)
        sns.barplot(
            ax=ax,
            x=data.index,
            y=data[col],
            hue=data.index,  # Use index values for hue to maintain color control
            palette=colors if isinstance(colors[0], tuple) else colors,
            saturation=1.0,
            width=bar_width,
            edgecolor=bar_edge_color,
            linewidth=bar_edge_width,
            alpha=bar_alpha,
            legend=False  # Don't show the legend for the hue
        )
        
        # Set column title (use custom if provided, otherwise the column name)
        if column_titles and col in column_titles:
            column_title = column_titles[col]
        else:
            column_title = _wrap_text(col, width=30)
            
        ax.set_title(column_title, fontsize=column_title_fontsize, fontweight="bold", pad=15)
        
        # Set x-axis label
        if xlabel:
            ax.set_xlabel(xlabel, fontsize=label_fontsize, labelpad=10)
        elif data.index.name:
            ax.set_xlabel(data.index.name, fontsize=label_fontsize, labelpad=10)
        
        # Set y-axis label
        if ylabels:
            if isinstance(ylabels, dict):
                if col in ylabels:
                    y_label = ylabels[col]
                else:
                    y_label = "Value"
            else:
                y_label = ylabels
            ax.set_ylabel(y_label, fontsize=label_fontsize, labelpad=10)
        elif is_percentage:
            ax.set_ylabel("Percentage", fontsize=label_fontsize, labelpad=10)
        else:
            # Check if all values are integers
            all_integers = all(abs(v - round(v)) < 0.01 for v in data[col].dropna())
            if all_integers:
                ax.set_ylabel("Count", fontsize=label_fontsize, labelpad=10)
            else:
                ax.set_ylabel("Value", fontsize=label_fontsize, labelpad=10)
        
        # Format y-axis for percentage
        if is_percentage:
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1%}'))
        
        # Annotate bars with values
        if show_values:
            for p in ax.patches:
                value = p.get_height()
                
                # Format the value
                label = _format_value(value, is_percentage=is_percentage, precision=precision)
                
                # Add the annotation with a subtle shadow effect for better visibility
                text = ax.annotate(
                    label,
                    (p.get_x() + p.get_width() / 2., value),
                    ha='center', va='bottom',
                    size=value_fontsize, fontweight="bold", color="#303030",
                    xytext=(annotate_offset[0], annotate_offset[1]),
                    textcoords='offset points',
                    rotation=value_rotation
                )
                
                # Add subtle shadow effect for better visibility
                text.set_path_effects([
                    path_effects.Stroke(linewidth=2, foreground='white'),
                    path_effects.Normal()
                ])
        
        # Add grid lines if requested
        if grid:
            ax.grid(True, axis='y', alpha=style_settings['grid_alpha'], linestyle='--')
        else:
            ax.grid(False)
            
        # Add legend if requested
        if legend:
            ax.legend(data.index, title=data.index.name or "Category", 
                     loc='upper right', fontsize=label_fontsize-2)
    
    # Remove any unused axes
    for j in range(len(valid_columns), len(axes)):
        fig.delaxes(axes[j])
      # Adjust layout with increased spacing between subplots
    plt.subplots_adjust(top=0.85, hspace=0.7, wspace=0.5)
    
    # Add overall title and subtitle
    if title:
        fig.suptitle(title, fontsize=title_fontsize, fontweight="bold", y=0.98)
        
        # Add subtitle if provided
        if subtitle:
            plt.figtext(0.5, 0.94, subtitle, horizontalalignment='center', 
                       fontsize=subtitle_fontsize, fontstyle='italic')
      # Tight layout with better spacing (but preserving the top for titles)
    plt.tight_layout(rect=[0, 0.05, 1, 0.93 if subtitle else 0.95])
    
    # Save figure if path is provided
    if save_path:
        plt.savefig(save_path, dpi=dpi, bbox_inches='tight')
    
    # Show plot if requested
    if show_plot:
        plt.show()
    else:
        plt.close()
    
    # Return figure and axes for further customization if needed
    return fig, axes


def create_dashboard(
    df, 
    sheet_name, 
    column_groups=None,  # List of column group definitions
    output_path=None,
    title_prefix="HDFC",
    color_schemes=None,  # List of color schemes to cycle through
    bg_style='presentation',
    show_plots=True,
    dpi=300,
    layout_options=None,  # List of layout tuples for each group
    custom_titles=None,  # Dict of custom titles for each group
    custom_subtitles=None,  # Dict of custom subtitles
    custom_column_titles=None,  # Nested dict {group_id: {col_name: custom_title}}
    value_formats=None,  # Nested dict {group_id: {col_name: {is_percentage, precision}}}
    global_xlabel=None,  # Global x-label for all charts
    global_ylabel=None,  # Global y-label for all charts
    figsize=None  # Override default figsize
):
    """
    Create a comprehensive dashboard with multiple chart groups.
    
    Parameters:
    -----------
    df : pandas DataFrame
        The data to visualize
    sheet_name : str
        Name of the Excel sheet (used for automatic titles)
    column_groups : list of lists, optional
        Groups of columns to plot together. If None, will be created automatically.
    output_path : str, optional
        Base path for saving charts, will be appended with group numbers
    title_prefix : str, optional
        Prefix for auto-generated titles
    color_schemes : list, optional
        List of color schemes to cycle through for different groups
    bg_style : str, optional
        Background style
    show_plots : bool, optional
        Whether to display plots
    dpi : int, optional
        Resolution for saved figures
    layout_options : list of tuples, optional
        Layout options for each group (rows, cols)
    custom_titles : dict, optional
        Custom titles for each group {group_index: "title"}
    custom_subtitles : dict, optional
        Custom subtitles for each group {group_index: "subtitle"}
    custom_column_titles : dict, optional
        Custom column titles {group_index: {column_name: "custom title"}}
    value_formats : dict, optional
        Value formatting options by group and column
    global_xlabel : str, optional
        X-axis label for all charts
    global_ylabel : str, optional
        Y-axis label for all charts
    figsize : tuple, optional
        Override default figure size
        
    Returns:
    --------
    list : List of (fig, axes) tuples for each chart group
    """
    results = []
    
    # Default color schemes if not provided
    if color_schemes is None:
        color_schemes = ['corporate', 'hdfc_brand', 'vibrant', 'pastel', 'gradient_blue', 'gradient_red']
    
    # Auto-create column groups if not provided
    if column_groups is None:
        if len(df.columns) <= 4:
            column_groups = [df.columns.tolist()]
        else:
            # Group columns into groups of 3-4
            column_groups = []
            cols = df.columns.tolist()
            for i in range(0, len(cols), 4):
                group = cols[i:i+4]
                if group:  # Add only non-empty groups
                    column_groups.append(group)
    
    # Process each group
    for i, columns in enumerate(column_groups):
        # Select color scheme
        color_scheme = color_schemes[i % len(color_schemes)]
        
        # Create title if not provided
        group_title = None
        if custom_titles and i in custom_titles:
            group_title = custom_titles[i]
        else:
            group_title = f"{title_prefix} {sheet_name} Analysis - Group {i+1}"
        
        # Create subtitle if provided
        group_subtitle = None
        if custom_subtitles and i in custom_subtitles:
            group_subtitle = custom_subtitles[i]
        
        # Get custom column titles if provided
        group_column_titles = None
        if custom_column_titles and i in custom_column_titles:
            group_column_titles = custom_column_titles[i]
        
        # Get value format specifications
        group_value_formats = None
        if value_formats and i in value_formats:
            group_value_formats = value_formats[i]
        
        # Get layout options if provided
        layout = None
        if layout_options and i < len(layout_options):
            layout = layout_options[i]
            
        # Prepare save path if output path is provided
        save_path = None
        if output_path:
            if output_path.lower().endswith(('.png', '.jpg', '.jpeg', '.pdf', '.svg')):
                # Split extension
                base, ext = output_path.rsplit('.', 1)
                save_path = f"{base}_group{i+1}.{ext}"
            else:
                save_path = f"{output_path}_group{i+1}.png"
        
        # Create the plot
        fig, axes = plot_bar_chart(
            df, 
            columns,
            title=group_title,
            subtitle=group_subtitle,
            column_titles=group_column_titles,
            color_scheme=color_scheme,
            bg_style=bg_style,
            xlabel=global_xlabel or df.index.name,
            ylabels=global_ylabel,
            value_format=group_value_formats,
            layout=layout,
            save_path=save_path,
            dpi=dpi,
            show_plot=show_plots,
            figsize=figsize
        )
        
        results.append((fig, axes))
    
    return results
