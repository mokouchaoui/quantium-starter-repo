import pandas as pd
import os

# Define the data folder
data_folder = "data"

# List all CSV files in the data folder
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

# Initialize an empty list to store DataFrames
data_frames = []

# Process each CSV file
for file in csv_files:
    file_path = os.path.join(data_folder, file)
    
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Filter for "Pink Morsels" only
    df = df[df["product"] == "Pink Morsels"]
    
    # Create the 'sales' column
    df["sales"] = df["quantity"] * df["price"]
    
    # Select required columns
    df = df[["sales", "date", "region"]]
    
    # Append the processed DataFrame to the list
    data_frames.append(df)

# Combine all DataFrames
final_df = pd.concat(data_frames, ignore_index=True)

# Save to a new CSV file
output_file = os.path.join(data_folder, "formatted_sales_data.csv")
final_df.to_csv(output_file, index=False)

print(f"Processed data saved to {output_file}")
