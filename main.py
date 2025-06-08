import pandas as pd
from src.config_loader import load_config
from src.utils import init_logger, label_sentiment
from src.sentiment import train_model, predict_headline
from src.robot_controller import NAOEmotionResponder

def main():
    cfg = load_config()
    init_logger(cfg["log_path"])

    # Load dataset
    df = pd.read_csv(cfg["data_path"])

    # Label sentiments using TextBlob
    df['sentiment'] = df['headline'].apply(label_sentiment)

    # Show original distribution
    print("\nOriginal sentiment distribution:")
    print(df['sentiment'].value_counts())

    # Balance the dataset
    min_class_size = df['sentiment'].value_counts().min()
    df_balanced = df.groupby('sentiment').sample(n=min_class_size, random_state=42).reset_index(drop=True)

    # Show balanced distribution
    print("\nBalanced training data:")
    print(df_balanced['sentiment'].value_counts())

    # Train model on balanced data
    train_model(df_balanced, cfg["model_path"])

    # Simulate robot interaction
    nao = NAOEmotionResponder()

    # Prompt until valid input
    sample_headline = ""
    while not sample_headline.strip():
        sample_headline = input("Enter a weather headline: ").strip()

    prediction = predict_headline(sample_headline, cfg["model_path"])
    import logging

# Log and act
    log_entry = f"Headline: {sample_headline} | Sentiment: {prediction}"
    print(log_entry)
    logging.info(log_entry)

    nao.act_on_sentiment(prediction, sample_headline)


if __name__ == "__main__":
    main()
