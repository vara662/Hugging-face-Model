**Hugging face_model**

## Intelligent AI Assistant

Nexa AI is an intelligent conversational AI assistant developed using Python, Streamlit, and the Hugging Face Inference API. The application provides a simple and interactive chat interface where users can ask questions and receive AI-generated responses in real time.

The project is designed to demonstrate the integration of Large Language Models with a web-based user interface. Nexa AI can assist users with programming, education, artificial intelligence, technology, general knowledge, creative ideas, and everyday questions.

The assistant also supports multiple communication styles, including English, Tamil, and Tanglish, making interactions more natural and accessible.

---

## Features

* Interactive conversational AI interface
* Real-time AI-generated responses
* Support for general knowledge questions
* Programming assistance
* Educational support
* Artificial Intelligence and technology guidance
* Creative ideas and project suggestions
* Tamil, Tanglish, and English language support
* Chat history management
* Clear chat functionality
* Quick suggestion buttons
* User-friendly Streamlit interface
* Secure API token management using environment variables

---

## Technologies Used

* Python
* Streamlit
* Hugging Face Hub
* Hugging Face Inference API
* Groq Provider
* GPT-OSS 120B Model
* Python Dotenv

---

## Project Structure

```text
Nexa-AI/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── venv/
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Nexa-AI.git
```

### 2. Navigate to the Project Folder

```bash
cd Nexa-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project directory.

Add your Hugging Face API token:

```env
HF_TOKEN=your_huggingface_token_here
```

Do not share or upload your API token to public repositories.

---

## Running the Application

Run the following command:

```bash
streamlit run app.py
```

After running the command, Streamlit will start a local server and provide a URL in the terminal. Open the URL in your browser to access Nexa AI.

---

## How It Works

1. The user enters a question through the Streamlit chat interface.
2. The question is stored in the session chat history.
3. The application sends the conversation to the Hugging Face Inference API.
4. The AI model processes the request.
5. The generated response is returned to the application.
6. Nexa AI displays the response in the chat interface.

---

## AI Model

Nexa AI uses the following model configuration:

```text
Provider: Groq
Model: openai/gpt-oss-120b
```

The model is accessed through the Hugging Face Inference Client.

---

## Requirements

The project requires the following Python libraries:

```text
streamlit
huggingface_hub
python-dotenv
transformers
```

---

## Future Enhancements

* Voice input and voice responses
* Document and PDF analysis
* Image understanding
* Chat export functionality
* Multiple AI model selection
* Dark mode support
* Personalized AI responses
* Multi-language translation
* User authentication
* Cloud deployment

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* Python programming
* API integration
* Large Language Models
* Conversational AI
* Streamlit web development
* Environment variable management
* Session state management
* Hugging Face technologies
* AI application development

---

## Conclusion

Nexa AI demonstrates how modern Artificial Intelligence technologies can be integrated into a web application to create an interactive and intelligent virtual assistant. The project combines Python, Streamlit, and Hugging Face technologies to provide a simple, responsive, and user-friendly conversational experience.

The application can be expanded further with advanced AI capabilities and additional features, making it a scalable foundation for future AI assistant development.

---

## Author

Varalakshmi K
