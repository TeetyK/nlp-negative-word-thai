import pandas as pd
def preprocessing(path:str,type_word:int)->pd.DataFrame:
    df = pd.read_csv(path,sep='\n',names=['text'])
    df['labels'] = int
    return df