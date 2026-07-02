# Task 3: Basic Chatbot

responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello!",
    "how are you": "I'm doing well, thank you!",
    "bye": "Goodbye! Have a great day!"
}

print("Basic Chatbot (type 'bye' to exit)")
while True:
    msg = input("You: ").strip().lower()
    if msg in responses:
        print("Bot:", responses[msg])
        if msg == "bye":
            break
    else:
        print("Bot: Sorry, I don't understand that.")
