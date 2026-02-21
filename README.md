# Guided Component Architect - MyAssignment

Live Demo  https://assignment-bciyxmyfpn6nrzagsesjxm.streamlit.app/

An AI-powered system that generates Angular/HTML components

Built using:
- Streamlit
- LangChain
- Groq (LLaMA 3.1)
- Python

---

## Features

- Generate UI components from natural language
- Enforces strict design system (JSON-based tokens)
- Extracts only valid HTML output
- Save generated code as `.tsx`
- Runs locally using Streamlit

---

# Setup Instructions

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Create `.env` File

Inside the project root folder create a file named:

```
.env
```

Add this inside it:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## How to Get Groq API Key

1. Go to: https://console.groq.com
2. Login / Sign up
3. Navigate to **API Keys**
4. Click **Create API Key**
5. Copy the generated key
6. Paste it inside your `.env` file

---

## Run the Application

```bash
streamlit run main.py
```

The app will open automatically in your browser.

---

# Project Structure

```
├── main.py
├── json_input.json
├── requirements.txt
├── README.md
└── .env
```



# How It Works

1. User enters a prompt.
2. LLM generates an HTML component.
3. System extracts only clean HTML.
4. Validates classes against predefined JSON design system.
5. Displays final valid code.
6. Optionally saves or downloads as `.tsx`.

---

# 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- Groq LLaMA 3.1
- JSON-based Design System

---

# Author

Lucky Tiwari

---

Enjoy Building
