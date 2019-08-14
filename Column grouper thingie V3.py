
import pandas as pd 

f = open("D:\Latest  programs &  data  that work -in IDLE-/1st 495 symbols.csv", "r")

'''
df_old = pd.read_csv("A.csv")
print(df_old.head())
df_old.drop(["volume", "timestamp", "open", "high", "low"], axis = 1, inplace = True)
print(df_old.head())

'''
for symbol in f.readlines():

    symbol = symbol.strip()

    url_part1 = symbol
    url_part2 = ".csv"
    url = url_part1 + url_part2 

    df_old = pd.read_csv(url)
    print(df_old.head())
    df_old.drop(["volume", "timestamp", "open", "high", "low"], axis = 1, inplace = True)
    print(df_old.head())
    
    df_old.set_index('close')
    #df_old.rename(columns={'close':(symbol)}, inplace=True)
    print(df_old.head())
    
    #df_old.to_csv(r'D:\Latest  programs &  data  that work -in IDLE-\revised colum csvs\(url)')
    

