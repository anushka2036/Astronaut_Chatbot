# Ollama Chatbot

A simple local chatbot project built with **Python, Ollama, and Streamlit**. It allows you to run and experiment with locally hosted language models without depending entirely on cloud-based APIs.

## Requirements

Before getting started, make sure you have:

* **Python 3.11 or newer**
* **Ollama** installed on your computer
  Download it from [ollama.com](https://ollama.com/)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ThomasJanssen-tech/Ollama-Chatbot.git
cd Ollama-Chatbot
```

### 2. Set Up a Virtual Environment

Create an isolated Python environment for the project:

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Project

Open the project folder in **VS Code**, launch the integrated terminal, and run the script you want to test.

### Python Example

```bash
python 1_python_ollama.py
```

### Streamlit Examples

```bash
streamlit run 2_streamlit_example.py
```

```bash
streamlit run 3_chatbot_echo.py
```

### Main Application

To launch the complete chatbot:

```bash
streamlit run app.py
```

After running a Streamlit command, open the local URL displayed in the terminal to access the chatbot in your browser.
