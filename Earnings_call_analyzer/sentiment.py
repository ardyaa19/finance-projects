from transformers import pipeline
classifier = pipeline("sentiment-analysis", model = "ProsusAI/finbert")
def get_sentiment(text):
    result = classifier(text[:512])
    return result[0]