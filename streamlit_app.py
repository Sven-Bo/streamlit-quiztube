import streamlit as st
from helpers.youtube_utils import extract_video_id_from_url, get_transcript_text
from helpers.openai_utils import get_quiz_data
from helpers.quiz_utils import string_to_list, get_randomized_options
from helpers.toast_messages import get_random_toast


st.set_page_config(
    page_title="QuizTube",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Check if user is new or returning using session state.
# If user is new, show the toast message.
if 'first_time' not in st.session_state:
    message, icon = get_random_toast()
    st.toast(message, icon=icon)
    st.session_state.first_time = False

with st.sidebar:
    st.header("👨‍💻 About the Author")
    st.write("""
    **Sven Bosau** is a tech enthusiast, educator, and coder. Driven by passion and a love for sharing knowledge, he's created this platform to make learning more interactive and fun.

    Connect, contribute, or just say hi!
    """)

    st.divider()
    st.subheader("🔗 Connect with Me", anchor=False)
    st.markdown(
        """
        - [🐙 Source Code](https://github.com/Sven-Bo)
        - [🎥 YouTube Channel](https://youtube.com/@codingisfun)
        - [☕ Buy me a Coffee](https://pythonandvba.com/coffee-donation)
        - [🌐 Personal Website](https://pythonandvba.com)
        - [👔 LinkedIn](https://www.linkedin.com/in/sven-bosau/)
        """
    )

    st.divider()
    st.subheader("🏆 Streamlit Hackathon 2023", anchor=False)
    st.write("QuizTube proudly stands as Sven's innovative entry for the Streamlit Hackathon held in September 2023. A testament to the power of imagination and code!")

    st.divider()
    st.write("Made with ♥ in Dresden, Germany")



st.title(":red[QuizTube] — Watch. Learn. Quiz. 🧠", anchor=False)
st.write("""
Ever watched a YouTube video and wondered how well you understood its content? Here's a fun twist: Instead of just watching on YouTube, come to **QuizTube** and test your comprehension!

**How does it work?** 🤔
1. Paste the YouTube video URL of your recently watched video.
2. Enter your [OpenAI API Key](https://platform.openai.com/account/api-keys).
3. Decide on the number of questions you'd love to challenge yourself with.


⚠️ Important: The video **must** have English captions for the tool to work.

Once you've input the details, voilà! Dive deep into questions crafted just for you, ensuring you've truly grasped the content of the video. Let's put your knowledge to the test! 
""")

with st.form("user_input"):
    YOUTUBE_URL = st.text_input("Enter the YouTube video link:", value="https://youtu.be/bcYwiwsDfGE?si=qQ0nvkmKkzHJom2y")
    OPENAI_API_KEY = st.text_input("Enter your OpenAI API Key:", placeholder="sk-XXXX", type='password')
    NUMBER_OF_QUESTIONS = st.number_input("Choose the number of questions:", min_value=2, max_value=10, value=5)
    submitted = st.form_submit_button("Craft my quiz!")

if submitted or ('quiz_data_list' in st.session_state):
    if not YOUTUBE_URL:
        st.info("Please provide a valid YouTube video link. Head over to [YouTube](https://www.youtube.com/) to fetch one.")
        st.stop()
    elif not OPENAI_API_KEY:
        st.info("Please fill out the OpenAI API Key to proceed. If you don't have one, you can obtain it [here](https://platform.openai.com/account/api-keys).")
        st.stop()
        
    with st.spinner("Crafting your quiz...🤓"):
        if submitted:
            video_id = extract_video_id_from_url(YOUTUBE_URL)
            video_transcription = get_transcript_text(video_id)
            quiz_data_str = get_quiz_data(video_transcription, NUMBER_OF_QUESTIONS, OPENAI_API_KEY)
            st.session_state.quiz_data_list = string_to_list(quiz_data_str)

            if 'user_answers' not in st.session_state:
                st.session_state.user_answers = [None for _ in st.session_state.quiz_data_list]
            if 'correct_answers' not in st.session_state:
                st.session_state.correct_answers = []
            if 'randomized_options' not in st.session_state:
                st.session_state.randomized_options = []

            for q in st.session_state.quiz_data_list:
                options, correct_answer = get_randomized_options(q[1:])
                st.session_state.randomized_options.append(options)
                st.session_state.correct_answers.append(correct_answer)

        with st.form(key='quiz_form'):
            st.subheader("🧠 Quiz Time: Test Your Knowledge!")
            for i, q in enumerate(st.session_state.quiz_data_list):
                options = st.session_state.randomized_options[i]
                default_index = st.session_state.user_answers[i] if st.session_state.user_answers[i] is not None else 0
                response = st.radio(q[0], options, index=default_index)
                st.session_state.user_answers[i] = options.index(response)

            results_submitted = st.form_submit_button(label='Unveil My Score!')

            if results_submitted:
                score = sum([ua == st.session_state.randomized_options[i].index(ca) for i, (ua, ca) in enumerate(zip(st.session_state.user_answers, st.session_state.correct_answers))])
                st.success(f"Your score: {score}/{len(st.session_state.quiz_data_list)}")

                if score == len(st.session_state.quiz_data_list):  # Check if all answers are correct
                    st.balloons()
                else:
                    incorrect_count = len(st.session_state.quiz_data_list) - score
                    if incorrect_count == 1:
                        st.warning(f"Almost perfect! You got 1 question wrong. Let's review it:")
                    else:
                        st.warning(f"Almost there! You got {incorrect_count} questions wrong. Let's review them:")

                for i, (ua, ca, q, ro) in enumerate(zip(st.session_state.user_answers, st.session_state.correct_answers, st.session_state.quiz_data_list, st.session_state.randomized_options)):
                    with st.expander(f"Question {i + 1}", expanded=False):
                        if ro[ua] != ca:
                            st.info(f"Question: {q[0]}")
                            st.error(f"Your answer: {ro[ua]}")
                            st.success(f"Correct answer: {ca}")