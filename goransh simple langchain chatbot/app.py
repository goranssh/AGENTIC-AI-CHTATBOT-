if st.button("🧹 Clear Conversation"):
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant.")
    ]
    memory.clear()  # This clears the memory in LangChain as well

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# User input
user_input = st.chat_input("Say something...")

if user_input:
    # Add user input to the conversation
    st.session_state.messages.append(HumanMessage(content=user_input))
    
    # Get bot response
    with st.spinner("Thinking..."):
        response = conversation.predict(input=user_input)  # Use LangChain to predict
    st.session_state.messages.append(HumanMessage(content=response))  # Append response to the session state

# Display chat history
for msg in st.session_state.messages[1:]:  # Skip system message
    role = "🧑 You" if isinstance(msg, HumanMessage) else "🤖 Bot"
    st.markdown(f"**{role}:** {msg.content}")
