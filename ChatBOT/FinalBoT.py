import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from ChatBoT import Engine
nltk.download('punkt')
nltk.download('stopwords')

class DOJVirtualAssistant:
    def __init__(self):
        self.faqs = [
            "What services does the Department of Justice provide?",
            "How can I file a complaint?",
            "Where can I find information on civil rights?",
            "How do I report a crime?",
            "What are the responsibilities of the Department of Justice?",
            "What is the mission of the Department of Justice?",
            "How can I contact the Department of Justice?",
            "Where can I find information about the Freedom of Information Act (FOIA)?",
            "What is the Office of Justice Programs?",
            "How do I find a list of DOJ press releases?"
        ]
        self.chatbot = Engine()
        self.chatbot.AgentToolMaster()

        self.responses = [
            "The Department of Justice provides legal advice to the government, represents the state in legal matters, and ensures the enforcement of the law.",
            "You can file a complaint by visiting our official website and following the complaint submission process.",
            "Information on civil rights can be found under the 'Civil Rights' section on our website.",
            "To report a crime, please visit the 'Report a Crime' section on our website or contact your local law enforcement agency.",
            "The Department of Justice is responsible for upholding the rule of law, prosecuting federal cases, and ensuring justice is served.",
            "The mission of the Department of Justice is to enforce the law and defend the interests of the United States according to the law, ensure public safety, provide federal leadership in preventing and controlling crime, seek just punishment for those guilty of unlawful behavior, and ensure fair and impartial administration of justice for all Americans.",
            "You can contact the Department of Justice by visiting our 'Contact Us' page on the official website, where you can find phone numbers, email addresses, and mailing addresses for various offices and services.",
            "Information about the Freedom of Information Act (FOIA) can be found on the 'FOIA' page of the Department of Justice's website, including details on how to file a FOIA request.",
            "The Office of Justice Programs (OJP) provides federal leadership, grants, training, technical assistance, and other resources to improve the nation’s capacity to prevent and reduce crime, assist victims, and enforce state, local, and tribal laws.",
            "A list of DOJ press releases can be found in the 'News' section of the Department of Justice's website, where you can filter by date and topic."
        ]
        self.closest_match_score =0

    def preprocess(self, text):
        text = text.lower()
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word.isalnum()]
        tokens = [word for word in tokens if word not in stopwords.words('english')]
        return " ".join(tokens)

    def chatbot_response(self, user_query):
        self.actualquery = user_query
        preprocessed_faqs = [self.preprocess(faq) for faq in self.faqs]
        user_query = self.preprocess(user_query)
        preprocessed_faqs.append(user_query)    
        vectorizer = TfidfVectorizer().fit_transform(preprocessed_faqs)
        vectors = vectorizer.toarray()
        cosine_similarities = cosine_similarity(vectors[-1].reshape(1, -1), vectors[:-1])
        preprocessed_faqs.pop()
        closest_match_idx = np.argmax(cosine_similarities)
        self.closest_match_score = cosine_similarities[0][closest_match_idx]
        threshold = 0.5
        if self.closest_match_score >= threshold:
            return self.responses[closest_match_idx]
        else:
            output = self.chatbot.complete(self.actualquery)
            return output

    def start_chat(self):
        print("Welcome to the Department of Justice Virtual Assistant. How can I assist you today?")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Bot: Thank you for using the Department of Justice Virtual Assistant. Goodbye!")
                break
            print("Bot:", self.chatbot_response(user_input))
        
# assistant = DOJVirtualAssistant() This will make it work here
# assistant.start_chat()