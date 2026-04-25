import streamlit as st
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