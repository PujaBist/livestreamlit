import streamlit as st
st.title("Hello chai app")
st.subheader("Brewed with streamlit")
st.text("Welcomoe to you first interactive app")
st.write("Choose your fav variety of chai")
chai=st.selectbox("your prefered this one :", ["black chai" , "lemon chai", "milk chai", "green chai"])
st.write(f"you chose {chai}. Excellent choice")
st.success("your chai has been brewed")