import pandas as pd

# The array of codes we created earlier
eventration_sein_instruments = [
    "37609",
    "37609",
    "37609",
    "N060",
    "UN140",
    "35405",
    "UN130",
    "UC4312",
    "UC4314",
    "UC4306",
    "38305",
    "UC4309",
    "37705",
    "35103",
    "38903",
    "38903",
    "35403",
    "35101",
    "35101",
    "38902",
    "35405",
    "02602",
    "UC4313",
    "UN120",
    "35405",
    "34203",
    "34203",
    "38902",
    "35405",
    "38903",
    "35103",
    "35103",
    "26708",
    "35405",
    "35403",
    "35403",
    "02602",
    "01217",
    "02003",
    "30910",
    "30909",
    "29305",
    "28402",
    "28402",
    "28402",
    "28402",
    "28402",
    "00517",
    "17505",
    "17505",
    "14104",
    "14104",
    "14104",
    "14104",
    "01217",
    "47207",
    "17706",
    "W732",
    "17706",
    "21506",
    "32919",
    "17507",
    "17507",
    "K1007",
    "K1008",
]

# Load the Excel file
# Replace 'your_excel_file.xlsx' with your actual file path
df = pd.read_excel(
    "./public/Ensemble de la commande Mouzaia par boite avec code EAN13.xlsx"
)

instruments_saved = "./public/eventration_seins_instrument_results.xlsx"

# Create a new dataframe to store the matched results
results = []

# Check each code against the reference data
for code in eventration_sein_instruments:
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
total_count = len(eventration_sein_instruments)
print(
    f"Summary: Found {found_count} out of {total_count} instruments ({found_count/total_count*100:.1f}%)"
)
