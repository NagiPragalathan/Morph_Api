from flask import Flask, request, jsonify
import openai

# Initialize Flask app
app = Flask(__name__)

# Set up the OpenAI client with the base URL and API key
openai.api_base = 'https://api.red-pill.ai/v1'
openai.api_key = 'sk-lPrp67KbkKz8cojLOk0CvZvFgxGC5oOHRzRMAn6JnbQw8Nkz'

# Define the route for chat completion
@app.route('/chat', methods=['POST'])
def chat_completion():
    try:
        # Get the user input from the request JSON body
        user_input = request.json.get('user_input', '')

        # If user input is empty, return an error
        if not user_input:
            return jsonify({'error': 'user_input is required'}), 400

        # Send a chat completion request to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Use the correct model available in the API
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        # Extract the first response choice
        chat_response = response['choices'][0]['message']['content']

        # Return the chat response as JSON
        return jsonify({'response': chat_response,  'block': 123}), 200


    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
