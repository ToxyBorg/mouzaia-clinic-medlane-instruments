import pandas as pd

excel_file_path = (
    "./public/Ensemble de la commande Mouzaia par boite avec code EAN13.xlsx"
)

# Load the Excel file
# Replace 'your_excel_file.xlsx' with your actual file path
df = pd.read_excel(excel_file_path)


# Function to add leading zeros to numeric values
def add_leading_zeros(ref_code):
    # Check if the value is a string first (to handle values like 'K1006')
    if not isinstance(ref_code, str):
        ref_code = str(ref_code)

    # If the code is all numeric and less than 5 digits, add leading zeros
    if ref_code.isdigit() and len(ref_code) < 5:
        return ref_code.zfill(5)  # zfill pads with zeros to reach the specified length
    else:
        return ref_code  # Return unchanged for non-numeric codes or those already 5+ digits


# Apply the function to the 'Réf' column
df["Réf"] = df["Réf"].apply(add_leading_zeros)

# Save the modified Excel file
df.to_excel(excel_file_path, index=False)

print(
    "Excel file has been modified. Numeric values in 'Réf' column with less than 5 digits now have leading zeros."
)
