import pandas as pd

# The array of codes we created earlier
accouchement_instruments = [
    "30912",
    "37605",
    "35407",
    "35407",
    "35409",
    "36006",
    "47209",
    "UC4314",
    "UC4333",
    "UN140",
]

# Load the Excel file
# Replace 'your_excel_file.xlsx' with your actual file path
df = pd.read_excel(
    "./public/Ensemble de la commande Mouzaia par boite avec code EAN13.xlsx"
)

instruments_saved = "./public/accouchement_9_instrument_results.xlsx"

# Create a new dataframe to store the matched results
results = []

# Check each code against the reference data
for code in accouchement_instruments:
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
total_count = len(accouchement_instruments)
print(
    f"Summary: Found {found_count} out of {total_count} instruments ({found_count/total_count*100:.1f}%)"
)
