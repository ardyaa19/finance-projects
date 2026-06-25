from sentiment import get_sentiment

with open("data/transcript.txt", "r", encoding = "utf-8") as file:
    transcript = file.read()

result = get_sentiment(transcript)
print(result)