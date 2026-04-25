import streamlit as st

st.title("Hello chai app")
st.subheader("Brewed with streamlit")
st.text("Welcomoe to you first interactive app")
st.write("Choose your fav variety of chai")
chai=st.selectbox("your prefered this one :", ["black chai" , "lemon chai", "milk chai", "green chai"])
st.write(f"you chose {chai}. Excellent choice")
st.success("your chai has been brewed")
st.title("Lets start do practise")
#st.header("Streamlit")
#st.subheader("Java")

#st.markdown("Puja cv letter")
d=st.text_input("Enter your name ")
e=st.text_input("Ebter your father's name")
f=st.text_area("Enter your address:")
g=st.selectbox("select your corresponding class:" ,{1,2,3,4,5})
button=st.button("Done")
if button : 
  st.markdown(f""""
              Name: {d}
Father's Name: {e}
Address :{f}
class:{g}
              """)
