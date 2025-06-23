
import pandas as pd

def duplicate_csv_data(file_path):

    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)

        # Concatenate the DataFrame with itself to duplicate the data
        df_duplicated = pd.concat([df, df], ignore_index=True)

        # Create a new file name for the duplicated data
        new_file_name = file_path.replace(".csv", "_duplicated.csv")  # or any other name

        # Save the duplicated data to a new CSV file
        df_duplicated.to_csv(new_file_name, index=False)

        print(f"Duplicated data saved to {new_file_name}")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage (replace 'diabetes (1).csv' with your actual file path)
duplicate_csv_data('clonedata/dataset.csv')