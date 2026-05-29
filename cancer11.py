import pandas as pd
url = "https://raw.githubusercontent.com/sincostheta/ICSEPy/refs/heads/main/balaji.json"
df = pd.read_json(url)
df.info(verbose=True)
print(df.tail(7))
print("Total number of entries are: ", len(df))
x = df['Daily_Screen_Time'].mean()
print("Average screen time: ", x)
print(df)