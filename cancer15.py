# importing libraries, reading csv
import matplotlib.pyplot as plt
import pandas as pd
url = "https://raw.githubusercontent.com/sincostheta/ICSEPy/refs/heads/main/top_200_youtubers.csv"
df = pd.read_csv(url)
# csv indexing
df.rename(columns={"Main Video Category": "Genre",}, inplace=True)
df["Likes"] = pd.to_numeric(df["Likes"], errors="coerce")
df["followers"] = pd.to_numeric(df["followers"], errors="coerce")
df.dropna(subset=["Genre", "Likes", "followers"], inplace=True) 
# plot 1
plt.figure(figsize=(14, 5))
plt.title("Visualisation of the most Liked genre")
plt.scatter(df["Genre"], df["Likes"])
plt.xlabel("Genre")
plt.ylabel("Likes")
plt.xticks(rotation=45, ha="right", fontsize=8)
plt.tight_layout()
plt.show()
# identifying the most liked genre
most_liked = df.groupby("Genre")["Likes"].sum().idxmax()
print(f"Most liked genre: {most_liked}")
# plot 2
plt.figure(figsize=(14, 5))
plt.title("Visualisation of the most Followed genre")
plt.scatter(df["Genre"], df["followers"])
plt.xlabel("Genre")
plt.ylabel("Followers")
plt.xticks(rotation=45, ha="right", fontsize=8)
plt.tight_layout()
plt.show()