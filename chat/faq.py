from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from lib import preprocess

# Preprocessed FAQ questions
faq_questions = [
    "reset password",
    "transfer money",
    "fee wire transfer",
    "account secure"
]
answers = {
    "reset password": "You can reset your password from the login screen...",
    "transfer money": "To transfer funds, log in to your account...",
    "fee wire transfer": "Domestic wire transfers cost $25...",
    "account secure": "Yes, we use industry-standard encryption..."
}

def get_best_match(user_question, faq_questions, answers):
    processed_user_question = preprocess(user_question)
    
    # Vectorize the questions
    vectorizer = TfidfVectorizer().fit(faq_questions)
    faq_vectors = vectorizer.transform(faq_questions)
    user_vector = vectorizer.transform([processed_user_question])
    
    # Calculate cosine similarity
    similarities = cosine_similarity(user_vector, faq_vectors).flatten()
    
    # Get the index of the most similar question
    best_match_index = similarities.argmax()
    
    # Define a similarity threshold (e.g., 0.5)
    if similarities[best_match_index] > 0.5:
        best_question = faq_questions[best_match_index]
        return answers[best_question]
    else:
        return "Sorry, I couldn't find an answer to your question. Please try rephrasing or contact support."

# Example Usage:
user_input = "I need help changing my forgotten password."
response = get_best_match(user_input, faq_questions, answers)
print(f"Chatbot: {response}")
