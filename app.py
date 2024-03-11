import nltk
nltk.download('vader_lexicon', download_dir='./nltk_data')
nltk.data.path.append('./nltk_data')


import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK data
import nltk
nltk.download('vader_lexicon')

# Function for sentiment analysis
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Streamlit app
def main():
    st.title("Sentiment Analysis App")
    st.write("Enter a sentence, and the app will analyze its sentiment.")

    # User input
    user_input = st.text_input("Enter your sentence:")

    # Analyze sentiment on button click
    if st.button("Analyze Sentiment"):
        if user_input:
            sentiment = analyze_sentiment(user_input)
            st.write(f"Sentiment: {sentiment}")
        else:
            st.warning("Please enter a sentence.")

if __name__ == "__main__":
    main()
