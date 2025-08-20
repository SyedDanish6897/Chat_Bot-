import random

print(" Chatbot: Hello! Ask me anything. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print(" Chatbot: Hi there! How can I help you?")
    elif "salman khan" in user_input:
        print(" Chatbot: Salman Khan is a famous Bollywood actor and film producer.")
    elif "your name" in user_input:
        print(" Chatbot: I am your AI assistant ")
    elif "bye" in user_input:
        print(" Chatbot: Goodbye! Have a nice day ")
        break
    else:
        responses = [
            "Hmm, I didn’t get that. Can you rephrase?",
            "Interesting! Tell me more...",
            "I’m not sure about that, but I’ll learn someday."
        ]
        print(" Chatbot:", random.choice(responses))

