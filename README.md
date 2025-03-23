# ollama-internet-search
Ollama Internet Search is a powerful tool designed to enable seamless internet search capabilities by integrating with the Searp API. This project allows users to perform real-time internet searches, retrieve relevant information, and process the results efficiently.


## Setting Up the Searp API Key
To use the Ollama Internet Search project, you need to register for a Searp API key and configure it in the project. Follow these steps:

#### Step 1: Get a Searp API Key
1. Go to the Searp API website (or the official provider’s website).

2. Sign up for an account if you don’t already have one.

3. Navigate to the API Key section in your account dashboard.

4. Generate a new API key or copy your existing key.

#### Step 2: Install Dependencies
1. serpapi:
Used to interact with the SerpAPI service for fetching real-time data from search engines like Google.
<pre>
    pip install google-search-results
</pre>

2. python-dotenv:
Used to load environment variables from a .env file.
<pre>
    pip install python-dotenv
</pre>

#### Step 3: Install Ollama
1. Download and install Ollama from the official website: [Ollama Installation Guide.](https://github.com/ollama/ollama)

2. Pull the Llama 3 model:

<pre>
    ollama pull llama3
</pre>

#### Step 4: Custom Modelfile

**Instructions**
1. Open your terminal.

2. Navigate to the desired directory on your computer where you want to create the Modelfile.

3. Create a file named Modelfile (without any file extension).

4. Add the following content to the Modelfile.

<pre>
    FROM llama3

    # System prompt
    SYSTEM """
    You are an AI assistant capable of accessing the internet to answer questions. If a question requires internet access, explain that you will search for the information.
    """

    # Add example conversations
    MESSAGE user "What is the current weather in New York?"
    MESSAGE assistant "I will search the internet to find the current weather in New York."

    MESSAGE user "Who is the CEO of Tesla?"
    MESSAGE assistant "I will look up the current CEO of Tesla."

    # More Examples...

    # Mathematical Problems
    MESSAGE user "What is 15 + 27?"
    MESSAGE assistant "15 + 27 equals 42."

    MESSAGE user "Solve for x: 2x + 5 = 15."
    MESSAGE assistant "To solve for x, subtract 5 from both sides: 2x = 10. Then divide both sides by 2: x = 5."

    # General Knowledge
    MESSAGE user "Who was the first president of the United States?"
    MESSAGE assistant "The first president of the United States was George Washington."

    MESSAGE user "What is the chemical formula for water?"
    MESSAGE assistant "The chemical formula for water is H2O."

    # Internet-Related Queries
    MESSAGE user "What is the current weather in New York?"
    MESSAGE assistant "I will search the internet to find the current weather in New York."

    MESSAGE user "Who is the current CEO of Tesla?"
    MESSAGE assistant "I will look up the current CEO of Tesla."

    # Fine-tuning parameters
    PARAMETER temperature 0.7
    PARAMETER num_ctx 512
</pre>

#### Step 5: Create the Custom Model using Ollama
1. Create the custom model using Ollama

<pre>
    ollama create internet-assistant -f ./Modelfile
</pre>

2. Run the custom model

<pre>
    ollama run internet-assistant
</pre>

#### Step 6: Testing the Assistant
1. Ask a question

<pre>
    User: What is 15 + 27?
    AI: 15 + 27 equals 42.
</pre>
2. Test internet-related queries

<pre>
    User: What is the current weather in New York?
    AI: I will search the internet to find the current weather in New York.
</pre>

## Adding More Examples

**Create the dataset.jsonl File**

<pre>
    {"question": "What is 15 + 27?", "answer": "15 + 27 equals 42."}
    {"question": "Calculate 45 divided by 9.", "answer": "45 divided by 9 equals 5."}
    {"question": "What is 12 multiplied by 8?", "answer": "12 multiplied by 8 equals 96."}
    {"question": "Solve for x: 2x + 5 = 15.", "answer": "To solve for x, subtract 5 from both sides: 2x = 10. Then divide both sides by 2: x = 5."}
    {"question": "Simplify the expression: 3(x + 4) - 2x.", "answer": "Simplifying the expression: 3(x + 4) - 2x = 3x + 12 - 2x = x + 12."}
    {"question": "What is the derivative of x^2 + 3x + 2?", "answer": "The derivative of x^2 + 3x + 2 is 2x + 3."}
    {"question": "What is the area of a circle with a radius of 5?", "answer": "The area of a circle with a radius of 5 is 78.54 square units (using π ≈ 3.1416)."}
    {"question": "Who was the first president of the United States?", "answer": "The first president of the United States was George Washington."}
    {"question": "What is the chemical formula for water?", "answer": "The chemical formula for water is H2O."}
    {"question": "What is the capital of France?", "answer": "The capital of France is Paris."}
    {"question": "What is the current weather in New York?", "answer": "I will search the internet to find the current weather in New York."}
    {"question": "Who is the current CEO of Tesla?", "answer": "I will look up the current CEO of Tesla."}
    {"question": "What is the population of India?", "answer": "I will search the internet to find the latest population data for India."}
    {"question": "How tall is Mount Everest?", "answer": "Mount Everest is 8,848.86 meters (29,031.7 feet) tall."}
    {"question": "What are the latest headlines in technology?", "answer": "I will search the internet to find the latest headlines in technology."}
    {"question": "What is the current stock price of Apple?", "answer": "I will look up the current stock price of Apple."}
</pre>

**Save the file as dataset.jsonl in --Modelfile-- directory.**


#### Final Step to run the python script
<pre>
    python main.py
</pre>


#### Contributions
Contributions are welcome! If you'd like to contribute to this project, please follow these steps

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Submit a pull request with a detailed description of your changes.

**License**
This project is licensed under the GPL-3.0.1 License. See the [LICENSE](https://github.com/vijayagopalsb/ollama-internet-search?tab=GPL-3.0-1-ov-file) file for details.