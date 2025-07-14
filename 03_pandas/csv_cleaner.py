import pandas as pd
import os

#defining file paths

input_path = os.path.join("..", "data", "sample_dirty.csv")
output_path = os.path.join("..", "data", "sample_clean.csv")

def clean_csv(input_file, output_file):
     df = pd.read_csv(input_file)

     #dropping duplicates
     df_unduplicated = df.drop_duplicates()


     #dropping rows with missing values
     df_clean = df_unduplicated.dropna()


     #saving the cleaned data
     df_clean.to_csv(output_file, index=False)
     print(f"✅ cleaned file saved to {output_file}")

if __name__ == "__main__":
    clean_csv(input_path, output_path)