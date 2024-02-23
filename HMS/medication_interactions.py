import pandas as pd
import os

def check_medication_interaction(med_list_a, med_list_b):
    csv_file_path = 'C:/Users/rudra/Documents/BOLT 2.0/Telehealth/drugInteractions.csv'

    # Check if the file exists
    if os.path.exists(csv_file_path):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)

        # Filter the DataFrame based on drugA and drugB
        filter_a = df['drugA'].isin(med_list_a)
        filter_b = df['drugB'].isin(med_list_b)
        interaction_df = df[filter_a & filter_b]

        if not interaction_df.empty:
            # Assuming there's only one row for the interaction
            mechanism = interaction_df['mechanism'].iloc[0]
            return mechanism
        else:
            return "No interaction found"
    else:
        return f"Data file 'drugInteractions.csv' not found at {csv_file_path}"
