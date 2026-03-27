import pandas as pd
from src.preprocessing import preprocessing


if __name__ == "__main__":
    df1 = preprocessing(".\\datasets\\positive-sentiment-words.txt",0)
    df2 = preprocessing(".\\datasets\\negative-sentiment-words.txt",1)
    df3 = preprocessing(".\\datasets\\swear-words.txt",1)
    print(df1)
    print(df2)
    print(df3)
