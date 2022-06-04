
# create Pandas Data Frame
import pandas as pd
import datetime as dt
from functools import wraps

def log_step(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tic = dt.datetime.now()
        result = func(*args, **kwargs)
        time_taken = str(dt.datetime.now() - tic)
        print(f"{func.__name__}:\n shape={result.shape} took {time_taken}s\n")
        return result

    return wrapper

@log_step
def init_pipeline(df):
    return df.copy()

@log_step
def unfold_columns(df, env: bool =False):
    dict_cols = ["fields", "rights"] 
    for col in dict_cols:
        print(col)
        new_df = pd.DataFrame()
        new_df[col] = df[col].apply(lambda x: eval(x))
        add_cols_df = pd.json_normalize(new_df[col])
        df = pd.concat([df, add_cols_df], axis=1)
        df.drop(columns=col)
    # Tags extraction
    if env:
        df["tags"] = df["tags"].apply(lambda x: eval(x))

    df['tagWebTitle'] = df['tags'].map(lambda x:[i['webTitle'] for i in x])
    df['tagId'] = df['tags'].map(lambda x:[i['id'] for i in x])
    df = df.drop(columns="tags")
    return 


