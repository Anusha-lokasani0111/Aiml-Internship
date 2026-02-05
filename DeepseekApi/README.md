# 💬 DeepSeek Chat Assistant (Using OpenRouter API)

A simple AI-powered chat application built using **Streamlit** and **DeepSeek model via OpenRouter API**.  
This application allows users to ask questions and receive AI-generated responses in real-time.

-----------------------------------------------------

##  Features

- ✅ DeepSeek AI Integration (via OpenRouter)
- ✅ Interactive Chat UI using Streamlit
- ✅ Environment Variable Security (.env file)
- ✅ Error Handling & Logging
- ✅ Multi-message Chat Memory
- ✅ Free AI API Usage

------------------------------------------------------

##  Technologies Used

- Python
- Streamlit
- OpenRouter API
- DeepSeek Chat Model
- Requests Library
- .env
- Logging

-----------------------------------------------------

##  Project Structure
DeepseekApi
│
├── app.py  # Streamlit User Interface
├── deepseek_api.py # API Integration Logic
├── .env # API Key Storage
└── error.log # Error Logs (Auto Generated)

##  Installation & Setup
# 1. Install Dependencies
pip install streamlit requests python-dotenv

# 2. Create `.env` File
 OPENROUTER_API_KEY=your_api_key_here

 # 3. Run Application 
 streamlit run app.py

 # 4. Open Browser

http://localhost:8501


------------------------------------------------------

##  How to Get OpenRouter API Key

1. Visit: https://openrouter.ai  
2. Sign up / Login  
3. Go to API Keys section  
4. Generate API key  
5. Add it to `.env` file  

------------------------------------------------------

## How It Works

### ✔ app.py
- Creates Streamlit UI  
- Accepts user input  
- Displays chat messages  
- Calls AI API  

------------------------------------------------------

### ✔ deepseek_api.py
- Connects to OpenRouter API  
- Sends user messages  
- Receives AI responses  
- Handles API errors  

------------------------------------------------------

##  Error Handling

Application handles:

- API timeout errors  
- Connection failures  
- Invalid API responses  
- Logs errors into `error.log`  

-----------------------------------------------------

## 🔮 Future Enhancements

- Voice input support  
- Chat history download  
- Multi-model selection  
- Database integration  
- UI improvements  

-------------------------------------------------------

## Use Case

This project demonstrates:

- AI API integration  
- Streamlit UI development  
- Secure API key management  
- Chatbot implementation  

## Author

Developed by: Anusha Lokasani


