

from ollama_integration import handle_query
def main():
    print("Welcome to the Internet-Enabled AI Assistant!")
    while True:
        query = input("\nEnter your query (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        response = handle_query(query)
        print(f"\nAI: {response}")

if __name__ == "__main__":
    main()