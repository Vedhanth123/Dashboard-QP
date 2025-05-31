import pandas as pd
import os
import shutil

# Create a backup of the original file
original_file = 'HDFC.xlsx'
backup_file = 'HDFC_backup.xlsx'

# Create backup if it doesn't exist
if not os.path.exists(backup_file):
    print(f"Creating backup of {original_file} as {backup_file}")
    shutil.copy2(original_file, backup_file)
    print("Backup created successfully")

# Read the Excel file
excel_file = pd.ExcelFile(original_file)
sheet_names = excel_file.sheet_names

print(f"Found {len(sheet_names)} sheets: {', '.join(sheet_names)}")

# Create a writer to save the modified sheets
with pd.ExcelWriter('HDFC_modified.xlsx') as writer:
    
    # Process each sheet
    for sheet_name in sheet_names:
        print(f"\nProcessing sheet: {sheet_name}")
        
        # Read the sheet with "Category" as index if it exists
        try:
            df = pd.read_excel(original_file, sheet_name=sheet_name, index_col="Category")
            has_category_index = True
        except:
            df = pd.read_excel(original_file, sheet_name=sheet_name)
            has_category_index = False
        
        print(f"Original shape: {df.shape}")
        
        # Remove "Sub total" row if it exists
        if has_category_index and "Sub total" in df.index:
            df = df.drop("Sub total")
            print(f"Removed 'Sub total' row from sheet '{sheet_name}'")
        elif not has_category_index and "Sub total" in df.values:
            # Find column that might contain "Sub total"
            for col in df.columns:
                mask = df[col] == "Sub total"
                if mask.any():
                    df = df[~mask]
                    print(f"Removed 'Sub total' row from sheet '{sheet_name}' in column '{col}'")
        
        print(f"New shape: {df.shape}")
        
        # Save to the new file
        df.to_excel(writer, sheet_name=sheet_name, index=has_category_index)

print("\nFinished processing all sheets.")
print("Modified file saved as 'HDFC_modified.xlsx'")
print("You can now review the changes and rename HDFC_modified.xlsx to HDFC.xlsx if satisfied.")
