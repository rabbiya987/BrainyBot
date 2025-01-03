
---

# **BrainyBot: An AI-Powered Chatbot** 🤖✨  

BrainyBot is a Flask-based chatbot application that uses the Cohere API to generate dynamic, context-aware AI responses. This project combines a robust backend with an elegant frontend to create an engaging chat experience for users.  

## 🚀 **Features**  
- **AI-Driven Responses**: Powered by the Cohere API, offering intelligent and realistic conversations.  
- **Interactive Interface**: Clean, responsive, and user-friendly chat UI.  
- **Customizable AI Parameters**: Fine-tune behavior like temperature and max tokens for tailored responses.  
- **Secure Communication**: CSRF protection implemented using Flask-WTF.  
- **Lightweight and Fast**: Built on Flask for efficient server-side processing.  

## 🛠️ **Tech Stack**  
- **Backend**: Flask  
- **AI Model**: Cohere API (Command Model)  
- **Frontend**: HTML, CSS, JavaScript  
- **Security**: Flask-WTF for form validation and CSRF protection  

## 📖 **How It Works**  
1. **User Input**: Users enter messages via the chat interface.  
2. **AI Processing**: Flask routes the input to the Cohere API, which generates a response using natural language processing.  
3. **Chat History**: Conversations are dynamically displayed on the UI, stored temporarily for seamless interaction.  

## 📂 **Project Structure**  
```
BrainyBot/
├── app.py              # Flask application logic
├── templates/
│   └── temp.html       # Frontend chat interface
├── static/             # CSS and other static files
└── README.md           # Documentation
```  

## 🖥️ **Setup Instructions**  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repo-link.git  
   cd BrainyBot  
   ```  
2. Add your Cohere API key to your environment variables:  
   ```bash  
   export Cohere_API='your-api-key'  
   ```  
3. Run the application:  
   ```bash  
   python app.py  
   ```  
4. Open the app in your browser:  
   - Navigate to `http://127.0.0.1:5000/`  

## 🌟 **Contributing**  
Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.  

