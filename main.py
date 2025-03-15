import password
import streamlit as st
import pyperclip


if "generate" not in st.session_state:
    st.session_state.generate = False

if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""



def handleGenerate():
    st.session_state.generate = True

    st.session_state.generated_password = password.generate_strong_password();


def handleCopy(text):
    pyperclip.copy(text)
    st.toast("Password copied to clipboard ✅")


st.title("Password Strength Meter 🔐")
st.markdown("---")

st.sidebar.title("About this app 🔍")
st.sidebar.info("This app allows you to check the strength of a password 🔑")



st.subheader("🔓 Check the strength of your password")

with st.form(key="my_form"):
    password_input = st.text_input("Enter your password", type="password")

    submitted = st.form_submit_button("Check strength")



if submitted:
    score = password.check_password_strength(password_input)
    
    message = password.assign_message(score)
    
    if score < 2:
        st.error(message)
    elif score < 4:
        st.warning(message)
    else:
        st.success(message)



st.markdown("---")



st.subheader("✨ Generate a strong password")

st.button("Generate" if not st.session_state.generate else "Regenerate", on_click=handleGenerate)


if st.session_state.generate:

    gen_pass = st.session_state.generated_password

    col1, col2 = st.columns((4, 1));

    with col1:
        st.success(gen_pass)


    with col2:
        st.button("📎", on_click=handleCopy, args=(gen_pass,))

