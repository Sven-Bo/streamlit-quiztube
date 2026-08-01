# 🧠 QuizTube: Transforming YouTube Videos into Quizzes with Streamlit

QuizTube offers an innovative approach to create interactive quizzes from YouTube video captions. By extracting captions using the [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) and subsequently processing the text with OpenAI's LLM, `QuizTube` serves as a powerful tool for enhancing video content interaction.

## Video Tutorial
[![YouTube Video](https://img.youtube.com/vi/xCsAbe5MVLc/0.jpg)](https://youtu.be/xCsAbe5MVLc)

## Website Link
👉 Check out the app here: https://quiztube.streamlit.app/

## How It Works

1. **Caption Extraction:** Using the [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api), captions are extracted from a given YouTube video URL.
2. **Quiz Generation:** The extracted captions are then fed into OpenAI's LLM using [`LangChain Python`](https://python.langchain.com/) with a predefined prompt template. The model generates questions based on the content, turning the video's key points into an interactive quiz.
3. **Streamlit Integration:** The quizzes are seamlessly integrated and displayed in a Streamlit app, providing users with a unique and interactive experience.

This project was developed as an entry for the [Streamlit Hackathon in September 2023](https://streamlit.io/community/llm-hackathon-2023).

## Learn Excel Automation with Python
If this repo helped you, my [Excel Automation Course](https://pythonandvba.com/excel-automation-course/) teaches the full workflow from zero: Python for Excel users, xlwings, pandas and real projects.

Also check out my other [tools and templates](https://pythonandvba.com/solutions).

## Connect with Me
- **YouTube:** [CodingIsFun](https://youtube.com/c/CodingIsFun)
- **Website:** [PythonAndVBA](https://pythonandvba.com)
- **LinkedIn:** [Sven Bosau](https://www.linkedin.com/in/sven-bosau/)
- **Contact:** [Get in Touch](https://pythonandvba.com/contact)
## Support
If you find this project helpful, consider buying me a coffee. 

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://pythonandvba.com/coffee-donation)
