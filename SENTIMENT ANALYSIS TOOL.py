def analyze_sentiment(text):
    positive_keywords = ['love', 'good', 'great', 'happy', 'excellent', 'amazing', 'awesome', 'wonderful', 'best', 'joyful', 'pleasant', 'positive']
    negative_keywords = ['hate', 'bad', 'awful', 'terrible', 'horrible', 'sad', 'angry', 'disappointed', 'worst', 'miserable', 'unhappy', 'negative']
    intensifiers = ['very', 'extremely', 'super', 'totally', 'absolutely', 'quite', 'really']
    negation_words = ['not', 'no', 'never', 'none', 'neither', 'nobody', 'nothing', 'hardly', 'scarcely', 'barely']
    
    text = text.lower()
    positive_score = 0
    negative_score = 0
    words = text.split()
    negation_found = False

    for i, word in enumerate(words):
        if word in negation_words:
            negation_found = True
        elif word in intensifiers:
            if i + 1 < len(words) and words[i + 1] in positive_keywords:
                positive_score += 2
            elif i + 1 < len(words) and words[i + 1] in negative_keywords:
                negative_score += 2
        elif word in positive_keywords:
            positive_score += 1
        elif word in negative_keywords:
            negative_score += 1

    if negation_found:
        positive_score, negative_score = negative_score, positive_score

    if positive_score > negative_score:
        if positive_score > 3:
            return "Overall Sentiment: Very Positive 😊"
        else:
            return "Overall Sentiment: Positive 😊"
    elif negative_score > positive_score:
        if negative_score > 3:
            return "Overall Sentiment: Very Negative 😞"
        else:
            return "Overall Sentiment: Negative 😞"
    else:
        return "Overall Sentiment: Neutral 😐"

def main():
    print("Sentiment Analysis Tool (Advanced Version)")
    while True:
        text = input("\nEnter a sentence for sentiment analysis (or 'exit' to quit): ")
        if text.lower() == "exit":
            print("\nGoodbye!")
            break
        result = analyze_sentiment(text)
        print(result)

if _name_ == "_main_":
    main()
