# Movie Recommender System

## Overview

Welcome to the Movie Recommender System! This project employs a feature-based approach using Natural Language Processing (NLP) techniques to recommend movies tailored to the user's preferences. The system takes into account various factors, such as storyline, genre, keywords, cast, and crew.

## How it Works

### 1. Stemming Process in NLP

Our system employs stemming in NLP to enhance the accuracy of movie recommendations. Stemming involves reducing words to their root or base form, removing prefixes and suffixes. This ensures that similar words (e.g., "running" and "run") are treated as the same, improving the system's understanding of textual data.

### 2. Cosine Similarity

The core of our recommendation engine lies in the use of cosine similarity. This mathematical technique measures the cosine of the angle between two vectors, providing a measure of similarity between documents. In our case, movies are represented as vectors based on various features. The system calculates the cosine similarity between the input movie and others in the dataset, generating a personalized list of 9 movie recommendations.

## Demo

### Screenshots

Include a few screenshots to showcase the UI and different aspects of your Movie Recommender System.

![Screenshot 1](/output/Screenshot%202024-01-10%20at%2011.30.44 AM.png)
*Search page for the movie*

![Screenshot 2](/output/Screenshot%202024-01-10%20at%2011.34.33 AM.png)
*Details of the selected movie*

![Screenshot 1](/output/Screenshot%202024-01-10%20at%2011.34.42 AM.png)
*Details of recommended movie*

### Video Demo

[![Movie Recommender System Demo](/output/Screenshot%202024-01-10%20at%2011.30.44 AM.png)](/output/Screen%20Recording%202024-01-10%20at%2011.32.27 AM.mov)
*Click the image above to watch the demo video.*

## Model Deployment

Check out the deployed model [here](https://movierecommendation-ratish.streamlit.app/).

## How to Use


```bash
# Clone the repository
git clone https://github.com/Ratish-ai/movie_recommendation.git