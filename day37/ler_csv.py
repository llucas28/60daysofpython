import pandas as pd

def main():
    nome_arquivo = "test.csv"

    df = pd.read_csv(r"C:\Users\Lucas\60daysofpython\day37\test.csv")

    print(df)

    print(df.head())

    print(df.info())

if __name__ == "__main__":
    main()
