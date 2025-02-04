import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai._client import OpenAI

app = Flask(__name__)
CORS(app)

# Replace with your DeepSeek API key and endpoint
DEEPSEEK_API_KEY = "CREATE API KEY FORM THE FOLLOWING URL"
DEEPSEEK_API_URL = "https://openrouter.ai/api/v1"


def refine_prompt_with_deepseek(user_input):
    """
    Uses DeepSeek API to refine user input into a structured prompt.
    """
    system_message = (
        "You are an assistant who improves prompts for AI tools."
        "Your task is to rewrite and enhance the input text so AI can understand it better and give an accurate response."
        "Do not change the meaning of the input and do not add extra topics, but make it more clear and concise."
        "Format the response as a paragraph of two or three items, without emojis or special characters like quotations or stars."
        "Important: Do not answer questions—only refine the prompt."
    )

    # Initialize the OpenAI client with DeepSeek API
    client = OpenAI(
        base_url=DEEPSEEK_API_URL,
        api_key=DEEPSEEK_API_KEY,
    )

    try:
        # Call DeepSeek's API to refine the input
        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",  # Replace with the appropriate DeepSeek model
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_input}
            ],
            temperature=0.1,  # Low randomness for consistent results
        )
        # Extract the response content
        print(completion)
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error refining prompt: {str(e)}"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_prompt():
    data = request.get_json()
    user_input = data.get('prompt', '').strip()
    refined_prompt = refine_prompt_with_deepseek(user_input)
    return jsonify({'refined_prompt': refined_prompt})

if __name__ == '__main__':
    app.run(debug=True)



