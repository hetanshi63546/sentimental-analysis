positive_words = ["love", "happy", "good", "great", "amazing", "excellent", "awesome"]
negative_words = ["hate", "terrible", "bad", "worst", "awful", "horrible", "poor"]

def analyze_sentiment(text):
    text_lower = text.lower()
    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)
    
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"


print("Simple Sentiment Analysis (type 'exit' to quit)")
while True:
    user_input = input("Enter your sentence: ")
    if user_input.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break
    sentiment = analyze_sentiment(user_input)
    print(f"Sentiment: {sentiment}\n")