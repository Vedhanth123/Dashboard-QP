import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from math import ceil

def create_grouped_barplots(df, column_groups, category_col='Category', 
                           figsize_per_subplot=(12, 8), title_fontsize=18, 
                           axis_label_fontsize=14, tick_label_fontsize=12, 
                           rotation=45, color_palette='Set2'):
    """
    Create bar plots with custom column groupings
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The input dataframe
    column_groups : list of lists
        Each inner list contains column names to be plotted together
        Example: [['col1', 'col2'], ['col3', 'col4', 'col5']]
    category_col : str
        The column name to use as x-axis categories
    figsize_per_subplot : tuple
        Size of each subplot (width, height)
    Other parameters: formatting options
    """
    
    n_subplots = len(column_groups)
    
    # Create figure with subplots arranged vertically for better readability
    fig, axes = plt.subplots(n_subplots, 1, figsize=(figsize_per_subplot[0], 
                                                     figsize_per_subplot[1] * n_subplots))
    
    # Handle case where there's only one subplot
    if n_subplots == 1:
        axes = [axes]
    
    # Process each group
    for i, group_cols in enumerate(column_groups):
        ax = axes[i]
        
        # Filter valid columns that exist in dataframe
        valid_cols = [col for col in group_cols if col in df.columns]
        
        if not valid_cols:
            ax.set_visible(False)
            continue
        
        # Prepare data for grouped bar plot
        x_positions = np.arange(len(df[category_col]))
        bar_width = 0.8 / len(valid_cols)  # Adjust width based on number of bars
        
        colors = sns.color_palette(color_palette, len(valid_cols))
        
        # Create bars for each column in the group
        for j, col in enumerate(valid_cols):
            offset = (j - len(valid_cols)/2 + 0.5) * bar_width
            bars = ax.bar(x_positions + offset, df[col], bar_width, 
                         label=col.replace('_', ' ').title(), color=colors[j], alpha=0.8)
            
            # Add value labels on bars (optional - comment out if too cluttered)
            for bar in bars:
                height = bar.get_height()
                if not pd.isna(height):
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{height:.2f}' if abs(height) < 1000 else f'{height:.0f}',
                           ha='center', va='bottom', fontsize=tick_label_fontsize-2,
                           rotation=0)
        
        # Format the subplot
        group_title = f"Group {i+1}: " + " | ".join([col.replace('_', ' ').title() for col in valid_cols[:2]])
        if len(valid_cols) > 2:
            group_title += f"\n+ {len(valid_cols)-2} more columns"
        
        ax.set_title(group_title, fontsize=title_fontsize, fontweight='bold', pad=20)
        ax.set_xlabel(category_col.replace('_', ' ').title(), fontsize=axis_label_fontsize, fontweight='bold')
        ax.set_ylabel('Values', fontsize=axis_label_fontsize, fontweight='bold')
        
        # Set x-axis labels
        ax.set_xticks(x_positions)
        ax.set_xticklabels(df[category_col], rotation=rotation, fontsize=tick_label_fontsize)
        ax.tick_params(axis='y', labelsize=tick_label_fontsize)
        
        # Add legend and grid
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=tick_label_fontsize)
        ax.grid(axis='y', alpha=0.3)
        ax.set_axisbelow(True)
    
    plt.tight_layout()
    plt.show()
    
    return fig, axes

def create_predefined_groups_plot(df, category_col='Category', **kwargs):
    """
    Create plots with your specific grouping requirements:
    - First 2 numeric columns: 1 subplot
    - Next 4 columns: another subplot  
    - Next 4 columns: another subplot
    - Next 2 columns: another subplot
    - Remaining columns: another subplot
    """
    
    # Get numeric columns (excluding category column)
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if category_col in numeric_cols:
        numeric_cols.remove(category_col)
    
    # Define the groups based on your requirements
    column_groups = []
    
    # Group 1: First 2 columns
    if len(numeric_cols) >= 2:
        column_groups.append(numeric_cols[0:2])
    elif len(numeric_cols) > 0:
        column_groups.append(numeric_cols[0:1])
    
    # Group 2: Next 4 columns (columns 2-5)
    if len(numeric_cols) >= 6:
        column_groups.append(numeric_cols[2:6])
    elif len(numeric_cols) > 2:
        column_groups.append(numeric_cols[2:min(6, len(numeric_cols))])
    
    # Group 3: Next 4 columns (columns 6-9)
    if len(numeric_cols) >= 10:
        column_groups.append(numeric_cols[6:10])
    elif len(numeric_cols) > 6:
        column_groups.append(numeric_cols[6:min(10, len(numeric_cols))])
    
    # Group 4: Next 2 columns (columns 10-11)
    if len(numeric_cols) >= 12:
        column_groups.append(numeric_cols[10:12])
    elif len(numeric_cols) > 10:
        column_groups.append(numeric_cols[10:min(12, len(numeric_cols))])
    
    # Group 5: Remaining columns (columns 12+)
    if len(numeric_cols) > 12:
        column_groups.append(numeric_cols[12:])
    
    # Remove empty groups
    column_groups = [group for group in column_groups if group]
    
    print("Column Groups:")
    for i, group in enumerate(column_groups):
        print(f"Group {i+1}: {group}")
    
    return create_grouped_barplots(df, column_groups, category_col, **kwargs)

