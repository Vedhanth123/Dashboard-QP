"""
HDFC Dashboard Generator Script
-------------------------------
Command-line script for generating visualizations from HDFC Excel data

Usage:
    python generate_dashboard.py [options]

Options:
    --file FILE             Excel file path (default: HDFC_modified.xlsx)
    --sheet SHEET           Excel sheet name (default: all sheets)
    --output DIR            Output directory for images (default: ./exports)
    --dpi DPI              Image resolution (default: 300)
    --title TITLE           Custom dashboard title
    --style STYLE           Background style (default: presentation)
    --colors SCHEME         Color scheme (default: hdfc_brand)
"""

import argparse
import os
import pandas as pd
from hdfc_viz import create_dashboard, COLOR_SCHEMES, BG_STYLES

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate HDFC data visualizations')
    parser.add_argument('--file', default='HDFC_modified.xlsx', help='Excel file path')
    parser.add_argument('--sheet', default=None, help='Excel sheet name (default: all sheets)')
    parser.add_argument('--output', default='./exports', help='Output directory')
    parser.add_argument('--dpi', type=int, default=300, help='Image resolution')
    parser.add_argument('--title', default=None, help='Custom dashboard title')
    parser.add_argument('--style', default='presentation', choices=list(BG_STYLES.keys()),
                        help='Background style')
    parser.add_argument('--colors', default='hdfc_brand', choices=list(COLOR_SCHEMES.keys()),
                        help='Color scheme')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)
    
    # Load Excel file
    excel_file = pd.ExcelFile(args.file)
    
    # Get list of sheets to process
    sheets = [args.sheet] if args.sheet else excel_file.sheet_names
    
    # Process each sheet
    for sheet in sheets:
        print(f"Processing sheet: {sheet}")
        
        try:
            # Load the data
            df = pd.read_excel(args.file, index_col="Category", sheet_name=sheet)
            
            # Define column groups - adjust based on number of columns
            n_cols = len(df.columns)
            column_groups = []
            
            # Group columns into 4-column groups
            for i in range(0, n_cols, 4):
                group = df.columns[i:i+4].tolist()
                if group:  # Add only non-empty groups
                    column_groups.append(group)
            
            # Custom title based on sheet name if not provided
            title_prefix = args.title if args.title else "HDFC"
            
            # Create dashboard
            output_path = os.path.join(args.output, f"HDFC_{sheet}")
            dashboard = create_dashboard(
                df=df,
                sheet_name=sheet,
                column_groups=column_groups,
                output_path=output_path,
                title_prefix=title_prefix,
                color_schemes=[args.colors],
                bg_style=args.style,
                show_plots=False,  # Don't show plots, just save them
                dpi=args.dpi
            )
            
            print(f"  - Generated {len(dashboard)} chart groups for {sheet}")
            
        except Exception as e:
            print(f"Error processing sheet {sheet}: {e}")
    
    print(f"All dashboards exported to {args.output}")

if __name__ == "__main__":
    main()
