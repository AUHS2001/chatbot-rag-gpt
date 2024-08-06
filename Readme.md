# RAG Chatbot Setup with GPT

# Prerequisites
- Ensure that you have VSCode and Python installed on your machine.

# Setup
- Open the project folder in VSCode.
- Create a Python virtual environment using the following commands in the terminal:
	For Linux:
		python3 -m venv env
		source env/bin/activate
		
	For Windows:
		python -m venv env
		env\Scripts\activate
- Install the required dependencies by executing "pip install -r requirements.txt" in the terminal

# Requirements
-Create a .env File:
	In the root of your project directory, create a file named .env.

	Add your API keys to this file:
		OPENAI_API_KEY="your_openai_api_key_here"
		PINECONE_API_KEY="your_pinecone_api_key_here"
		
	Make sure to replace "your_openai_api_key_here" and "your_pinecone_api_key_here" with your actual API keys.

# Run
- Launch the project by running "streamlit run main.py" in the terminal
- IThe terminal will display a link. Open this link in your browser to start chatting with the ML Chatbot.