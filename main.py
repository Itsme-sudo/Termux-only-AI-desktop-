from ai_module import interpret_command
from config import IS_TERMUX, SYSTEM

def main():
    print(f"Local AI Assistant (Offline - Termux Safe)")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = interpret_command(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
