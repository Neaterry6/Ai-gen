from flask import Flask, request, jsonify
import os
from chat_ai import chat_response
from image_generator import generate_image

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("text", "")
    response = chat_response(user_input)
    return jsonify({"response": response})

@app.route("/generate-image", methods=["POST"])
def generate_image_api():
    prompt = request.json.get("prompt", "A futuristic city at sunset")
    image_path = generate_image(prompt)
    return jsonify({"image": image_path})

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT, debug=True
