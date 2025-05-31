"""
HDFC Example Visualizations Generator
------------------------------------
This script generates example visualizations for all sheets in the HDFC_modified.xlsx file,
demonstrating different visual styles, color schemes, and customization options.

Usage:
    python generate_examples.py
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from hdfc_viz import plot_bar_chart, create_dashboard, COLOR_SCHEMES

# Ensure output directory exists
os.makedirs("exports/examples", exist_ok=True)

# Load the Excel file
excel_file = "HDFC_modified.xlsx"
excel = pd.ExcelFile(excel_file)

# Get all sheet names
sheet_names = excel.sheet_names

print(f"Generating example visualizations for {len(sheet_names)} sheets...")

# Examples of different visualization styles
def generate_examples():
    """Generate example visualizations for all sheets"""
    for i, sheet in enumerate(sheet_names):
        print(f"Processing sheet {i+1}/{len(sheet_names)}: {sheet}")
        
        # Load the sheet data
        df = pd.read_excel(excel_file, sheet_name=sheet, index_col="Category")
        
        # 1. Basic example - Default settings
        columns = df.columns[:min(4, len(df.columns))]
        fig, axes = plot_bar_chart(
            df=df,
            columns=columns,
            title=f"HDFC {sheet} - Basic Example",
            subtitle="Default settings with corporate color scheme",
            color_scheme='corporate',
            save_path=f"exports/examples/{sheet}_basic.png",
            show_plot=False
        )
        
        # 2. Professional style - HDFC brand colors
        columns = df.columns[min(4, len(df.columns)):min(8, len(df.columns))] if len(df.columns) > 4 else df.columns[:min(4, len(df.columns))]
        if len(columns) > 0:
            fig, axes = plot_bar_chart(
                df=df,
                columns=columns,
                title=f"HDFC {sheet} - Professional Style",
                subtitle="HDFC brand colors with enhanced presentation style",
                color_scheme='hdfc_brand',
                bg_style='presentation',
                bar_edge_color='white',
                bar_edge_width=0.5,
                save_path=f"exports/examples/{sheet}_professional.png",
                show_plot=False
            )
        
        # 3. Gradient style with custom layout
        columns = df.columns[:min(6, len(df.columns))]
        if len(columns) > 0:
            fig, axes = plot_bar_chart(
                df=df,
                columns=columns,
                title=f"HDFC {sheet} - Gradient Style",
                subtitle="Blue gradient with 2x3 grid layout",
                color_scheme='gradient_blue',
                bg_style='minimal',
                layout=(2, 3),
                save_path=f"exports/examples/{sheet}_gradient.png",
                show_plot=False
            )
        
        # 4. Complete dashboard for the sheet
        column_groups = []
        for j in range(0, len(df.columns), 4):
            cols = df.columns[j:j+4].tolist()
            if cols:
                column_groups.append(cols)
        
        # Define custom titles for each group
        custom_titles = {}
        for j in range(len(column_groups)):
            custom_titles[j] = f"HDFC {sheet} - Group {j+1}"
        
        # Create a dashboard with all column groups
        dashboard = create_dashboard(
            df=df,
            sheet_name=sheet,
            column_groups=column_groups,
            output_path=f"exports/examples/{sheet}_dashboard",
            title_prefix="HDFC",
            color_schemes=list(COLOR_SCHEMES.keys()),
            bg_style='presentation',
            custom_titles=custom_titles,
            show_plots=False,
            dpi=300
        )
        
        print(f"  - Created {3 + len(dashboard)} visualizations for {sheet}")
    
    print(f"All example visualizations generated in exports/examples/")

if __name__ == "__main__":
    generate_examples()
