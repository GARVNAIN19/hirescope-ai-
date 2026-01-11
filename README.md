# HireScope.AI 🚀

> **AI-Powered Resume Scoring & Career Intelligence Platform**

[![Live Demo](https://img.shields.io/badge/demo-live-green?style=for-the-badge&logo=vercel)](https://hirescope-ai.vercel.app/)
[![Python](https://img.shields.io/badge/python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Gemini AI](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)

**HireScope.AI** is a cutting-edge career tool that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS) and human recruiters. By leveraging Google's **Gemini AI**, it provides deep, contextual feedback, keyword matching, and a ruthless "recruiters-eye" score to help users land more interviews.

---

## 📸 Screenshots


<img width="1350" height="597" alt="Screenshot 2026-01-11 215643" src="https://github.com/user-attachments/assets/7387bd10-120d-4c1d-bb5c-f467de5ff386" />


---

## ✨ Key Features

- **📄 Smart PDF Parsing**: Accurately extracts text from PDF resumes using `PyPDF2`.
- **🤖 AI-Driven Analysis**: Uses **Google Gemini 1.5 Flash** to simulate a Senior Recruiter's critique.
- **🎯 ATS Match Scoring**: Calculates a match score (0-100%) based on Job Description keywords.
- **🔍 Deep Insights**: Provides actionable feedback on:
  - Missing keywords & skills.
  - Formatting & structure issues.
  - Quantification of achievements (impact metrics).
- **🎨 Premium UI/UX**: Built with **Tailwind CSS** and **GSAP** for smooth, glassmorphic animations and a modern feel.

---

## 🛠️ Tech Stack

- **Frontend**: HTML5, Tailwind CSS (CDN), GSAP (Animations), FontAwesome.
- **Backend**: Python, Flask (Web Framework).
- **AI Engine**: Google Generative AI (Gemini API).
- **Utilities**: `PyPDF2` (PDF Processing), `python-dotenv` (Config).
- **Deployment**: Vercel (recommended) or Render.

---

## 🚀 Local Installation & Setup

Follow these steps to run HireScope.AI locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com/GARVNAIN19/hirescope-ai.git
cd hirescope-ai
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a file named `.env` in the root directory and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
```
> **Note**: You can get a free API key from [Google AI Studio](https://aistudio.google.com/).

### 5. Run the Application
```bash
python app.py
```
The app will start at `http://localhost:5000`.

---

## 🌐 Deployment (Vercel)

This project is configured for easy deployment on **Vercel**.

1. **Fork/Clone** this repo to your GitHub.
2. Login to [Vercel](https://vercel.com/) and **Import** your repository.
3. In the Vercel Project Settings, add your Environment Variable:
   - Key: `GEMINI_API_KEY`
   - Value: `Address to your API Key`
4. Deploy! 🚀

*(Configuration files `vercel.json` and `requirements.txt` are already included).*

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<center>
  <sub>Built with ❤️ by Garv Nain</sub>
</center>
