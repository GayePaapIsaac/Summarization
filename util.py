import streamlit as st

def config():
    
                # Définir la taille de la police souhaitée
        font_size = "30px"

        # Définir la police de caractères souhaitée
        font_family = "Times New Roman, serif"


       

        # Set the background image
        background_image = """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            background-image: url("https://img.freepik.com/free-photo/3d-rendering-pen-ai-generated_23-2150695471.jpg?t=st=1701176210~exp=1701179810~hmac=8994a86a50586b13e3787ced911a2e5386b5a126f47fbf2a8e5bcdaea90ade7a&w=740");
            background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
            background-position: center;  
            background-repeat: no-repeat;
        }
        </style>
        """
        
        st.markdown(background_image, unsafe_allow_html=True)