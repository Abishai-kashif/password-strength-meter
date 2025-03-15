import password
import streamlit as st
import requests

if "generate" not in st.session_state:
    st.session_state.generate = False

if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""

if "error" not in st.session_state:
    st.session_state.error = ""

if "loading" not in st.session_state:
    st.session_state.loading = False

def handleGenerate():
    st.session_state.generate = True
    st.session_state.loading = True

    while True:    
        strong_password = password.generate_strong_password()

        try:
            response = requests.post("https://password-strength-meter-api.vercel.app/check-password-existence", json={
                            "password": strong_password
                        })

            if response.status_code != 200:
                raise Exception("Password strength meter API returned a non-200 status code")

            does_exists: bool = response.json()['doesExists']

            if not does_exists:
                st.session_state.generated_password = strong_password

                requests.post("https://password-strength-meter-api.vercel.app/insert-password", json={
                            "password": strong_password
                        })

                break
        except Exception as e:
            st.session_state.error = str(e)
            break
        finally:
            st.session_state.loading = False



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
    if st.session_state.loading:
        st.warning("Loading....")
    elif st.session_state.error:
        st.error(st.session_state.error)
    else:
        st.success( st.session_state.generated_password)

