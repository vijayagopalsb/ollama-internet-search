from serpapi import GoogleSearch

import os
from dotenv import load_dotenv

def search_internet(query):
    
    # Please Read README file for instructions
    # Access the SERP API key
    SERP_API_KEY = serp_api_key()

    params = {
        "q": query,
        "api_key": SERP_API_KEY  # Replace with your actual API key 
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    # Print the entire response for debugging
    # print("Full SerpAPI Response:", results)
    
    # Check if the weather section exists
    if "weather" in results:
        weather = results["weather"]
        return f"The current weather in {weather.get('location', 'New York')} is {weather.get('temperature', 'unknown')}°F and {weather.get('condition', 'unknown')}."
    
    # Check for organic_results (fallback)
    elif "organic_results" in results and results["organic_results"]:
        first_result = results["organic_results"][0]
        return f"Weather information from {first_result.get('source', 'a source')}: {first_result.get('snippet', 'No details available.')}"
    
    # Default response if no relevant data is found
    return "No weather data found in the response."

def serp_api_key():
    # Load environment variables from .env file
    load_dotenv()

    # Access the SERP API key
    return os.getenv("SERP_API_KEY")
    


# Example usage
query = "current weather in New York"
result = search_internet(query)
# print("Result:", result)