
import pandas as pd 

f = open("D:\Latest  programs &  data  that work -in IDLE-/1st 495 symbols.csv", "r")
df_new = pd.read_csv('D:\Latest  programs &  data  that work -in IDLE-/1st A 495 column merge.csv')


for symbol in f.readlines():

    symbol = symbol.strip()

    url_part1 = symbol
    url_part2 = ".csv"
    url = url_part1 + url_part2 

    df_old = pd.read_csv(url)
    old = df_old
    
    df_old.drop(["volume", "timestamp", "open", "high", "low"], axis = 1, inplace = True)
    #print(df_old.head(3))
    
    #df_old.set_index('close')

    
    #df_old.rename(columns={'close':(symbol)}, inplace=True)
    #print(df_old.head(3))

    df_new = df_old.filter(['close'], axis=1)#.copy()
   # df_new.set_index('timestamp')
    print(df_new.head(3))
    #df_old.to_csv(r'D:\Latest  programs &  data  that work -in IDLE-\revised colum csvs\'(url))
    df_new.rename(columns={'close':(symbol)}, inplace=True)
    
    
    
    #df_new[(symbol)] = df_old[(symbol)]
    #print(df_new.head(3))        

