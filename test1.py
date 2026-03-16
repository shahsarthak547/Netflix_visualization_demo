import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("netflix_titles.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
#handled missing values
df['country'].fillna("Unknown", inplace=True)
df['director'].fillna("Unknown", inplace=True)
df['cast'].fillna("Unknown", inplace=True)
print(df.head())
print(df.isnull().sum())
#Movies v/s Tv Shows Distribution on netflix
df['type'].value_counts()
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.savefig('movies_vs_shows.jpg')
plt.show() #Shows that netflix contains more movies 
#Content Released per year
release_year = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,5))
sns.lineplot(x=release_year.index, y=release_year.values, marker="o")
plt.title("Content released per year")
plt.xlabel("Year")
plt.ylabel("Number of shows")
plt.savefig('release_per_year.jpg')
plt.show() # Shows that content released per year increased after 2015
#Shows Top 10 Countries Producing Content
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(
    x=top_countries.index,
    y=top_countries.values
)
plt.title("Top 10 Content Producing Countries")
plt.xticks(rotation=45)
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.savefig('top_10_content.jpg')
plt.show() #USA Leads the World
#Years In Which Most Content was added 
dates = df['date_added'].value_counts().head(10)
plt.figure(figsize=(10,5))
dates.plot(kind='pie')
plt.title("Years Most Content Was Added")
plt.savefig('yearly_content.jpg')
plt.show()
# #Average Time Duration of any Shows Or Movies on Netflix
avg_duration = df['duration'].value_counts().mean()
print(avg_duration)
#Top 10 trending genres on Netflix
genres = df['listed_in'].str.split(" ", expand=True).stack()
top_genres = genres.value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_genres.index, y=top_genres.values)
plt.title("Top Genres on Netflix")
plt.xlabel("Genres")
plt.ylabel("Number of Genres")
plt.savefig('genres.jpg')
plt.show()