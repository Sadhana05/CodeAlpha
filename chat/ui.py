# Simple Command-line Chat UI
from lib import preprocess
from faq import get_best_match, faq_questions, answers

print("Chatbot: Hi! Ask me anything about online banking. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    response = get_best_match(user_input, faq_questions, answers)
    print(f"Chatbot: {response}")
