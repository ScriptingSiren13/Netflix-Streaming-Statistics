# analysis/insights.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_venn import venn2

# 1. Content type distribution
def content_type_distribution(df):
    df['type'].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=90,
        title='Content Type Distribution',
        colors=['#E50914','black'],
        textprops={'color':'white'}
    )
    plt.show()
    return df['type'].value_counts()


# 2. Netflix growth over the years
def netflix_growth(df):
    count_by_year = df['release_year'].value_counts().sort_index()
    count_by_year.plot(kind='bar', figsize=(20,5), color='#E50914', title='Netflix Over the Years')
    plt.show()
    
    df.groupby(['release_year', 'type'], observed=True).size().unstack().plot(
        kind='bar', stacked=True, figsize=(20,5), color=['#E50914','black']
    )
    plt.show()
    return count_by_year


# 3. Top content-producing countries
def top_countries(df, top_n=10):
    top = df['country'].value_counts().head(top_n)
    top.plot(kind='bar', figsize=(20,5), color='#E50914', title=f'Top {top_n} Content Producing Countries')
    plt.xticks(rotation=45)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
    return top


# 4. Most frequent directors
def top_directors(df, top_n=10):
    top = df['director'].value_counts().head(top_n)
    top.plot(kind='bar', figsize=(20,5), color='#E50914', title='Most Frequent Directors')
    plt.xticks(rotation=45)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
    return top


# 5. Most frequent actors
def top_actors(df, top_n=10):
    all_cast = df['cast'].dropna().str.split(', ')
    flat_cast = [actor.strip() for sublist in all_cast for actor in sublist]
    top = pd.Series(flat_cast).value_counts().head(top_n)
    top.plot(kind='bar', figsize=(20,5), color='#E50914', title='Most Frequent Actors')
    plt.xticks(rotation=45)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
    return top


# 6a. Movie duration distribution
def movie_duration_distribution(df):
    movies = df[df['type']=='Movie']
    plt.figure(figsize=(15,5))
    plt.hist(movies['duration_int'], bins=30, color='#E50914', edgecolor='black')
    plt.title('Distribution of Movie Durations')
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Number of Movies')
    plt.grid(True)
    plt.show()
    return movies['duration_int']


# 6b. Trend of kids' content
def kids_content_trend(df):
    kids_df = df[df['rating'].str.contains('TV-Y|TV-G|TV-PG', na=False)]
    kids_by_year = kids_df['release_year'].value_counts().sort_index()
    kids_by_year.plot(kind='line', color="#E50914", title="Trend of Kid's Content Over the Years")
    plt.show()
    return kids_by_year


# 7. Genre distribution by country
def genre_by_country(df, top_n_countries=10, top_n_genres=5):
    df_explode = df.dropna(subset=['country','listed_in']).copy()
    df_explode['country'] = df_explode['country'].str.split(', ')
    df_explode['listed_in'] = df_explode['listed_in'].str.split(', ')
    df_explode = df_explode.explode('country').explode('listed_in')
    
    genre_by_country = df_explode.groupby(['country','listed_in']).size().unstack().fillna(0)
    
    top_countries = df_explode['country'].value_counts().head(top_n_countries).index
    top_genres = df_explode['listed_in'].value_counts().head(top_n_genres).index
    
    filtered_df = genre_by_country.loc[top_countries, top_genres]
    
    # Heatmap
    plt.figure(figsize=(18,8))
    sns.heatmap(genre_by_country.loc[top_countries], cmap='Reds', linewidths=0.5, linecolor='gray')
    plt.title("Genre Distribution Across Top Content-Producing Countries")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    # Horizontal stacked bar
    filtered_df.plot(kind='barh', stacked=True, figsize=(14,8), colormap='tab10', edgecolor='black')
    plt.title("Top Genres in Top Countries")
    plt.xlabel("Number of Titles")
    plt.ylabel("Countries")
    plt.tight_layout()
    plt.grid(True, axis='x', linestyle='--', alpha=0.6)
    plt.show()
    
    return filtered_df


# 8. Monthly content addition trend
def content_addition_trend(df):
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['month_added'] = df['date_added'].dt.month
    monthly_counts = df['month_added'].value_counts().sort_index()
    
    plt.figure(figsize=(10,5))
    monthly_counts.plot(kind='bar', color='#E50914', edgecolor='black')
    plt.xticks(ticks=range(12), labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], rotation=45)
    plt.title("Monthly Trend of Netflix Content Additions")
    plt.ylabel("Number of Titles Added")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    
    return monthly_counts


# 9. Country-wise breakdown of Movies vs TV Shows
def country_type_breakdown(df, top_n=10):
    country_type = df.groupby(['country','type'], observed=True).size().unstack().fillna(0)
    country_type.sort_values('Movie', ascending=False).head(top_n).plot(kind='bar', stacked=True, figsize=(12,6), color=['#E50914','black'])
    plt.title("Top Countries by Content Type")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()
    return country_type



