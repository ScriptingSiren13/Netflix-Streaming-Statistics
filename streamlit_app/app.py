import streamlit as st
from matplotlib_venn import venn2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests
import json
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import analysis.insights as insights
import analysis.data_prep as data_prep
import analysis.eda_plots as eda_plots
from wordcloud import WordCloud
from matplotlib.colors import LinearSegmentedColormap
import plotly.express as px
import plotly.graph_objects as go



# -----------------------------



# Helper function to load Lottie JSON
def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)
    


# -----------------------------



# Loading Netflix Lottie animation
lottie_netflix = load_lottie_file("./netflix_logo.json")




# -----------------------------



# Setting up page:
st.set_page_config(page_title="Netflix Dashboard", layout="wide")



# -----------------------------



# Loading Font Awesome for icons:
st.markdown("""
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)



# -----------------------------



# Netflix palette:
netflix_red = "#E50914"
bg_black = "#121212"       
text_white = "#ffffff"     
netflix_red = "#E50914"    
bar_color = netflix_red
pie_colors = [netflix_red, "#333333"]



# -----------------------------



# Sidebar - only for social icons
st.sidebar.markdown("---")
st.sidebar.markdown(f"""
<style>
.social-icons {{
  display: flex;
  gap: 10px;
  font-size: 1.8rem;
  margin-top: 10px;
}}

.social-icons a {{
  color: black;  
  text-decoration: none;
  transition: transform 0.3s ease, color 0.3s ease;
  position: relative;
}}

.social-icons a:hover {{
  color: {bg_black}
  transform: scale(1.2);
}}

/* Tooltip Styling */
.social-icons a .tooltip {{
  visibility: hidden;
  background-color: {netflix_red};
  color: white;
  text-align: center;
  border-radius: 5px;
  padding: 4px 8px;
  position: absolute;
  z-index: 1;
  bottom: -30px;
  left: 50%;
  transform: translateX(-50%);
  opacity: 0;
  transition: opacity 0.3s ease;
  font-size: 0.7rem;
  white-space: nowrap;
}}

.social-icons a:hover .tooltip {{
  visibility: visible;
  opacity: 1;
}}
</style>

<div style="margin-top: 2rem;">
    <p style="color:black;">Made by Zarnain</p>
    <div class="social-icons">
        <a href="https://github.com/ScriptingSiren13" target="_blank">
            <i class="fab fa-github"></i>
            <span class="tooltip">GitHub</span>
        </a>
        <a href="www.linkedin.com/in/zarnain-723a31325" target="_blank">
            <i class="fab fa-linkedin"></i>
            <span class="tooltip">LinkedIn</span>
        </a>
        <a href="zedd.web13@gmail.com">
            <i class="fas fa-envelope"></i>
            <span class="tooltip">Email</span>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)



# -----------------------------



