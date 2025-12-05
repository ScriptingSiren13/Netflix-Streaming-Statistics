
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud


# 1. Violin Plot - Movie duration per rating
def plot_violin(movies):
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=movies,
                   x='rating', 
                   y='duration_int', 
                   color="#E50914")
    plt.title('Movie Duration Distribution by Rating')
    plt.xticks(rotation=45)
    plt.show()



# 2. Scatterplot - Release year vs duration
def plot_scatter(movies):
    plt.figure(figsize=(10, 6))
    plt.scatter(movies['release_year'], 
                movies['duration_int'], 
                alpha=0.5, 
                color="#E50914")
    plt.title('Release Year vs Movie Duration')
    plt.xlabel('Release Year')
    plt.ylabel('Duration (minutes)')
    plt.grid(True)
    plt.show()



# 3. Heatmap - Type vs Rating vs Count
def plot_type_rating_heatmap(df):
    heat_df = pd.crosstab(df['type'], df['rating'])
    plt.figure(figsize=(20, 5))
    sns.heatmap(heat_df, 
                annot=True, 
                cmap='inferno')
    plt.title('Heatmap of Type vs Rating')
    plt.show()



# 4. Correlation Heatmap - Duration vs Release Year
def plot_correlation_heatmap(df):
    netflix_cmap = LinearSegmentedColormap.from_list("netflix", ["black", "#E50914"])
    plt.figure(figsize=(6, 4))
    sns.heatmap(df[['duration_int', 'release_year']].corr(),
                annot=True,
                cmap=netflix_cmap,
                linewidths=0.5,
                linecolor='white',
                annot_kws={"size": 12, "color": "white"})
    plt.title("Netflix-Style Correlation Heatmap", fontsize=14, color="#E50914")
    plt.show()



# 5. Geographical Map - Netflix Shows by Country
def plot_geo_map(df):
    country_counts = df['country'].value_counts().reset_index()
    country_counts.columns = ['country', 'count']
    country_counts['count_log'] = np.log1p(country_counts['count'])
    fig = px.choropleth(
        country_counts,
        locations='country',
        locationmode='country names',
        color='count_log',
        color_continuous_scale=['#E50914', '#FFE5E5', '#FF9999'],
        title='Number of Shows per Country on Netflix'
    )
    fig.update_layout(width=1000, height=600, geo=dict(bgcolor='#000000'))
    return fig



# 6. Sunburst Chart - Type → Country → Genre
def plot_sunburst(df):
    df_sunburst = df.dropna(subset=['country', 'listed_in', 'type']).copy()
    df_sunburst['country'] = df_sunburst['country'].str.split(', ').str[0]
    df_sunburst['listed_in'] = df_sunburst['listed_in'].str.split(', ').str[0]
    fig = px.sunburst(df_sunburst, 
                      path=['type', 'country', 'listed_in'],
                      title='Netflix Content Hierarchy (Type → Country → Genre)')
    return fig



# 7. Treemap - Genre Distribution by Country
def plot_treemap(df):
    df_sunburst = df.dropna(subset=['country', 'listed_in']).copy()
    df_sunburst['country'] = df_sunburst['country'].str.split(', ').str[0]
    df_sunburst['listed_in'] = df_sunburst['listed_in'].str.split(', ').str[0]
    fig = px.treemap(df_sunburst, 
                     path=['country', 'listed_in'],
                     title='Treemap of Netflix Genres by Country')
    return fig



# 8. Radar Chart - Genre Diversity Comparison
def plot_radar(df):
    df_explode = df.dropna(subset=['listed_in', 'country'])
    df_explode['country'] = df_explode['country'].str.split(', ').str[0]
    df_explode['listed_in'] = df_explode['listed_in'].str.split(', ')
    df_explode = df_explode.explode('listed_in')
    top_countries = ['United States', 'India', 'United Kingdom']
    genres = df_explode['listed_in'].value_counts().nlargest(8).index.tolist()
    fig = go.Figure()
    for country in top_countries:
        genre_count = df_explode[df_explode['country'] == country]['listed_in'].value_counts()
        data = [genre_count.get(g, 0) for g in genres]
        fig.add_trace(go.Scatterpolar(r=data, theta=genres, fill='toself', name=country))
    fig.update_layout(title='Genre Spread Across Top 3 Countries',
                      polar=dict(radialaxis=dict(visible=True)))
    return fig



