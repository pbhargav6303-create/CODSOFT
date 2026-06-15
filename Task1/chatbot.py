while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hello! How can I help you?")
    elif user == "how are you":
        print("Bot: I am fine. Thank you!")
    elif user == "what is your name":
        print("Bot: I am a CodSoft AI chatbot.")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand. Please try another question.")
