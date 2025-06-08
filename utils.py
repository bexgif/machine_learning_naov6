from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def label_sentiment(text):
    text_lower = text.lower()

    # Refined keyword lists
    negative_keywords = [
        "storm", "thunder", "flood", "chaos", "fog", "ice", "warning", "snow",
        "winds", "threat", "black ice", "visibility", "disruption", "gale", "severe"
    ]
    positive_keywords = [
        "sunny", "clear skies", "good weather", "warm", "heat", "dry", "ideal weather",
        "bright", "pleasant", "mild", "calm"
    ]

    # Forced keyword classification
    if any(neg_word in text_lower for neg_word in negative_keywords):
        return "negative"
    if any(pos_word in text_lower for pos_word in positive_keywords):
        return "positive"

    # Fallback to VADER score
    score = analyser.polarity_scores(text)["compound"]
    if score >= 0.3:
        return "positive"
    elif score <= -0.3:
        return "negative"
    else:
        return "neutral"

import logging

def init_logger(log_path):
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
