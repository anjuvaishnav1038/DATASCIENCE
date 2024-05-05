import speech_recognition as sr
from textblob import TextBlob
import streamlit as st

def speech_to_text(language):
  """Recognizes speech in the specified language and returns the text."""
  s = sr.Recognizer()
  with sr.Microphone() as source:
    st.write(f"Speak in {language.upper()}:")
    audio = s.listen(source)
  try:
    query = s.recognize_google(audio, language=language)
    return query
  except sr.UnknownValueError:
    st.error(f"Sorry, I couldn't understand the speech in {language.upper()}.")
    return None

def analyze_sentiment(text):
  """Analyzes the sentiment of the provided text and returns the polarity score."""
  if text:
    sentiment = TextBlob(text).sentiment
    return sentiment.polarity
  else:
    return None

def main():
  """Builds the Streamlit web page for speech recognition and sentiment analysis."""
  st.title("Speech Recognition and Sentiment Analysis")

  language_options = ["English", "Hindi"]
  selected_language = st.selectbox("Select Language", language_options)

  user_query = speech_to_text(selected_language.lower())

  if user_query:
    sentiment_score = analyze_sentiment(user_query)
    st.write(f"**You said:** {user_query}")
    if sentiment_score is not None:
      sentiment_text = "Positive" if sentiment_score > 0 else ("Negative" if sentiment_score < 0 else "Neutral")
      st.write(f"**Sentiment:** {sentiment_text} (Polarity Score: {sentiment_score:.2f})")

if __name__ == "__main__":
  main()