# 9. Donut Chart - Rating Breakdown
def plot_donut(df):
    rating_counts = df['rating'].value_counts().head(7)
    plt.figure(figsize=(8, 8))
    plt.pie(rating_counts, 
            labels=rating_counts.index, 
            autopct='%1.1f%%',
            startangle=90, 
            pctdistance=0.8,
            labeldistance=1.1,
            wedgeprops={'width': 0.4})
    plt.title('Netflix Content Rating Distribution (Donut Style)')
    plt.tight_layout()
    plt.show()



# 10. Stacked Area Chart - Content Added Over Time
def plot_area(df):
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    stacked = df.groupby(['year_added', 'type']).size().unstack().fillna(0)
    stacked.plot.area(figsize=(12, 6), 
                      colormap='Set2', 
                      alpha=0.8)
    plt.title('Netflix Content Growth Over Years')
    plt.ylabel('Number of Titles Added')
    plt.grid(True, linestyle='--')
    plt.show()



# 11. Bump Chart - Top Genres Over Years
def plot_bump(df):
    df_explode = df.dropna(subset=['listed_in', 'release_year']).copy()
    df_explode['listed_in'] = df_explode['listed_in'].str.split(', ')
    df_explode = df_explode.explode('listed_in')
    genre_year = df_explode.groupby(['release_year', 'listed_in']).size().reset_index(name='count')
    top_years = genre_year[genre_year['release_year'] >= 2015]
    pivot = top_years.pivot(index='release_year', columns='listed_in', values='count').fillna(0)
    top_genres = pivot.sum().sort_values(ascending=False).head(5).index
    pivot[top_genres].plot(figsize=(12, 6), marker='o')
    plt.title('Top Genre Trends Over the Years')
    plt.ylabel('Number of Titles Released')
    plt.grid(True)
    plt.show()



# 12. Word Cloud - Frequent Cast
def plot_wordcloud(df):
    text = ' '.join(df['cast'].dropna().astype(str))
    wordcloud = WordCloud(width=1000, 
                          height=500,
                          background_color='black',
                          colormap='Reds').generate(text)
    plt.figure(figsize=(15, 7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Frequent Actors in Netflix Titles')
    plt.show()



# 13. Lollipop Chart - Top Countries by Content
def plot_lollipop(df):
    top = df['country'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    plt.stem(top.index, top.values, basefmt=" ")
    plt.title('Top 10 Countries Producing Netflix Content (Lollipop Chart)')
    plt.ylabel('Number of Titles')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--')
    plt.show()



# 14. Swarm Plot - Ratings vs Duration
def plot_swarm(df):
    plt.figure(figsize=(12, 6))
    sns.swarmplot(data=df[df['type'] == 'Movie'],
                  x='rating', 
                  y='duration_int', 
                  palette='Set3')
    plt.title('Movie Duration Spread Across Ratings')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--')
    plt.show()



# 15. Sankey Diagram - Country → Type → Genre
def plot_sankey(df):
    df_sankey = df.dropna(subset=['country', 'type', 'listed_in']).copy()
    df_sankey['country'] = df_sankey['country'].str.split(', ').str[0]
    df_sankey['listed_in'] = df_sankey['listed_in'].str.split(', ').str[0]
    grouped = df_sankey.groupby(['country', 'type', 'listed_in']).size().reset_index(name='count')
    labels = list(pd.unique(grouped['country'])) + list(pd.unique(grouped['type'])) + list(pd.unique(grouped['listed_in']))
    label_to_index = {label: i for i, label in enumerate(labels)}
    sources = grouped['country'].map(label_to_index)
    targets_type = grouped['type'].map(label_to_index)
    targets_genre = grouped['listed_in'].map(label_to_index)
    source_list = sources.tolist()
    target_list = targets_type.tolist()
    value_list = grouped['count'].tolist()
    source_list += targets_type.tolist()
    target_list += targets_genre.tolist()
    value_list += grouped['count'].tolist()
    fig = go.Figure(data=[go.Sankey(
        node=dict(pad=15, thickness=20,
                  line=dict(color="black", width=0.5),
                  label=labels, color='rgba(229,9,20,0.8)'),
        link=dict(source=source_list, target=target_list, value=value_list)
    )])
    fig.update_layout(title_text="🔀 Netflix Flow: Country → Type → Genre", font_size=12)
    return fig