# Load sample data (replace with your actual dataframe)
def load_sample_data():
    """Create sample data based on your provided dataframe structure"""
    data = {
        'Category': ['Active', 'Inactive'],
        'CAP_LRM_cohort': [2866, 4169],
        'CAP_12_cohort': [1068, 502],
        'Average_Cumulative_Combined_KPI': [0.696836, 0.141789],
        'CAP_on_COMBINED_KPI_of_Top_10%': [1.866591, 1.837040],
        'CAP_on_COMBINED_KPI_of_Bottom_10%': [0.128534, 0.108028],
        'Performance_multiple_of_the_CAP_12': [14.522180, 17.005259],
        'Average_Cumulative_KPI_1': [0.803662, 0.158137],
        'CAP_on_KPI_1_of_Top_10%': [2.828391, 3.143468],
        'CAP_on_KPI_1_of_Bottom_10%': [0.097645, 0.078580],
        'Performance_multiple_ON_KPI_1_of_the_CAP_12': [28.966008, 40.003515],
        'Time_to_make_the_first_CAP': [6.820934, 7.855946],
        'CAR2CATPO_ratio_UP_TO_Residency': [2.484035, 1.204261],
        'Count_of_attrited_employees_in_Cohort_LRM': [float('nan'), 4169.0],
        'Average_Residency_of_TOP_10%_employees_in_COHORT_LRM': [9.589323, 6.308227],
        'Average_Residency_of_all_employees_in_KPI_1_in_COHORT_LRM': [9.752809, 9.727273],
        'Infant_attrition_in_the_first_6_residency_months_as_a_%_of_all_people': [float('nan'), 0.646678],
        'Infant_attrition_-_attrited_employees_in_the_first_23_months_in_the_sub_cohort': [float('nan'), 0.646678]
    }
    return pd.DataFrame(data)

# Example usage
if __name__ == "__main__":
    # Load your dataframe (replace with your actual dataframe loading)
    
    df = pd.read_excel('HDFC_modified.xlsx', index_col="Category",sheet_name="WorkStatus")
    
    # First, let's check what columns you actually have
    print("Available columns in your dataframe:")
    print(df.columns.tolist())
    print(f"\nDataframe shape: {df.shape}")
    print(f"\nIndex name: {df.index.name}")
    print(f"Index values: {df.index.tolist()}")
    print("\nFirst few rows:")
    print(df.head())
    
    # Check if index contains categories (like Active/Inactive)
    if df.index.name is not None or len(df.index.unique()) > 1:
        # Reset index to make it a column
        df = df.reset_index()
        category_col = df.columns[0]  # First column after reset_index
        print(f"\nUsing index as category column: '{category_col}'")
    else:
        # Find the category column (usually the first non-numeric column)
        category_col = None
        for col in df.columns:
            if df[col].dtype == 'object' or df[col].dtype.name == 'category':
                category_col = col
                break
        
        if category_col is None:
            print("No categorical column found. Creating a simple index.")
            df['Row'] = range(len(df))
            category_col = 'Row'
    
    print(f"\nUsing '{category_col}' as category column")
    print(f"Categories: {df[category_col].unique()}")
    
    # Method 1: Use predefined grouping (your specific requirements)
    print("\n=== Using Predefined Groups ===")
    try:
        fig1, axes1 = create_predefined_groups_plot(
            df, 
            category_col=category_col,  # Use the detected category column
            figsize_per_subplot=(16, 8),
            title_fontsize=14,
            rotation=0  # No rotation needed for Active/Inactive
        )
    except Exception as e:
        print(f"Error creating plots: {e}")
        print("Please check your dataframe structure and column names")
    
    # Method 2: Complete Custom grouping with all your columns
    print("\n=== Complete Custom Grouping ===")
    custom_groups = [
        # Group 1: First 2 columns (Cohort data)
        ['CAP_LRM_cohort', 'CAP_12_cohort'],
        
        # Group 2: Next 4 columns (Combined KPI metrics)
        ['Average_Cumulative_Combined_KPI', 'CAP_on_COMBINED_KPI_of_Top_10%', 
         'CAP_on_COMBINED_KPI_of_Bottom_10%', 'Performance_multiple_of_the_CAP_12'],
        
        # Group 3: Next 4 columns (KPI 1 specific metrics)
        ['Average_Cumulative_KPI_1', 'CAP_on_KPI_1_of_Top_10%', 
         'CAP_on_KPI_1_of_Bottom_10%', 'Performance_multiple_ON_KPI_1_of_the_CAP_12'],
        
        # Group 4: Next 2 columns (Time and ratio metrics)
        ['Time_to_make_the_first_CAP', 'CAR2CATPO_ratio_UP_TO_Residency'],
        
        # Group 5: Remaining columns (Attrition and residency metrics)
        ['Count_of_attrited_employees_in_Cohort_LRM', 
         'Average_Residency_of_TOP_10%_employees_in_COHORT_LRM',
         'Average_Residency_of_all_employees_in_KPI_1_in_COHORT_LRM',
         'Infant_attrition_in_the_first_6_residency_months_as_a_%_of_all_people',
         'Infant_attrition_-_attrited_employees_in_the_first_23_months_in_the_sub_cohort']
    ]
    
    # Use the complete custom groups:
    fig2, axes2 = create_grouped_barplots(
        df, 
        custom_groups,
        category_col='Category',
        figsize_per_subplot=(16, 7),
        title_fontsize=16,
        rotation=0
    )