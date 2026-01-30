print("AI-Based Sentiment Analyzer")

positive_words = ["good", "happy", "excellent", "great", "love", "amazing"]
negative_words = ["bad", "sad", "worst", "hate", "poor", "angry"]

sentence = input("Enter a sentence: ").lower()

positive_count = 0
negative_count = 0

for word in positive_words:
    if word in sentence:
        positive_count += 1

for word in negative_words:
    if word in sentence:
        negative_count += 1

if positive_count > negative_count:
    print("Sentiment: Positive 😊")
elif negative_count > positive_count:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")
