import pandas as pd

# The array of codes we created earlier
hysteroscopie_KO_instruments = [
    "02004",
    "02602",
    "02602",
    "02728",
    "03510",
    "17505",
    "17505",
    "17706",
    "20304",
    "20304",
    "21601",
    "21602",
    "25514",
    "26712",
    "28402",
    "28402",
    "28402",
    "28402",
    "30933",
    "30935",
    "30938",
    "33601",
    "33603",
    "33603",
    "33603",
    "33605",
    "33705",
    "33705",
    "33801",
    "33801",
    "34207",
    "34502",
    "35103",
    "35103",
    "35103",
    "35103",
    "35405",
    "36008",
    "36008",
    "36008",
    "37606",
    "37607",
    "37607",
    "37705",
    "38903",
    "38903",
    "46402",
    "47203",
    "47209",
    "47210",
    "47213",
    "47213",
    "47505",
    "52929",
    "D2BB",
    "K1008",
    "K1301",
    "UC4308",
    "UC4309",
    "UC4314",
    "UN130",
    "UN140",
    "UN145",
]


# Load the Excel file
# Replace 'your_excel_file.xlsx' with your actual file path
df = pd.read_excel(
    "./public/Ensemble de la commande Mouzaia par boite avec code EAN13.xlsx"
)

instruments_saved = "./public/hysteroscopie_KO_instrument_results.xlsx"

# Create a new dataframe to store the matched results
results = []

# Check each code against the reference data
for code in hysteroscopie_KO_instruments:
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
total_count = len(hysteroscopie_KO_instruments)
print(
    f"Summary: Found {found_count} out of {total_count} instruments ({found_count/total_count*100:.1f}%)"
)
