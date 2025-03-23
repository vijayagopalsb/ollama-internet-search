import subprocess
import json
from internet_search import search_internet

# Function to call Ollama and get the model's response
def ask_ollama(query):
    # Prepare the input for Ollama
    input_data = {
        "model": "internet-assistant",  # Replace with your fine-tuned model name
        "prompt": query
    }
    
    # Call Ollama using subprocess
    result = subprocess.run(
        ["ollama", "run", "internet-assistant", query],
        capture_output=True,
        text=True,  # Use text mode to automatically decode output
        encoding="utf-8"  # Explicitly specify UTF-8 encoding
    )
    
    # Extract the model's response
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return "Error: Unable to get a response from Ollama."

# Function to handle internet-related queries
def handle_query(query):
    # Step 1: Ask Ollama if the query requires internet access
    response = ask_ollama(f"Does the following query require internet access? Query: {query}")
    
    # Step 2: Check the response
    if "yes" in response.lower():
        # Step 3: Fetch data using SerpAPI
        internet_result = search_internet(query)
        
        # Step 4: Pass the fetched data back to Ollama for a final response
        final_response = ask_ollama(f"Here is the data I found: {internet_result}. Answer the user's query: {query}")
        return final_response
    else:
        # Step 5: If no internet access is needed, return Ollama's response directly
        return ask_ollama(query)

# Example usage
user_query = "What is the current weather in New York?"
response = handle_query(user_query)
# print(response)