import streamlit as st
import random

# 1. Expanded Quiz Pool (10 unique questions)
QUESTION_POOL = [
    {"question": "Which Indian state is known as the 'Land of Five Rivers'?", "options": ["Punjab", "Haryana", "Uttar Pradesh", "Bihar"], "answer": "Punjab"},
    {"question": "Which state is the largest by area in India?", "options": ["Madhya Pradesh", "Maharashtra", "Rajasthan", "Uttar Pradesh"], "answer": "Rajasthan"},
    {"question": "In which northeastern state would you find the living root bridges?", "options": ["Assam", "Meghalaya", "Nagaland", "Mizoram"], "answer": "Meghalaya"},
    {"question": "Which southern state has the longest coastline in India?", "options": ["Tamil Nadu", "Kerala", "Andhra Pradesh", "Karnataka"], "answer": "Andhra Pradesh"},
    {"question": "Which state is the leading producer of tea in India?", "options": ["West Bengal", "Kerala", "Assam", "Tamil Nadu"], "answer": "Assam"},
    {"question": "Which Indian state is known as 'God's Own Country'?", "options": ["Karnataka", "Kerala", "Goa", "Himachal Pradesh"], "answer": "Kerala"},
    {"question": "Which state is famous for the 'Gir National Park', the home of Asiatic Lions?", "options": ["Gujarat", "Rajasthan", "Madhya Pradesh", "Maharashtra"], "answer": "Gujarat"},
    {"question": "Which Indian state surrounds Bangladesh on three sides?", "options": ["West Bengal", "Meghalaya", "Tripura", "Mizoram"], "answer": "Tripura"},
    {"question": "Which state is known as the 'Spice Garden of India'?", "options": ["Andhra Pradesh", "Karnataka", "Kerala", "Tamil Nadu"], "answer": "Kerala"},
    {"question": "The classical dance form 'Kathakali' originated in which state?", "options": ["Tamil Nadu", "Andhra Pradesh", "Karnataka", "Kerala"], "answer": "Kerala"}
]

# 2. Configure the page
st.set_page_config(page_title="Indian States Quiz", page_icon="🇮🇳", layout="centered")
st.title("🇮🇳 Indian States Trivia Quiz")
st.write("Test your knowledge about the incredible states of India!")
st.markdown("---")

# 3. Initialize Session State variables
if "quiz_questions" not in st.session_state:
    # Randomly select 5 unique questions from the pool of 10 for this session
    st.session_state.quiz_questions = random.sample(QUESTION_POOL, 5)

if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_over" not in st.session_state:
    st.session_state.quiz_over = False
if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = []

# Use the randomly selected questions for the active quiz session
active_questions = st.session_state.quiz_questions

# 4. Quiz Logic
if not st.session_state.quiz_over:
    current_index = st.session_state.current_q
    q_item = active_questions[current_index]
    
    # Display progress
    st.subheader(f"Question {current_index + 1} of {len(active_questions)}")
    st.progress((current_index) / len(active_questions))
    
    # Display Question
    st.write(f"### {q_item['question']}")
    
    # Radio buttons for options
    user_choice = st.radio("Choose your answer:", q_item["options"], key=f"q_{current_index}")
    
    # Submit Button
    if st.button("Submit Answer"):
        if user_choice == q_item["answer"]:
            st.session_state.score += 1
            st.toast("✨ Brilliant! That's correct!", icon="🎉")
        else:
            st.session_state.wrong_answers.append({
                "question": q_item["question"],
                "your_answer": user_choice,
                "correct_answer": q_item["answer"]
            })
            st.toast("Oh close! Keep going!", icon="💪")
        
        if current_index + 1 < len(active_questions):
            st.session_state.current_q += 1
            st.rerun()
        else:
            st.session_state.quiz_over = True
            st.rerun()

# 5. Scorecard / End Screen
else:
    st.balloons()
    st.header("🏆 Quiz Completed!")
    
    final_score = st.session_state.score
    total_q = len(active_questions)
    
    if final_score == total_q:
        st.success(f"🌟 **Perfect Score! {final_score}/{total_q}** — You are an absolute expert on Indian Geography! Incredible job!")
    elif final_score >= 3:
        st.info(f"👍 **Great Job! {final_score}/{total_q}** — Fantastic effort! You really know your way around the states.")
    else:
        st.warning(f"📚 **Score: {final_score}/{total_q}** — A wonderful attempt! Every mistake is just a step closer to mastering Indian geography. Keep learning!")
        
    # Review Wrong Answers Section
    if st.session_state.wrong_answers:
        st.markdown("### 🔍 Answer Review")
        st.write("Here are the questions you missed. Take a look to learn something new:")
        for item in st.session_state.wrong_answers:
            with st.expander(f"Review: {item['question']}"):
                st.write(f"❌ **Your Answer:** {item['your_answer']}")
                st.write(f"✅ **Correct Answer:** {item['correct_answer']}")
    else:
        st.write("🎉 Flawless victory! You didn't miss a single question.")

    # Reset Button - Generates a completely new set of questions!
    if st.button("🔄 Play Again with New Questions"):
        # Select a brand new set of 5 random questions
        st.session_state.quiz_questions = random.sample(QUESTION_POOL, 5)
        # Reset the pointers and tracking
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.quiz_over = False
        st.session_state.wrong_answers = []
        st.rerun()