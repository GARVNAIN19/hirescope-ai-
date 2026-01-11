import os
import json
import logging
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import PyPDF2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask App
app = Flask(__name__)

# Configure Gemini AI
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    logger.warning("GEMINI_API_KEY not found in environment variables. Please set it.")

try:
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    logger.error(f"Failed to configure Gemini AI: {e}")

def extract_text_from_pdf(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        logger.error(f"PDF extraction error: {e}")
        return None

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/app')
def analyzer_page():
    return render_template('app.html')

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400
    
    file = request.files['resume']
    job_description = request.form.get('job_description', '').strip()

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Only PDF files are supported"}), 400
    
    if len(job_description) < 50:
         return jsonify({"error": "Job description is too short (min 50 chars)."}), 400

    # Extract text
    resume_text = extract_text_from_pdf(file)
    if not resume_text or len(resume_text) < 50:
        return jsonify({"error": "Could not extract sufficient text from PDF."}), 400

    # List of models to try in order of preference
    # 'gemini-2.5-flash' added per user request (will likely fallback if invalid)
    model_candidates = [
        'gemini-2.5-flash', 
        'gemini-2.0-flash-exp',
        'gemini-1.5-flash',
        'gemini-1.5-pro'
    ]
    
    last_error = None
    
    for model_name in model_candidates:
        try:
            logger.info(f"Attempting analysis with model: {model_name}")
            model = genai.GenerativeModel(model_name)
            
            prompt = f"""
            Act as a Senior Technical Recruiter and Resume Strategist at a top-tier tech firm (Google, Meta, Amazon). 
            Perform a ruthless, deep-dive analysis of the following resume against the provided job description.
            
            Resume Text:
            {resume_text}

            Job Description:
            {job_description}

            Your goal is to provide a uniquely tailored score based ONLY on the evidence in the text. Do not default to generic scores (like 80 or 85). 
            
            Scoring Criteria (Be Strict):
            1. ats_score (0-100): 
               - Calculate based on exact keyword matches from the JD found in the Resume. 
               - Penalize for parsing errors or bad formatting.
            2. content_score (0-100): 
               - 0-50: Vague, passive voice, no metrics ("Responsible for...").
               - 50-75: Some metrics, but generic impact.
               - 75-90: Strong Action + Context + Result (ACR) format.
               - 90-100: Top 1% resume, quantified dollar amounts/percentages, perfect clarity.

            Output must be a pure JSON object with this structure:
            {{
                "ats_score": <int>,
                "content_score": <int>,
                "summary_feedback": "<string_max_2_sentences_direct_and_punchy>",
                "issues_list": [
                    "<string_critical_issue_1>",
                    "<string_critical_issue_2>",
                    "<string_critical_issue_3>",
                    "<string_critical_issue_4>"
                ]
            }}
            
            Important:
            - Vary the scores significantly based on the actual quality. 
            - If the resume is bad, give it a low score (e.g., 30 or 40).
            - The issues_list must be specific (quote the bad text if possible).
            - Respond ONLY with the JSON.
            """

            response = model.generate_content(prompt)
            response_text = response.text.strip()
            
            # Clean up potential markdown formatting
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]

            result_json = json.loads(response_text)
            logger.info(f"Successfully analyzed with {model_name}")
            return jsonify(result_json)

        except Exception as e:
            logger.warning(f"Model {model_name} failed: {e}")
            last_error = e
            continue

    # If all models fail
    logger.error(f"All models failed. Last error: {last_error}", exc_info=True)
    return jsonify({"error": f"AI Analysis Service failed: {str(last_error)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