# 10. Genre overlap between Movies and TV Shows
def genre_overlap_venn(df):
    df_exploded = df.dropna(subset=['listed_in']).copy()
    df_exploded['listed_in'] = df_exploded['listed_in'].str.split(', ')
    df_exploded = df_exploded.explode('listed_in')
    
    movie_genres = set(df_exploded[df_exploded['type']=='Movie']['listed_in'])
    tv_genres = set(df_exploded[df_exploded['type']=='TV Show']['listed_in'])
    
    plt.figure(figsize=(8,6))
    venn2([movie_genres, tv_genres], set_labels=('Movies','TV Shows'), set_colors=('#E50914','black'), alpha=0.7)
    plt.title("Genre Overlap Between Movies and TV Shows on Netflix")
    plt.show()
    
    return movie_genres, tv_genres


# 11. TV show season distribution
def tv_seasons_distribution(df):
    tv_shows = df[df['type']=='TV Show'].copy()
    tv_shows['duration_int'] = pd.to_numeric(tv_shows['duration'].str.extract('(\d+)')[0])
    
    plt.figure(figsize=(12,6))
    plt.hist(tv_shows['duration_int'], bins=range(1, tv_shows['duration_int'].max()+2), color='#E50914', edgecolor='black', align='left')
    plt.title("Distribution of TV Show Seasons")
    plt.xlabel("Number of Seasons")
    plt.ylabel("Number of TV Shows")
    plt.xticks(range(1, tv_shows['duration_int'].max()+1))
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    
    return tv_shows['duration_int']


# 12. Content rating distribution
def rating_distribution(df):
    rating_counts = df['rating'].value_counts()
    plt.figure(figsize=(12,6))
    rating_counts.plot(kind='bar', color='#E50914', edgecolor='black')
    plt.title("Distribution of Content Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    
    return rating_counts


# 13. Top directors vs genres heatmap
def director_genre_heatmap(df, top_directors_series):
    df_genre = df[df['director'].isin(top_directors_series.index)].copy()
    df_genre['listed_in'] = df_genre['listed_in'].str.split(', ')
    df_genre = df_genre.explode('listed_in')
    
    director_genre = df_genre.groupby(['director','listed_in']).size().unstack().fillna(0)
    
    plt.figure(figsize=(15,7))
    sns.heatmap(director_genre, cmap='YlGnBu', linewidths=0.5)
    plt.title("Top Directors vs Genres")
    plt.xlabel("Genre")
    plt.ylabel("Director")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    return director_genre

# 14. Director genre diversity by country
def director_genre_diversity(df):
    df_genre_explode = df.copy()
    df_genre_explode = df_genre_explode[df_genre_explode['director'] != 'Unknown']
    df_genre_explode = df_genre_explode.dropna(subset=['country','listed_in'])
    df_genre_explode['country'] = df_genre_explode['country'].str.split(', ')
    df_genre_explode['listed_in'] = df_genre_explode['listed_in'].str.split(', ')
    df_genre_explode = df_genre_explode.explode('country').explode('listed_in')
    
    genre_diversity = df_genre_explode.groupby('director')['listed_in'].nunique().reset_index()
    genre_diversity.columns = ['director','unique_genre_count']
    
    director_country = df_genre_explode.groupby(['director','country']).size().reset_index(name='count')
    top_country = director_country.sort_values('count', ascending=False).drop_duplicates('director')
    genre_diversity = genre_diversity.merge(top_country[['director','country']], on='director')
    
    top_countries = genre_diversity['country'].value_counts().head(15).index
    filtered_data = genre_diversity[genre_diversity['country'].isin(top_countries)]
    
    plt.figure(figsize=(14,6))
    sns.boxplot(data=filtered_data, x='country', y='unique_genre_count', color='#E50914', showmeans=True,
                meanprops={"marker":"o","markerfacecolor":"white","markeredgecolor":"black"})
    plt.title("Genre Diversity of Directors by Top 15 Countries")
    plt.xlabel("Country")
    plt.ylabel("Number of Unique Genres Directed")
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    
    return filtered_data


# 15. Metadata completeness by release year
def metadata_completeness_by_year(df):
    metadata_cols = ['director','cast','country','rating','date_added','duration']
    df['metadata_complete_count'] = df[metadata_cols].notnull().sum(axis=1)
    df['total_metadata_fields'] = len(metadata_cols)
    df['metadata_completeness'] = df['metadata_complete_count']/df['total_metadata_fields']
    
    completeness_by_year = df.groupby('release_year')['metadata_completeness'].mean()
    plt.figure(figsize=(14,5))
    completeness_by_year.plot(kind='line', color='#E50914', marker='o')
    plt.title("Average Metadata Completeness by Release Year")
    plt.xlabel("Release Year")
    plt.ylabel("Avg. Metadata Completeness (0 to 1)")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    
    return completeness_by_year
   
