
import random
from cProfile import label

import streamlit as st
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "attepts" not in st.session_state:
        st.session_state.attepts = 0

if not st.session_state.logged_in:
    name = st.text_input("please enter your name:")
    email = st.text_input("please enter your email adress:")
    password = st.text_input("please enter your passwod:")
    if st.button('adam'):
        if password == "2015":
            st.session_state.logged_in = True
        else:
            st.write('wrong password')
            st.session_state.attepts +=1
    st.stop()

# st.title("chatbotsidd")
# st.subheader("talk to your fake friend")
# st.write("cuz your to lonley to have friends")
mood = st.radio(
"how are you feeling today?",
    ["tired","okay","good","great"])

subject = st.selectbox(
        'rockne',
        ['airockne', 'franklin','kahu']

    )

minute = st.slider(
    "Studay Time (minutes)",
    min_value=1,
    max_value=60,
    value=20,
    step=5)







if st.button('rockne'):
    if subject == "kahu":
        task = [
        "do 5 questions","prepare new","give me some tough questions","geometry","triangle*3"
        ]
    elif subject == "airockne":
        task = ["Review one airockne buddy."]
    elif subject =="franklin":
            task = ["read a article about steven burpa "]
    if mood == "tired":
        tip = "start with only 10 minutes first."
    elif mood == "okay":
        tip = "start with only 10 minutes"
    elif mood == "great":
        tip = "use a 25-minute focus"
    st.write( "Today's task")
    st.write("Smart tip")
    st.info(tip)
    st.write("motovation")
    st.success(random.choice(task))
    st.write("Bonus Challange")
    st.write("Teach Someone what you learned today!")





