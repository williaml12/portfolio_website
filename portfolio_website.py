import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
# model = genai.GenerativeModel('gemini-1.5-flash')
model = genai.GenerativeModel("gemini-2.5-flash")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Murtaza Hassan")

with col2:
    st.img = st.image("images/Murtaza-Hassan-6.png")

st.title(" ")

persona = """
        You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Murtaza: 

        Murtaza Hassan is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Murtaza obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.

        Murtaza's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Murtaza's Email: contact@murtazahassan.com 
        Murtaza's Facebook: https://www.facebook.com/murtazasworkshop
        Murtaza's Instagram: https://www.instagram.com/murtazasworkshop/
        Murtaza's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Murtaza's Github :https://github.com/murtazahassan
        """





# st.title("Murtaza's AI Bot")
# # user_question = st.text_input("Ask anything about me")
# # # st.text_input("Enter your question here:")
# # if st.button("ASK", use_container_width=400):
# #     prompt = persona + "Here is the question that the user asked: " + user_question
# #     response = model.generate_content(prompt)
# #     st.write(response.text)


# # st.title("💬 Chatbot")
# st.caption("🚀 A Streamlit chatbot powered by Google AI")

# # Initialize session state if not already done
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# # Display previous messages
# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# # User input section using chat_input
# if prompt := st.chat_input("Enter a prompt here"):
#     # Append the user's input to the messages
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)

#     # Generate the response using your Google AI model
#     # Assuming `persona` is a string with some predefined context
#     full_prompt = persona + " Here is the question that the user asked: " + prompt
#     response = model.generate_content(full_prompt)  # Replace this with your actual model call to Google AI
#     response_text = response.text  # Assuming the response object has a `text` attribute

#     # Append the assistant's response to the messages
#     st.session_state.messages.append({"role": "assistant", "content": response_text})
#     st.chat_message("assistant").write(response_text)










# # --- Title + Restart button in one row ---
# col1, col2 = st.columns([10, 2])

# with col1:
#     # st.title("Murtaza's AI Bot")
#     st.markdown(
#         "<h1 style='margin: 1; padding: 1;'>Murtaza's AI Bot</h1>",
#         unsafe_allow_html=True
#     )

# with col2:
#     # st.markdown('<div class="align-right">', unsafe_allow_html=True)

#     def clear_chat():
#         st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]
#         # st.rerun()
       
#     st.markdown("<div style='display: flex; justify-content: flex-end;'>", unsafe_allow_html=True)

#     st.button(
#         "Restart",
#         icon=":material/refresh:",
#         on_click=clear_chat
#         )

#     st.markdown("</div>", unsafe_allow_html=True)


# st.caption("🚀 A Streamlit chatbot powered by Google AI")

# # Initialize session state if not already done
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# # Display previous messages
# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# # User input section using chat_input
# if prompt := st.chat_input("Enter a prompt here"):

#     # Append user message
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)

#     # Build full prompt for Google AI
#     full_prompt = persona + " Here is the question that the user asked: " + prompt

#     # AI response
#     response = model.generate_content(full_prompt)
#     response_text = response.text

#     # Append bot response
#     st.session_state.messages.append({"role": "assistant", "content": response_text})
#     st.chat_message("assistant").write(response_text)










# --- Title only ---
# st.markdown("<h1 style='margin: 1; padding: 1;'>Murtaza's AI Bot</h1>", unsafe_allow_html=True)
st.caption("🚀 A Streamlit chatbot powered by Google AI")

# ----------------------------
# ✅ Restart button (WORKS after first prompt)
# ----------------------------
col1, col2 = st.columns([10, 2])

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]

# Display messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
with col1:
    st.markdown(
        "<h1 style='margin: 0; padding: 0;'>Murtaza's AI Bot</h1>",
        unsafe_allow_html=True
    )
    
with col2:

    if len(st.session_state.messages) > 1:

        def clear_chat():
            st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]
            # st.rerun()

        st.button(
            "Restart",
            icon=":material/refresh:",
            on_click=clear_chat
        )
        



# User input
if prompt := st.chat_input("Enter a prompt here"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    full_prompt = persona + " Here is the question that the user asked: " + prompt
    response = model.generate_content(full_prompt)
    response_text = response.text

    st.session_state.messages.append({"role": "assistant", "content": response_text})
    st.chat_message("assistant").write(response_text)

    # 🔥 critical: rerun after new message so header sees updated state
    st.rerun()









st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Computer Vision Channel")
    st.write("- 400k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")


with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3...")

st.title(" ")

st.title("My Setup")
st.image("images/setup.jpg")

st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Teaching", 0, 100, 85)
st.slider("Robotics", 0, 100, 75)

st.write(" ")
st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")

with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")

with col3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")

st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at: ")
st.subheader("contact@murtazahassan.com")

