# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/sincostheta/ICSEPy/refs/heads/main/best-selling-books%20export%202026-05-29%2006-17-11.csv"
df = pd.read_csv(url)
# indexing csv
df.rename(columns={"First published": "Year", "Approximate sales in millions": "Sales"}, inplace=True)
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df.dropna(subset=["Year", "Sales"], inplace=True)
books_per_year = df.groupby("Year").size()
# plotting
plt.figure(figsize=(16, 5))
plt.bar(books_per_year.index, books_per_year.values)
plt.title("Number of Bestselling Books Published per Year")
plt.xlabel("Year")
plt.ylabel("Number of Books")
plt.xticks(rotation=90, fontsize=7)
plt.tight_layout()
plt.show()
NON_FICTION_KEYWORDS = ["non-fiction", "self-help", "autobiography", "memoir", "biography","manual", "guide", "science", "history", "essay", "philosophy","psychology", "anthropology", "travel", "sexology", "pregnancy","motivational", "business", "leadership", "christian literature","popular science", "spiritual", "new-age"]
# logic
def classify_genre(genre_str):
    if str(genre_str).strip() in ("", "nan"): 
        return "Unknown"
    g = genre_str.lower()
    for kw in NON_FICTION_KEYWORDS:
        if kw in g:
            return "Non-Fiction"
    return "Fiction"

df["Category"] = df["Genre"].apply(classify_genre)
category_counts = df["Category"].value_counts()
print("category countss:")
print(category_counts)
most_frequent = category_counts.idxmax()
print(f"most frequent genre: {most_frequent} ({category_counts[most_frequent]} books)")