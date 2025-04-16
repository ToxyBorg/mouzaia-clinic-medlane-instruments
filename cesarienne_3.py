import pandas as pd

# The array of codes we created earlier
cesarienne_instruments = [
    "02003",
    "02602",
    "17505",
    "17505",
    "21602",
    "28402",
    "28402",
    "28402",
    "28402",
    "28402",
    "30909",
    "30912",
    "33603",
    "33603",
    "34203",
    "35103",
    "35405",
    "35405",
    "35405",
    "37609",
    "37609",
    "37705",
    "38403",
    "38403",
    "45503",
    "47210",
    "K1008",
    "UC4314",
    "UC4314",
    "UN130",
    "UN140",
]


# Load the Excel file
# Replace 'your_excel_file.xlsx' with your actual file path
df = pd.read_excel(
    "./public/Ensemble de la commande Mouzaia par boite avec code EAN13.xlsx"
)

instruments_saved = "./public/cesarienne_3_instrument_results.xlsx"

# Create a new dataframe to store the matched results
results = []

# Check each code against the reference data
for code in cesarienne_instruments:
    matching_rows = df[df["Réf"] == code]

    if not matching_rows.empty:
        # Found the reference code
        libelle = matching_rows["Libellé"].values[0]
        results.append(
            {
                "Réf": code,
                "Libellé": libelle,
            }
        )
    else:
        # Reference code not found
        results.append(
            {
                "Réf": code,
                "Libellé": "N/A",
            }
        )

# Create a DataFrame from the results
results_df = pd.DataFrame(results)

# Save to Excel
results_df.to_excel(instruments_saved, index=False)

print("Results saved to ", instruments_saved)

# Print a summary
found_count = results_df[results_df["Libellé"] != "N/A"].shape[0]
total_count = len(cesarienne_instruments)
print(
    f"Summary: Found {found_count} out of {total_count} instruments ({found_count/total_count*100:.1f}%)"
)
