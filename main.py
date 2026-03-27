import pandas as pd
from src.preprocessing import preprocessing
from src.train import train
from src.load import load

if __name__ == "__main__":
    df1 = preprocessing(".\\datasets\\positive-sentiment-words.txt",0)
    df2 = preprocessing(".\\datasets\\negative-sentiment-words.txt",1)
    df3 = preprocessing(".\\datasets\\swear-words.txt",1)
    final = pd.concat([df1,df2])
    final = pd.concat([final,df3])
    train(final)
    load()