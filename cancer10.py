# importing libraries
import pandas as pd
# importing the csv
url = "https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv"
csv_list = pd.read_csv(url)
# head() command + output
x = csv_list.head(10)
print(x)