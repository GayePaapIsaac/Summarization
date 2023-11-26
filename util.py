import streamlit as st

def config():
    
        original_title = '<h1 style="font-family: serif; color:white; font-size: 20px;"></h1>'
        st.markdown(original_title, unsafe_allow_html=True)


        # Set the background image
        background_image = """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            background-image: url("https://storage.letudiant.fr/mediatheque/letudiant/1/0/2522310-adobestock-322914233-766x438.jpeg");
            background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
            background-position: center;  
            background-repeat: no-repeat;
        }
        </style>
        """

        st.markdown(background_image, unsafe_allow_html=True)