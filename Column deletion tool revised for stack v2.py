
import pandas as pd 

f = open("D:\Latest  programs &  data  that work -in IDLE-/full  NYSE list  7-28-19.csv", "r")

for symbol in f.readlines():

    symbol = symbol.strip()

    url_part1 = symbol
    url_part2 = ".csv"
    url = url_part1 + url_part2 
    print(url)
    df = pd.read_csv(url, index_col = 'Close')
    df.drop(["Volume", "Date", "Open", "High", "Low"], axis = 1, inplace = True)
    df.rename(columns = {'Close': symbol}, inplace = True)
    df.head()
    url_part0 = "edited"
    final_url = url_part0 + url
    df.to_csv(r'D:\Latest  programs &  data  that work -in IDLE-/final_url')
