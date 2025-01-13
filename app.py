from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Instantiate OpenAI client
client = OpenAI(api_key=api_key)

# Create Flask app
app = Flask(__name__)

# Route to display the home page with a button
@app.route("/", methods=["GET", "POST"])
def index():
    response = None

    if request.method == "POST":
        try:
            user_prompt = request.form.get("prompt")
            # Call the OpenAI API using your preferred method
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "developer", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )
            response = completion.choices[0].message.content
        except Exception as e:
            response = f"Error: {str(e)}"

    return render_template("index.html", response=response)

# Run the Flask app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
