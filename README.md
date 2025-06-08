# 🌦️ Emotional Weather Newsreader with NAO V6
This project is a machine learning-driven emotional weather newsreader that combines Natural Language Processing, sentiment analysis, and human-robot interaction. It enables the NAO V6 robot to read out UK weather headlines using expressive tone, gestures, and LED facial feedback.

## 🤖 What It Does
- Scrapes UK weather headlines from a news source
- Classifies each headline as positive, neutral, or negative using a supervised ML model
- Delivers the headline via NAO with appropriate:
- Vocal tone
- LED facial expression
- Physical gesture

## 💡 Key Features
- Supervised sentiment classification using logistic regression 
- Real-time integration with NAO V6 via NAOqi SDK
- Supports accessibility through multimodal communication
- Designed with inclusivity in mind (e.g., learning disabilities, visual impairment)

## 📁 Structure
```bash
├── data/                  # Cleaned and labelled weather headlines
├── model/                 # Trained sentiment classifier (.joblib)
├── scripts/               # Python scripts for scraping, training, and deployment
├── robot/                 # NAOqi-based delivery scripts
└── README.md
```

## 🛠️ Technologies Used
- Python (Pandas, scikit-learn)
- Logistic Regression
- Bag-of-Words (CountVectorizer)
- NAOqi SDK
- Matplotlib (EDA)
- CSV, JSON (data logging)

## 🔮 Future Plans
- Integrate transformer models (e.g., BERT) for deeper sentiment understanding
- Connect to live news feeds for automatic, real-time delivery
- Add speech output for blind users and camera-based feedback for reactive interaction
