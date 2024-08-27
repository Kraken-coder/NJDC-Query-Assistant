import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Sample FAQs and corresponding responses
faqs = [
    "What services does the Department of Justice provide?",
    "How can I file a complaint?",
    "Where can I find information on civil rights?",
    "How do I report a crime?",
    "What are the responsibilities of the Department of Justice?",
    "What is the mission of the Department of Justice?",  # New FAQ
    "How can I contact the Department of Justice?",       # New FAQ
    "Where can I find information about the Freedom of Information Act (FOIA)?",  # New FAQ
    "What is the Office of Justice Programs?",            # New FAQ
    "How do I find a list of DOJ press releases?"         # New FAQ
]

responses = [
    "The Department of Justice provides legal advice to the government, represents the state in legal matters, and ensures the enforcement of the law.",
    "You can file a complaint by visiting our official website and following the complaint submission process.",
    "Information on civil rights can be found under the 'Civil Rights' section on our website.",
    "To report a crime, please visit the 'Report a Crime' section on our website or contact your local law enforcement agency.",
    "The Department of Justice is responsible for upholding the rule of law, prosecuting federal cases, and ensuring justice is served.",
    "The mission of the Department of Justice is to enforce the law and defend the interests of the United States according to the law, ensure public safety, provide federal leadership in preventing and controlling crime, seek just punishment for those guilty of unlawful behavior, and ensure fair and impartial administration of justice for all Americans.",  # Response to new FAQ
    "You can contact the Department of Justice by visiting our 'Contact Us' page on the official website, where you can find phone numbers, email addresses, and mailing addresses for various offices and services.",  # Response to new FAQ
    "Information about the Freedom of Information Act (FOIA) can be found on the 'FOIA' page of the Department of Justice's website, including details on how to file a FOIA request.",  # Response to new FAQ
    "The Office of Justice Programs (OJP) provides federal leadership, grants, training, technical assistance, and other resources to improve the nation’s capacity to prevent and reduce crime, assist victims, and enforce state, local, and tribal laws.",  # Response to new FAQ
    "A list of DOJ press releases can be found in the 'News' section of the Department of Justice's website, where you can filter by date and topic."  # Response to new FAQ
]

# Function to preprocess text
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)

# Preprocess FAQs
preprocessed_faqs = [preprocess(faq) for faq in faqs]

# Function to generate chatbot response
def chatbot_response(user_query):
    user_query = preprocess(user_query)
    preprocessed_faqs.append(user_query)
    
    # Convert text to vector using TF-IDF
    vectorizer = TfidfVectorizer().fit_transform(preprocessed_faqs)
    vectors = vectorizer.toarray()
    
    # Calculate cosine similarity - Reshape the vector to be 2D
    cosine_similarities = cosine_similarity(vectors[-1].reshape(1, -1), vectors[:-1])
    preprocessed_faqs.pop()  # Remove the user query from the list
    
    # Find the closest match
    closest_match_idx = np.argmax(cosine_similarities)
    closest_match_score = cosine_similarities[0][closest_match_idx]
    
    # Define a threshold for similarity to ensure relevance
    threshold = 0.5
    if closest_match_score >= threshold:
        return responses[closest_match_idx]
    else:
        return "I'm sorry, I didn't understand your question. Please try again or visit the Department of Justice's official website for more information."

# Main program loop for chatbot interaction
if __name__== "__main__":
    print("Welcome to the Department of Justice Virtual Assistant. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Thank you for using the Department of Justice Virtual Assistant. Goodbye!")
            break
        print("Bot:", chatbot_response(user_input))
