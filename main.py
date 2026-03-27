import pandas as pd
from src.preprocessing import preprocessing


if __name__ == "__main__":
    df1 = preprocessing(".\\datasets\\positive-sentiments-words",0)
    print(df1)
