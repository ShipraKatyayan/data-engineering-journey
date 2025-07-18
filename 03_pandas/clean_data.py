import pandas as pd
import os

# Defining input & output paths

input_path = os.path.join("..", "data", "sample_dirty.csv")
output_path = os.path.join("..", "data", "sample_clean.csv")

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)

    # Drop rows with missing values
    df = df.dropna()

    # Rename columns
    df.columns = [col.strip().capitalize() for col in df.columns]

    # Save cleaned data
    df.to_csv(output_file, index= False)
    print(f"✅ Cleaned data saved to {output_file}")

if __name__ == "__main__":
     clean_data(input_path, output_path)
