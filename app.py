#Lets start to explore streamlit frameowork
# import the streamlit
import streamlit as st
import time as t
#1. For title 
st.title('Hello, How are you?')
st.header('Streamlit Basic Concepts')
### -------------------------------------
# 2. for header
st.header('Artifical Intelligence')
#----------------------------------------
# 3. for subheader
st.subheader('Machine Learning')
#------------------------------------------
# 4. for infromation detials
st.info('Information details of employe')
#------------------------------------------------------
# 5. To set the waring in webbpage
st.warning('Hey alort')
#---------------------------------------------
# 6. To write someting
st.write('Employe Names')
#---------------------------------
# 7. To write in coding format
st.write(range(50)) 
# ----------------------------
# 8. To show error message
st.error('Wrong Path') 
#--------------------------------------------
# 9. To show sucess message
#st.success('Congrats you get grade A') 
#--------------------------------------------
# 10 for markdown
st.markdown('# Learn More Earn More') 
st.markdown('## Welcome to my chanel')

st.markdown(':moon:') # Moon Emogi
#-------------------------------
# 11. To write text
st.text('Hello my name is Rem Magar') 
#---------------------------------------------
# 12. To set the caption
st.caption('Caption is here')
#------------------------------------
# 13. Write in the LaTeX format
st.latex(r'a+bx^2 = c') 
# -------------------------------
# 14. To put images
# for images
st.image('images/g2.jpg', width=250)
st.image('images/g1.jpg', width=250)
st.image('images/g3.jpg', width=250)
st.header('Different Widgets')
#------------------------------------------
# 1. checkbox
st.checkbox('Login here')
#----------------------------
#2. button
st.button('Click Me')

# 3. Radio button
st.radio('Pick your gender',['M','F','N'])

#4. Select box
st.selectbox('Pick your cource',['Ml','Dl','Ai','Ds'])

#5. Multiple selection
st.multiselect('Check your department',['physics','maths','bio'])

#6. Slider
st.slider('Enter your name',0,100)

# 7. Number Input
st.number_input('Pick a number',0,100)

# 8. Text Input
st.text_input('Enter your email')

# 9. Date Input
st.date_input('Openign ceromeny')

# 10. Time Input
st.time_input('Hey what time is is?')

# 11. Text area
st.text_area('Welcome to Learn more earen meore')

# 12. File uploder
st.file_uploader("Choose a file")

# 12. Color Pick
st.color_picker('Pick A Color', '#00f900')

# 13. Progress report
st.progress(90) # 90%

# Spinner message
st.spinner('Just Wait')

with st.spinner('Just wait'):
    t.sleep(2)
# Celebration Ballons

st.balloons()
#-------------------------------------------------
st.header('Sidebar we can see in left side')
# Side bar
#st.sidebar('Welcome to RBGM')
st.sidebar.title('Learn More Earn More')
st.sidebar.text_input('Enter your Email')
st.sidebar.text_input('Password')
st.sidebar.button('Submit')
st.sidebar.radio('Export',['a','b'])
# ----------------------------------------
# practical
st.header('Practical IMplementation')
# Practical IMplementation
# Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
# Generate random data for the scatter plot
x = np.random.randn(50)
y = np.random.randn(50)

# Create a DataFrame from the random data
data = {'X': x, 'Y': y}
df = pd.DataFrame(data)

# Display the DataFrame
st.write(df)
st.title('Bar Chart')
st.bar_chart(df)
st.title('Line Chart')
st.line_chart(df)
st.title('Area Chart')
st.area_chart(df)
#--------------------------------------
st.header('Making a Nav bar')
st.text('We set our Navigation bar in the sidebar')
#-------------------------
# pip install streamlit-option-menu
from streamlit_option_menu import option_menu
#-----------------------------------------
with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",# required None for not main menu
        options = ["Home","About","Projects","Contact Me"], # required
        icons = ['house','book','envelope','book'], # optional
        menu_icon = 'cast', # ooptional
        default_index = 0, # optional
    )
if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "About":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact Me":
    st.title(f"You have selected {selected}")
#-------------------------------------------
st.header('Horizontal Nav Bar')
#with st.sidebar:
selected = option_menu(
    menu_title = None,# required None for not main menu
    options = ["Home","About","Projects","Contact Me"], # required
    icons = ['house','book','envelope','book'], # optional
    menu_icon = 'cast', # ooptional
    default_index = 0, # optional
    orientation = 'horizontal', # for horizontal menus
    styles = {
        'container':{'padding':'0!important','background-color':'green'},
        'icon':{'color':'orange','font-size':'25px'},
        'nav-link':{
            'font-size':'25px',
            'text-align':'left',
            'margin':'0px',
            '--hover-color':'#eee'
        },
    },
    )
if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "About":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact Me":
    st.title(f"You have selected {selected}")
#-------------------------------------------
st.header('Animation ')
# Required
import json
import requests # pip install requests
import streamlit as st # pip install streamlit
from streamlit_lottie import st_lottie # pip install streamlit-lottie
#----------------
#LOad json form local drive
#def load_lottiefile(filepath: str):
    #with open(filepath,"r") as f:
       # return json.load(f)
#---------------
# Load lotiefile form online directly
def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# load the files
#lottie_coding = load_lottiefile('PyWebApp/coding.json')
lottie_hello = load_lottieurl('https://lottie.host/68980b26-1d5b-4867-a17c-c830faf5e704/EvI7LJx4cW.json')
# fetch
st.title('Include Lottie files')
#'''st_lottie(
    #lottie_coding,
   # speed = 1,
    #reverse = False,
    #loop = True,
   # quality = "low",# medium, high
    #renderer = "svg", # canvas
    #height = None,
    #width = None,
    #key = None,
#)
#'''
# for second animation
st_lottie(lottie_hello,
    speed = 1,
    reverse = False,
    loop = True,
    quality = "low",# medium, high #renderer = "svg", # canvas
    height = None,
    width = None,
    key = None,
)
# form local
def load_lottie_file(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
lottie_coding = "PyWebApp/coding.json"
st_lottie(lottie_coding,
    speed = 1,
    reverse = False,
    loop = True,
    quality = "low",# medium, high#renderer = "svg", # canvas
    height = None,
    width = None,
    key = None,
)
st.title('Fully functional Conatat form')
st.header(':mailbox: Get in Touch wiht Me!')
# use formsubmit.co
# for css use w3school.com
contact_form = """
<form action="https://formsubmit.co/ghartirem072@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
    <textarea name="message" placeholder="Details of your problem"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form,unsafe_allow_html= True)
# cssss style is remains to learn
# Digital REsume
st.title("Digital Resume")
# To make awesome profile picture
# https://pfpmaker.com
#---------------------------
from pathlib import Path
import streamlit as st
from PIL import Image
#-----------------------------------
# current directory cwd is for parrent directory
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"style" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "pp.jpg"
#------------------------------------------
#General settings
PAGE_TITLE = "Digital CV | Rem Magar"
PAGE_ICON = ":wave:"
NAME = "Rem Magar"
DESCRIPTION = """ Matheamtician and Data Scientist"""
EMAIL = "ghartirem072@gmail.com"
SOCIAL_MEDIA = {
    "YouTube":"link",
    "LinkedIn":"link:",
    "GitHub":"link",
    "Viber": "link",
    "Twitter":"link"
}
PROJECTS = {
    "One: link",
    "Two: link",
    "Three: link",
    "Four: link"
}
# can use direct emoji
# page configuration
#
