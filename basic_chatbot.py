"""Basic rule-based chatbot."""

RESPONSES = {
    "hello": "Hi!",
    "hi": "Hello!",
    "how are you": "I'm fine, thanks! How can I help you today?",
    "what is your name": "I am a simple Python chatbot.",
    "bye": "Goodbye! Have a nice day!",
}


def get_response(message):
    normalized = message.strip().lower()
    return RESPONSES.get(normalized, "Sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'.")


def main():
    print("Basic Chatbot")
    print("Type a message and press Enter. Type 'bye' to exit.")

    while True:
        message = input("You: ")
        if not message.strip():
            continue

        response = get_response(message)
        print("Bot:", response)

        if message.strip().lower() == "bye":
            break


if __name__ == "__main__":
    main()
