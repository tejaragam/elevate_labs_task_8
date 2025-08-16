print("Chatbot: Hello! How can I help you today?")
while True:
    user_input = input("You: ").strip().lower()
    
    if user_input in ["hi", "hello"]:
        print("Chatbot: Hi there! What can I do for you?")
    elif user_input in ["how are you?", "how are you"]:
        print("Chatbot: I'm a bot, but I'm doing well! How are you?")
    elif user_input in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a nice day.")
        break
    elif "name" in user_input:
        print("Chatbot: I'm a rule-based chatbot created in Python.")
    elif "help" in user_input:
        print("Chatbot: Sure! Ask me about greetings, my name, or say bye to exit.")
    else:
        print("Chatbot: Sorry, I didn't understand that. Could you rephrase?")

