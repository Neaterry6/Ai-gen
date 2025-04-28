from transformers import pipeline

# Load Local LLM (Self-hosted, No API Key Needed)
chat_model = pipeline("text-generation", model="EleutherAI/gpt-j-6B")

def chat_response(user_input):
    """Generate chatbot response based on user input"""
    response = chat_model(user_input, max_length=100)
    return response[0]["generated_text"]
