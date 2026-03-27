import pandas as pd
def preprocessing(path:str,type_word:int)->pd.DataFrame:
    df = pd.read_csv(path,header=None,names=['text'])
    df['labels'] = type_word
    return df