# custom CSS 
st.markdown(
    f"""
    <style>
    .stApp{{
        background-color:{netflix_red};
        color:{bg_black};
        max-width:1600px;
        padding:2rem;
        margin:0 auto;
    }}

    h1,h2,h3,h4,h5,h6, .stMarkdown{{
        color:{text_white} 
    }}

     .netflix-card{{
        background-color: black;      
        padding: 30px;
        border-radius: 15px;
        color: {text_white};
        font-size: 16px;
        transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        height: 375px;                         
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}

     .netflix-card:hover{{
        background-color: {bg_black};           
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        transform: translateY(-5px);            
        cursor: pointer;
    }}

    .equal-box{{
        height:100%;
        dispaly:flex;
        align-items:stretch;
        justify-content:center;
        flex-direction:column;
        background-color:#1c1c1c;
        border-radius:10px;
        padding:20px;
        color:{text_white};
        box-shadow:2px 2px 5px rgba(0,0,0,0.3)
    }}  

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------



col1,col2 =st.columns([1,8])
# with col1:
#     st.image(r"streamlit_app/netflix_logo.png",width=100)

with col2:
    st.markdown(
        f"""
        <h1 style='padding-top:10px; margin-left:2px;font-size:50px;color:{text_white}'>
              Netflix Streaming Stats
        </h1>
        """,
        unsafe_allow_html=True
    )




# Load data
df = pd.read_csv("../data/netflix_titles.csv")





# -----------------------------



# Tabs
tab1, tab2, tab3, tab4 = st.tabs([" About", " Raw Data", " Insights", "Plots"])




# ---------- TAB 2: About (EDA + Lottie)----------
with tab1:

    
    margin_left, main_content, margin_right = st.columns([1, 6, 1])

    with main_content:
         
        st.markdown(
            """
            <div style="margin-top: 2rem;">
            """,
            unsafe_allow_html=True
        )


        
        col_lottie, col_about = st.columns([1, 1])

    
        # Left: Lottie
        with col_lottie:
            st_lottie(lottie_netflix, speed=1, height=370, key="netflix")


        # Right: Card
        with col_about:
            st.markdown(
                """
                <div class="netflix-card">
                    This project is an interactive Exploratory Data Analysis (EDA) of Netflix titles using Streamlit.
                      It transforms raw data into meaningful visual insights, allowing users to explore content patterns by country, genre, ratings,
                        and release year. he dashboard features a variety of plots—heatmaps, sunburst charts, word clouds, and more—that uncover trends
                        in how Netflix has expanded globally and diversified its catalog over time.
                      Alongside the visuals, the app includes an option to access the full Jupyter Notebook analysis, making it both a data storytelling tool
                        and a hands-on reference for deeper exploration.
                </div>
                """,
                unsafe_allow_html=True
            )





# ---------- TAB 2: RAW DATA----------
with tab2:
    st.markdown(
        "<h2 style='color:black;'>Raw Data Overview</h2>", 
        unsafe_allow_html=True
    )

    #Load and preview data
    df = data_prep.load_data("../data/netflix_titles.csv")
    preview = data_prep.preview_data(df)

    


    #1. Showing the dataframs shape:
    st.markdown(
    f"<p style='color:black;'><b>1. Dataset Shape:</b> {preview['shape'][0]} rows x {preview['shape'][1]}</p>",
    unsafe_allow_html=True
)



    st.markdown("---") 



    #2. Showing column names
    st.markdown(
        "<p style='color:black;'><b>2. Columns</b></p>", 
        unsafe_allow_html=True
    )
    st.write(preview['columns'])



    st.markdown("---") 



    #3. Showing first 5 rows
    st.markdown(
        "<p style='color:black;'><b>3. Sample Data (first 5 rows)</b></p>", 
        unsafe_allow_html=True
    )
    st.dataframe(preview['head'])



    st.markdown("---") 



    #4. Showing Raw vs Cleaned data
    st.markdown(
        "<p style='color:black;'><b>4. Raw Data vs Cleaned Data</b></p>", 
        unsafe_allow_html=True
    )

    # Toggle for raw vs cleaned dataset
    show_cleaned = st.checkbox("Show cleaned dataset", value=True)

    if show_cleaned:
        cleaned_df = data_prep.clean_missing_values(df)
        st.markdown("### Cleaned Dataset")
        st.dataframe(cleaned_df)

        st.markdown("### Cleaning Rules Applied")
        st.write("- Filled missing **director** with 'Unknown'")
        st.write("- Filled missing **cast** with 'Unknown'")
        st.write("- Filled missing **rating** with mode value")
        st.write("- Filled missing **date_added** with 'Unknown'")
        st.write("- Imputed **country** using type + listed_in groupwise mode")
        st.write("- Dropped rows with missing **duration**")

    else:
        st.markdown("### Raw Dataset (with missing values)")
        st.dataframe(df)
    


    st.markdown("---") 



    #5. Data Type Conversion:
    st.markdown(
        "<p style='color:black;'><b>5. Data Type Conversion</b></p>", 
        unsafe_allow_html=True
    )

    converted_df = data_prep.convert_dtypes(cleaned_df if show_cleaned else df)

    col1, col2 = st.columns([2, 1])  # left side wider than right

    with col1:
        st.markdown("### Updated Data Types")
        dtypes_df = pd.DataFrame(converted_df.dtypes, columns=["dtype"]).reset_index()
        dtypes_df.columns = ["Column", "Data Type"]
        st.dataframe(dtypes_df, use_container_width=True)

    with col2:
        st.markdown("### Notes on Conversions")
        st.write("- **date_added** → converted to datetime")
        st.write("- **type, listed_in, country, rating** → converted to categorical")
        st.write("- **duration** → split into `duration_int` (numeric) + `duration_type` (string)")



    st.markdown("---") 



    #6. Outlier Handling:
    st.markdown(
        "<p style='color:black;'><b>6. Outlier Handling</b></p>", 
        unsafe_allow_html=True
    )

    # Toggle to compare before vs after outlier removal
    show_outliers = st.checkbox("Apply Outlier Handling (remove extreme movie durations)", value=True)

    if show_outliers:
        outlier_df = data_prep.handle_outliers(converted_df)

        st.markdown("### After Outlier Handling")
        st.dataframe(outlier_df)

        st.markdown("### Notes on Outlier Handling")
        st.write("- Removed extreme movie durations (>250 mins), unless interactive titles")
        st.write("- Kept known interactive titles (e.g., Bandersnatch)")
    else:
        st.markdown("### Before Outlier Handling")
        st.dataframe(converted_df)



    st.markdown("---") 



    # 7. Final Cleaned Dataset
    st.markdown(
        "<p style='color:black;'><b>7. Final Cleaned Dataset</b></p>", 
        unsafe_allow_html=True
    )

    final_df = outlier_df if show_outliers else converted_df

    st.dataframe(final_df)


    # Download button
    csv = final_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=" Download Cleaned Dataset as CSV",
        data=csv,
        file_name="netflix_cleaned.csv",
        mime="text/csv",
    )







# ---------- TAB 3: INSIGHTS ----------
with tab3:

    # ---------------- Q1 ----------------
    st.markdown("<h3 style='color:black;'>Q1: What types of content are on Netflix?</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        fig2, ax2 = plt.subplots(figsize=(3,3))

        sizes = df['type'].value_counts()
        labels = sizes.index

        wedges, texts, autotexts = ax2.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90,
            colors=pie_colors,
            textprops={'color': text_white}
        )

        ax2.set_title("Content Type Distribution", color=text_white)
        fig2.patch.set_facecolor(bg_black)
        st.pyplot(fig2)




    st.markdown("---")



    # ---------------- Q2 ----------------
    st.markdown("<h3 style='color:black;'>Q2: How has Netflix grown over the years?</h3>", unsafe_allow_html=True)
    count_by_year = df['release_year'].value_counts().sort_index()

    fig2, ax2 = plt.subplots(figsize=(12, 5))
    count_by_year.plot(kind='bar', color='#E50914', title='Netflix Over the Years', ax=ax2)
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots(figsize=(12, 5))
    df.groupby(['release_year', 'type'], observed=True).size().unstack().plot(
        kind='bar', stacked=True, color=['#E50914','black'], ax=ax3
    )
    st.pyplot(fig3)   



    st.markdown("---")



    # ---------------- Q3 ----------------
    st.markdown("<h3 style='color:black;'>Q3: Which countries contribute the most content?</h3>", unsafe_allow_html=True)
    top_n = 10
    top = df['country'].value_counts().head(top_n)

    fig4, ax4 = plt.subplots(figsize=(12, 5))
    top.plot(kind='bar', color='#E50914', title=f'Top {top_n} Content Producing Countries', ax=ax4)
    plt.xticks(rotation=45)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    st.pyplot(fig4)

    

    st.markdown("---")



    # ---------------- Q4: Top Directors ----------------
    st.markdown("<h3 style='color:black;'>Q4: Who are the most featured directors?</h3>", unsafe_allow_html=True)
    top_directors = df['director'].value_counts().head(10)

    fig5, ax5 = plt.subplots(figsize=(12, 5))
    top_directors.plot(kind='bar', color='#E50914', title='Most Frequent Directors', ax=ax5)
    plt.xticks(rotation=45)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    st.pyplot(fig5)



    st.markdown("---")



    # ---------------- Q5: Top Actors ----------------
    st.markdown("<h3 style='color:black;'>Q5: Who are the most featured actors?</h3>", unsafe_allow_html=True)
    all_cast = df['cast'].dropna().str.split(', ')
    flat_cast = [actor.strip() for sublist in all_cast for actor in sublist]
    top_actors = pd.Series(flat_cast).value_counts().head(10)

    fig6, ax6 = plt.subplots(figsize=(12, 5))
    top_actors.plot(kind='bar', color='#E50914', title='Most Frequent Actors', ax=ax6)
    plt.xticks(rotation=45)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    st.pyplot(fig6)

  

    st.markdown("---")



    # ---------------- Q6a: Movie Duration ----------------
    st.markdown("<h3 style='color:black;'>Q6a: What is the typical duration of movies on Netflix?</h3>", unsafe_allow_html=True)
    movies = converted_df[converted_df['type'] == 'Movie']

    fig7, ax7 = plt.subplots(figsize=(12, 5))
    ax7.hist(movies['duration_int'].dropna(), bins=30, color='#E50914', edgecolor='black')
    ax7.set_title('Distribution of Movie Durations')
    ax7.set_xlabel('Duration (minutes)')
    ax7.set_ylabel('Number of Movies')
    ax7.grid(True)
    st.pyplot(fig7)



    st.markdown("---")



    # ---------------- Q6b: Kids Content Trend ----------------
    st.markdown("<h3 style='color:black;'>Q6b: How has the production of kids’ content changed over time?</h3>", unsafe_allow_html=True)
    kids_df = df[df['rating'].str.contains('TV-Y|TV-G|TV-PG', na=False)]
    kids_by_year = kids_df['release_year'].value_counts().sort_index()

    fig8, ax8 = plt.subplots(figsize=(12, 5))
    kids_by_year.plot(kind='line', color="#E50914", title="Trend of Kid's Content Over the Years", ax=ax8)
    st.pyplot(fig8)



    st.markdown("---")



    # ---------------- Q7: Genre by Country ----------------
    st.markdown("<h3 style='color:black;'>Q7: Are some countries specialized in specific genres?</h3>", unsafe_allow_html=True)
    df_explode = df.dropna(subset=['country','listed_in']).copy()
    df_explode['country'] = df_explode['country'].str.split(', ')
    df_explode['listed_in'] = df_explode['listed_in'].str.split(', ')
    df_explode = df_explode.explode('country').explode('listed_in')

    genre_by_country = df_explode.groupby(['country','listed_in']).size().unstack().fillna(0)

    top_countries = df_explode['country'].value_counts().head(10).index
    top_genres = df_explode['listed_in'].value_counts().head(5).index
    filtered_df = genre_by_country.loc[top_countries, top_genres]

    # Heatmap
    fig9, ax9 = plt.subplots(figsize=(18, 8))
    sns.heatmap(genre_by_country.loc[top_countries], cmap='Reds', linewidths=0.5, linecolor='gray', ax=ax9)
    plt.title("Genre Distribution Across Top Content-Producing Countries")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig9)

    # Horizontal stacked bar
    fig10, ax10 = plt.subplots(figsize=(14, 8))
    filtered_df.plot(kind='barh', stacked=True, colormap='tab10', edgecolor='black', ax=ax10)
    plt.title("Top Genres in Top Countries")
    plt.xlabel("Number of Titles")
    plt.ylabel("Countries")
    plt.tight_layout()
    plt.grid(True, axis='x', linestyle='--', alpha=0.6)
    st.pyplot(fig10)


    st.markdown("---")


   
    # Q8. When does Netflix usually add new content?
    st.markdown("<h3 style='color:black;'>Q8. When Does Netflix Usually Add New Content?</h3>", unsafe_allow_html=True)

    df_addition = converted_df.copy()
    df_addition['date_added'] = pd.to_datetime(df_addition['date_added'], errors='coerce')
    df_addition['month_added'] = df_addition['date_added'].dt.month

    monthly_counts = df_addition['month_added'].value_counts().sort_index()

    fig8, ax8 = plt.subplots(figsize=(10, 5))
    monthly_counts.plot(kind='bar', color='#E50914', edgecolor='black', ax=ax8)

    ax8.set_xticks(range(12))
    ax8.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun',
                        'Jul','Aug','Sep','Oct','Nov','Dec'], rotation=45)
    ax8.set_title("Monthly Trend of Netflix Content Additions")
    ax8.set_ylabel("Number of Titles Added")
    ax8.grid(axis='y', linestyle='--', alpha=0.5)

    st.pyplot(fig8, dpi=70)



    st.markdown("---")



    # Q9. Country-wise Breakdown of Movies vs TV Shows
    st.markdown("<h3 style='color:black;'>Q9. Country-wise Breakdown of Movies vs TV Shows</h3>", unsafe_allow_html=True)
    country_type = converted_df.groupby(['country','type'], observed=True).size().unstack().fillna(0)
    top_country_type = country_type.sort_values('Movie', ascending=False).head(10)

    fig9, ax9 = plt.subplots(figsize=(7, 4))  
    top_country_type.plot(kind='bar', stacked=True, color=['#E50914','black'], ax=ax9)

    ax9.set_title("Top Countries by Content Type", fontsize=12)  # shrink font size
    ax9.set_ylabel("Number of Titles", fontsize=10)
    ax9.set_xticklabels(ax9.get_xticklabels(), rotation=45, fontsize=9)
    ax9.grid(axis='y', linestyle='--', alpha=0.6)

    st.pyplot(fig9)



    st.markdown("---")



    # Q10. Are Genres Unique to TV Shows or Movies? (Venn Diagram)
    st.markdown("<h3 style='color:black;'>Q10. Are Genres Unique to TV Shows or Movies?</h3>", unsafe_allow_html=True)
    df_exploded = converted_df.dropna(subset=['listed_in']).copy()
    df_exploded['listed_in'] = df_exploded['listed_in'].str.split(', ')
    df_exploded = df_exploded.explode('listed_in')

    movie_genres = set(df_exploded[df_exploded['type']=='Movie']['listed_in'])
    tv_genres = set(df_exploded[df_exploded['type']=='TV Show']['listed_in'])

    fig10, ax10 = plt.subplots(figsize=(7, 5))
    venn2([movie_genres, tv_genres],
          set_labels=('Movies','TV Shows'),
          set_colors=('#E50914','black'),
          alpha=0.7, ax=ax10)
    ax10.set_title("Genre Overlap Between Movies and TV Shows on Netflix")
    st.pyplot(fig10)



    st.markdown("---")



    # Q11. How Many Seasons Do TV Shows Usually Have?
    st.markdown("<h3 style='color:black;'>Q11. How Many Seasons Do TV Shows Usually Have?</h3>", unsafe_allow_html=True)
    tv_shows = converted_df[converted_df['type']=='TV Show'].copy()
    tv_shows['duration_int'] = pd.to_numeric(tv_shows['duration'].str.extract(r'(\d+)')[0])


    fig11, ax11 = plt.subplots(figsize=(12, 6))
    ax11.hist(tv_shows['duration_int'], 
              bins=range(1, tv_shows['duration_int'].max()+2), 
              color='#E50914', edgecolor='black', align='left')
    ax11.set_title("Distribution of TV Show Seasons")
    ax11.set_xlabel("Number of Seasons")
    ax11.set_ylabel("Number of TV Shows")
    ax11.set_xticks(range(1, tv_shows['duration_int'].max()+1))
    ax11.grid(axis='y', linestyle='--', alpha=0.5)
    st.pyplot(fig11)



    st.markdown("---")



    # Q12. Which content ratings dominate on Netflix?
    st.markdown("<h3 style='color:black;'>Q12. Which content ratings dominate on Netflix?</h3>", unsafe_allow_html=True)
    
    rating_counts = insights.rating_distribution(df)

    # show the matplotlib chart inside Streamlit
    fig, ax = plt.subplots(figsize=(11,5))
    rating_counts.plot(kind='bar', color='#E50914', edgecolor='black', ax=ax)
    ax.set_title("Distribution of Content Ratings")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Number of Titles")
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    plt.xticks(rotation=45)
    st.pyplot(fig)



    st.markdown("---")


   # Q13. What Genres Do Top Netflix Directors Prefer?
    st.markdown("<h3 style='color:black;'>Q13. What Genres Do Top Netflix Directors Prefer?</h3>", unsafe_allow_html=True)
    
    # Get top 10 directors
    top_directors = df['director'].value_counts().head(10)

    # Explode genre since one title can have multiple genres
    df_genre = df.copy()
    df_genre = df_genre[df_genre['director'].isin(top_directors.index)]
    df_genre['listed_in'] = df_genre['listed_in'].str.split(', ')
    df_genre = df_genre.explode('listed_in')

    # Group and count
    director_genre = df_genre.groupby(['director', 'listed_in']).size().unstack().fillna(0)

    # Plotting inside Streamlit
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.heatmap(director_genre, cmap='YlGnBu', linewidths=0.5, ax=ax)
    ax.set_title('Top Directors vs. Genres (Heatmap)')
    ax.set_xlabel('Genre')
    ax.set_ylabel('Director')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)



    st.markdown("---")



    # Q14. Do international directors contribute more to a diverse set of genres?
    st.markdown("<h3 style='color:black;'>Q14. Do international directors contribute more to a diverse set of genres?</h3>", unsafe_allow_html=True)
    
    # Filter and explode the data
    df_genre_explode = df.copy()
    df_genre_explode = df_genre_explode[df_genre_explode['director'] != 'Unknown']
    df_genre_explode = df_genre_explode.dropna(subset=['country','listed_in'])
    df_genre_explode['country'] = df_genre_explode['country'].str.split(', ')
    df_genre_explode['listed_in'] = df_genre_explode['listed_in'].str.split(', ')
    df_genre_explode = df_genre_explode.explode('country').explode('listed_in')

    # Calculate unique genre counts per director
    genre_diversity = df_genre_explode.groupby('director')['listed_in'].nunique().reset_index()
    genre_diversity.columns = ['director','unique_genre_count']

    # Map each director to their top country
    director_country = df_genre_explode.groupby(['director','country']).size().reset_index(name='count')
    top_country = director_country.sort_values('count', ascending=False).drop_duplicates('director')
    genre_diversity = genre_diversity.merge(top_country[['director','country']], on='director')

    # Filter for top 15 countries
    top_countries = genre_diversity['country'].value_counts().head(15).index
    filtered_data = genre_diversity[genre_diversity['country'].isin(top_countries)]

    # Plotting boxplot inside Streamlit
    fig, ax = plt.subplots(figsize=(13,5))
    sns.boxplot(data=filtered_data, x='country', y='unique_genre_count', color='#E50914', showmeans=True,
                meanprops={"marker":"o","markerfacecolor":"white","markeredgecolor":"black"}, ax=ax)
    ax.set_title("Genre Diversity of Directors by Top 15 Countries")
    ax.set_xlabel("Country")
    ax.set_ylabel("Number of Unique Genres Directed")
    plt.xticks(rotation=45)
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig)



    st.markdown("---")



    # Q15: Metadata Completeness by Year 
    st.markdown("<h3 style='color:black;'>Q15. Are newer releases more likely to have complete metadata?</h3>", unsafe_allow_html=True)
    

    # Define metadata columns to check
    metadata_cols = ['director','cast','country','rating','date_added','duration']

    # Calculate metadata completeness for each title
    df['metadata_complete_count'] = df[metadata_cols].notnull().sum(axis=1)
    df['total_metadata_fields'] = len(metadata_cols)
    df['metadata_completeness'] = df['metadata_complete_count'] / df['total_metadata_fields']

    # Compute average completeness by release year
    completeness_by_year = df.groupby('release_year')['metadata_completeness'].mean()

    # Plot the line chart in Streamlit
    fig, ax = plt.subplots(figsize=(13,5))
    completeness_by_year.plot(kind='line', color='#E50914', marker='o', ax=ax)
    ax.set_title("Average Metadata Completeness by Release Year")
    ax.set_xlabel("Release Year")
    ax.set_ylabel("Avg. Metadata Completeness (0 to 1)")
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig)





with tab4:

    # Q1. Violin Plot - Movie Duration Distribution by Rating
    st.subheader("1. Movie Duration Distribution by Rating")

    # Filter only movies (in case TV Shows are present)
    movies = converted_df[converted_df['type'] == 'Movie'].copy()

    # Ensure numeric duration
    movies['duration_int'] = pd.to_numeric(movies['duration'].str.extract(r'(\d+)')[0], errors='coerce')


    # Plot
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.violinplot(data=movies,
                x='rating',
                y='duration_int',
                color="#E50914",
                ax=ax)
    ax.set_title('Movie Duration Distribution by Rating')
    plt.xticks(rotation=45)
    st.pyplot(fig)



    st.markdown("---")



    # Q2. Scatterplot - Release Year vs Movie Duration
    st.subheader("2. Release Year vs Movie Duration")

    # Filter movies only
    movies = converted_df[converted_df['type'] == 'Movie'].copy()
    movies['duration_int'] = pd.to_numeric(movies['duration'].str.extract(r'(\d+)')[0], errors='coerce')


    # Plot
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.scatter(movies['release_year'],
            movies['duration_int'],
            alpha=0.5,
            color="#E50914")
    ax.set_title('Release Year vs Movie Duration')
    ax.set_xlabel('Release Year')
    ax.set_ylabel('Duration (minutes)')
    ax.grid(True)

    st.pyplot(fig)



    st.markdown("---")



   # Q3. Heatmap - Type vs Rating vs Count
    st.subheader("3. Heatmap - Type vs Rating vs Count")

    heat_df = pd.crosstab(converted_df['type'], converted_df['rating'])
    fig, ax = plt.subplots(figsize=(20, 5))
    sns.heatmap(heat_df, annot=True, cmap='inferno', ax=ax)
    ax.set_title('Heatmap of Type vs Rating')
    st.pyplot(fig)



    st.markdown("---")



    # Q4. Correlation Heatmap - Duration vs Release Year
    st.subheader("4. Correlation Heatmap - Duration vs Release Year")

    # Ensure duration is numeric
    converted_df['duration_int'] = pd.to_numeric(
        converted_df['duration'].str.extract('(\d+)')[0], errors='coerce'
    )

    netflix_cmap = LinearSegmentedColormap.from_list("netflix", ["black", "#E50914"])
    fig, ax = plt.subplots(figsize=(12,6))
    sns.heatmap(
        converted_df[['duration_int', 'release_year']].corr(),
        annot=True,
        cmap=netflix_cmap,
        linewidths=0.5,
        linecolor='white',
        annot_kws={"size": 12, "color": "white"},
        ax=ax
    )
    ax.set_title("Netflix-Style Correlation Heatmap", fontsize=14, color="#E50914")
    st.pyplot(fig)



    st.markdown("---")



    # Q5. Geographic Distribution of Netflix Content
    st.subheader("5. Geographic Distribution of Netflix Content")

    fig = eda_plots.plot_geo_map(converted_df)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")



    # Q6. Sunburst Chart - Type → Country → Genre
    st.subheader("6. Netflix Content Hierarchy (Type → Country → Genre)")

    fig = eda_plots.plot_sunburst(converted_df)
    st.plotly_chart(fig, use_container_width=True)



    st.markdown("---")



    # Q7. Treemap - Genre Distribution by Country
    st.subheader("7. Treemap of Netflix Genres by Country")

    fig = eda_plots.plot_treemap(converted_df)
    st.plotly_chart(fig, use_container_width=True)



    st.markdown("---")



    # Q8. Radar Chart - Genre Diversity Comparison
    st.subheader("8. Genre Spread Across Top 3 Countries")

    fig = eda_plots.plot_radar(converted_df)
    st.plotly_chart(fig, use_container_width=True)



    st.markdown("---")


    # Q9. Donut Chart - Rating Breakdown
    st.subheader("9. Netflix Content Rating Distribution (Donut Style)")

    fig, ax = plt.subplots(figsize=(5, 4), dpi=80)  # slightly wider
    rating_counts = converted_df['rating'].value_counts().head(7)
    wedges, texts, autotexts = ax.pie(
        rating_counts, 
        labels=rating_counts.index, 
        autopct='%1.1f%%',
        startangle=90, 
        pctdistance=0.7,  # closer to center
        labeldistance=1.2,  # move labels a bit out
        wedgeprops={'width': 0.4}
    )

    # Reduce font size for percentage labels and labels
    for t in texts + autotexts:
        t.set_fontsize(9)

    ax.set_title('Netflix Content Rating Distribution (Donut Style)', fontsize=12)

    # Prevent Streamlit from stretching the figure
    st.pyplot(fig, use_container_width=False)





    # Q10. Stacked Area Chart - Content Added Over Time
    st.subheader("10. Netflix Content Growth Over Years")
    fig, ax = plt.subplots(figsize=(10, 5))
    stacked = converted_df.groupby([converted_df['date_added'].dt.year, 'type']).size().unstack().fillna(0)
    stacked.plot.area(ax=ax, colormap='Set2', alpha=0.8)
    ax.set_title('Netflix Content Growth Over Years')
    ax.set_ylabel('Number of Titles Added')
    ax.grid(True, linestyle='--')
    st.pyplot(fig)



    st.markdown("---")



    # Q11. Bump Chart - Top Genres Over Years
    st.subheader("11. Top Genre Trends Over the Years")
    fig, ax = plt.subplots(figsize=(10, 5))
    df_explode = converted_df.dropna(subset=['listed_in', 'release_year']).copy()
    df_explode['listed_in'] = df_explode['listed_in'].str.split(', ')
    df_explode = df_explode.explode('listed_in')
    genre_year = df_explode.groupby(['release_year', 'listed_in']).size().reset_index(name='count')
    top_years = genre_year[genre_year['release_year'] >= 2015]
    pivot = top_years.pivot(index='release_year', columns='listed_in', values='count').fillna(0)
    top_genres = pivot.sum().sort_values(ascending=False).head(5).index
    pivot[top_genres].plot(ax=ax, marker='o')
    ax.set_title('Top Genre Trends Over the Years')
    ax.set_ylabel('Number of Titles Released')
    ax.grid(True)
    st.pyplot(fig)



    st.markdown("---")



    # Q12. Word Cloud - Frequent Cast
    st.subheader("12. Frequent Actors in Netflix Titles")
    fig, ax = plt.subplots(figsize=(10, 5))
    text = ' '.join(converted_df['cast'].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='black', colormap='Reds').generate(text)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Frequent Actors in Netflix Titles')
    st.pyplot(fig)



    st.markdown("---")



    # Q13. Lollipop Chart - Top Countries by Content
    st.subheader("13. Top 10 Countries Producing Netflix Content")
    fig, ax = plt.subplots(figsize=(8, 5))
    top = converted_df['country'].value_counts().head(10)
    ax.stem(top.index, top.values, basefmt=" ")
    ax.set_title('Top 10 Countries Producing Netflix Content (Lollipop Chart)')
    ax.set_ylabel('Number of Titles')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.grid(True, axis='y', linestyle='--')
    st.pyplot(fig)



    st.markdown("---")



    # Q14. Swarm Plot - Ratings vs Duration
    st.subheader("14. Movie Duration Spread Across Ratings")
    fig, ax = plt.subplots(figsize=(9, 5))
    converted_df['duration_int'] = pd.to_numeric(converted_df['duration'].str.extract('(\d+)')[0], errors='coerce')
    sns.swarmplot(data=converted_df[converted_df['type'] == 'Movie'],
                x='rating', y='duration_int', palette='Set3', ax=ax)
    ax.set_title('Movie Duration Spread Across Ratings')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.grid(True, axis='y', linestyle='--')
    st.pyplot(fig)



    st.markdown("---")



    # Q15. Sankey Diagram - Country → Type → Genre
    st.subheader("15. Netflix Flow: Country → Type → Genre")
    fig = eda_plots.plot_sankey(converted_df)
    st.plotly_chart(fig, use_container_width=True)



  
    

    




