import random  

# List of possible responses
responses = [
    "Yes, definitely!", "No, absolutely not.", "Ask again later.",
    "It is certain.", "Very doubtful.", "Better not tell you now.",
    "Signs point to yes.", "My sources say no."
]

print("🎱 Welcome to the Magic 8-Ball! 🎱")

while True:
    question = input("\nAsk a yes/no question (or type 'quit' to exit): ").strip()
    
    if question.lower() == "quit":
        print("Goodbye! 👋")
        break

    # Pick a random response
    answer = random.choice(responses)
    print("Magic 8-Ball says:", answer)
