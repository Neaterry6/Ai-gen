from flask import Flask, request, jsonify
import os
from image_generator import generate_image

app = Flask(__name__)

@app.route("/generate-image", methods=["POST"])
def generate_image_api():
    """Handles image generation via Local AI"""
    prompt = request.json.get("prompt", "A futuristic city at sunset")
    
    if not prompt:
        return jsonify({"error": "❌ No prompt provided!"}), 400

    image_path = generate_image(prompt)
    return jsonify({"image": image_path})

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 5000))  # ✅ Uses assigned port or defaults to 5000
    app.run(host="0.0.0.0", port=PORT, debug=True)
