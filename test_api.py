
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
print(f"API Key present: {bool(api_key)}")
if api_key:
    print(f"Key start: {api_key[:5]}...")

genai.configure(api_key=api_key)

try:
    print("Testing gemini-1.5-flash...")
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Say hello in json format: {'message': 'hello'}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"gemini-1.5-flash failed: {e}")
    try:
        print("Testing gemini-pro...")
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Say hello in json format: {'message': 'hello'}")
        print(f"Response: {response.text}")
    except Exception as e2:
        print(f"gemini-pro failed: {e2}")
