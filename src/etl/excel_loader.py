import pandas as pd


def load_excel(file_path):
    """
    Load excel file with header=1
    """
    df = pd.read_excel(file_path, header=1)

    print("Rows:", len(df))
    print("Columns:", df.columns.tolist())

    return df


if __name__ == "__main__":
    df = load_excel("data/raw/companies.xlsx")

    print(df.head())