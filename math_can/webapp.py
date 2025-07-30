###experminetal ui

import streamlit as st
import random
import time

from math_can.operators import add, subtract, multiply, divide

op_map = {
    '+': ('add', add, '+'),
    '-': ('subtract', subtract, '-'),
    '*': ('multiply', multiply, '*'),
    '/': ('divide', divide, '/'),
}

def reset_quiz_state():
    st.session_state.quiz_started = False
    st.session_state.questions = []
    st.session_state.answers = []
    st.session_state.start_times = []
    st.session_state.end_times = []
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.quiz_start_time = None
    st.session_state.quiz_timer = 0.0
    st.session_state.name = ""
    st.session_state.last_input = ""
    st.session_state.just_submitted = False
    st.session_state.last_timer_rerun = 0

if 'page' not in st.session_state:
    reset_quiz_state()
    st.session_state.page = 'welcome'

if st.session_state.page == 'welcome':
    st.title("🧮 MathCan Quiz")
    st.markdown("""
        ## Welcome to MathCan!
        Sharpen your mental math skills with a fun, interactive quiz.
    """)
    if st.button("Start"):
        st.session_state.page = 'name'
        st.rerun()
elif st.session_state.page == 'name':
    st.title("🧮 MathCan Quiz")
    st.markdown("## What's your name?")
    name = st.text_input("Enter your name:", key="name_input")
    if st.button("Continue") and name.strip():
        st.session_state.name = name.strip()
        st.session_state.page = 'settings'
        st.rerun()
elif st.session_state.page == 'settings':
    st.title("🧮 MathCan Quiz")
    st.markdown(f"### Hello, {st.session_state.name}! Configure your quiz below.")
    op_choices = st.multiselect(
        "Choose operations:",
        options=list(op_map.keys()),
        default=['+']
    )
    num_questions = st.number_input(
        "How many questions?", min_value=1, max_value=50, value=5, step=1
    )
    if st.button("Start Quiz") and op_choices and num_questions:
        st.session_state.quiz_started = True
        st.session_state.page = 'quiz'
        st.session_state.name = st.session_state.name  # preserve name
        st.session_state.quiz_start_time = time.time()
        st.session_state.questions = []
        st.session_state.answers = []
        st.session_state.start_times = []
        st.session_state.end_times = []
        st.session_state.current = 0
        st.session_state.score = 0
        for _ in range(num_questions):
            op = random.choice(op_choices)
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            if op == '/' and b == 0:
                b = 1
            st.session_state.questions.append((op, a, b))
            st.session_state.answers.append(None)
            st.session_state.start_times.append(None)
            st.session_state.end_times.append(None)
        st.rerun()

elif st.session_state.page == 'quiz' and st.session_state.quiz_started and st.session_state.current < len(st.session_state.questions):
    idx = st.session_state.current
    op, a, b = st.session_state.questions[idx]
    op_disp = op_map[op][2]
    now = time.time()
    import datetime
    if st.session_state.quiz_start_time:
        elapsed = int(now - st.session_state.quiz_start_time)
        timer_str = str(datetime.timedelta(seconds=elapsed))
    else:
        timer_str = '0:00'
    st.markdown(f"<div style='display:flex;justify-content:center;align-items:center;'><h3>⏱️ Timer: {timer_str}</h3></div>", unsafe_allow_html=True)
    if 'last_timer_rerun' not in st.session_state:
        st.session_state['last_timer_rerun'] = now
    if not st.session_state.get('just_submitted', False) and now - st.session_state['last_timer_rerun'] >= 1:
        st.session_state['last_timer_rerun'] = now
        st.rerun()
    st.markdown(f"**Operations:** {', '.join([op_map[o][2] for o in set([q[0] for q in st.session_state.questions])])}")
    st.markdown(f"**Question:** {idx+1}/{len(st.session_state.questions)}")
    st.markdown(f"<div style='display:flex;justify-content:center;align-items:center;height:100px;'><h2>Q{idx+1}: {a} {op_disp} {b} = ?</h2></div>", unsafe_allow_html=True)
    if st.session_state.start_times[idx] is None:
        st.session_state.start_times[idx] = time.time()
    user_input = st.text_input("Your answer:", key=f"answer_{idx}", on_change=None)
    submit = st.button("Submit", key=f"submit_{idx}")
    if (submit or (user_input and st.session_state.get('last_input', '') != user_input)) and user_input.strip() != "":
        st.session_state.end_times[idx] = time.time()
        try:
            user_answer = float(user_input)
            answer = op_map[op][1](a, b)
            if abs(user_answer - answer) < 1e-6:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect. The correct answer is {answer}")
        except Exception:
            st.error(f"Invalid input. The correct answer is {op_map[op][1](a, b)}")
        st.session_state.current += 1
        st.session_state['last_input'] = ""
        st.session_state['just_submitted'] = True
        st.rerun()
    elif (submit or (user_input and st.session_state.get('last_input', '') != user_input)) and user_input.strip() == "":
        st.session_state['just_submitted'] = True
        st.warning("Please enter an answer before continuing.")
    else:
        st.session_state['just_submitted'] = False
    st.session_state['last_input'] = user_input

# --- Summary Page ---
elif st.session_state.page == 'quiz' and st.session_state.quiz_started and st.session_state.current >= len(st.session_state.questions):
    st.title("🧮 MathCan Quiz")
    st.markdown(f"### Well done, {st.session_state.name}!")
    total_time = sum([
        (et - st) if st and et else 0
        for st, et in zip(st.session_state.start_times, st.session_state.end_times)
    ])
    accuracy = (st.session_state.score / len(st.session_state.questions)) * 100
    st.write(f"**Correct:** {st.session_state.score}/{len(st.session_state.questions)}")
    st.write(f"**Accuracy:** {accuracy:.1f}%")
    st.write(f"**Total time:** {total_time:.2f} seconds")
    st.write(f"**Avg time/question:** {total_time/len(st.session_state.questions):.2f} seconds")
    if st.button("Restart Quiz"):
        reset_quiz_state()
        st.session_state.page = 'welcome'
        st.rerun()
