import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


st.set_page_config(layout="wide")

image = Image.open("zhengyang.jpg")
st.image(image, width=300)

st.title("Zac Lim Zheng Yang")
st.markdown(
    """
    Welcome to my page!
    """
)

# col1_sidebar = st.sidebar
# col1_sidebar_menu = col1_sidebar.header("Menu")

# st.sidebar.button(label="menu",
#                   help="click to find out more about me",
#                   on_click=st.)


#
# col1_sidebar_about = col1_sidebar.subheader("About")
# col1_sidebar_contact = col1_sidebar.subheader("Contact")
# col1_sidebar_work_experience = col1_sidebar.subheader("Work Experience")
#

with st.sidebar:
    choose = option_menu("Menu", ["About", "Work Experience", "Contact"],
                         icons=['house', 'briefcase', 'telephone'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "#007fff", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#f0ffff"},
        "nav-link-selected": {"background-color": "#89cff0"},
    }
    )

# logo = Image.open(r'C:\Users\13525\Desktop\Insights_Bees_logo.png')
# profile = Image.open(r'C:\Users\13525\Desktop\medium_profile.png')
if choose == "About":
    # col1, col2 = st.columns([20, 3])
    # with col1:  # To display the header text using css style
    st.markdown(""" <style> .font {
        font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">More About Me</p>', unsafe_allow_html=True)


    st.write(
        "Zheng Yang graduated from Nanyang Technological University with a Bachelor of Engineering (Civil)."
        " He is an aspiring Software Engineer who spends his time off work to hone his coding skills and to build projects."
        " He believes that technology holds the key to change the world in an unimaginable way."
        " In his free time, he likes to hit the gym, spend time with his dog, make a cup of nice filtered coffee, and to hang out with his friends.")

elif choose == "Work Experience":
    st.markdown(""" <style> .font {
        font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Work Experience</p>', unsafe_allow_html=True)

    st.header("""
            Software Engineer (February 2022 - Present)
            """)


    st.write("""
        Zheng Yang managed to transition into the tech industry and started off his career with a software engineering position.
         He has dabbled with HTML, Java codes to develop and maintain the frontend and backend.
          At the same time, he was also responsible to write out SQL scripts to make necessary changes to databases in development, UAT, and production environment. 
        """)

    st.header("""
        Operations Executive (August 2021 - February 2022)
        """)

    st.write("""
    Zheng Yang oversaw the facilities and management of a shopping centre. 
     He was responsible for the tender, bidding, award, and execution of rectification and upgrading works.
      He was also placed in charge of work budget up to 2 million dollars (SGD) 
    """)

    st.header("""
    Site Engineer (August 2020 - August 2021)
    """)

    st.write("""
    Zheng Yang led and managed a residential project to build Housing Development Board (HDB) Built-To-Order (BTO) flats.
     As an Engineer, he was responsible for the high level overview such as the cost, progression, and quality of the works.
     On the ground, he took care of the nitty-gritty such as the welfare of the workers, the workmanship, and the liaison between different contractors.
     In his one year stint, Zheng Yang saw the completion of the building structure of two residential blocks.
    """)

    # with col2:  # To display brand logo
    #     st.image(logo, width=150)
    # Add file uploader to allow users to upload photos
    # uploaded_file = st.file_uploader("", type=['jpg', 'png', 'jpeg'])
    # if uploaded_file is not None:
    #     image = Image.open(uploaded_file)

    # converted_img = np.array(image.convert('RGB'))
    # gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
    # inv_gray = 255 - gray_scale
    # blur_image = cv2.GaussianBlur(inv_gray, (125, 125), 0, 0)
    # sketch = cv2.divide(gray_scale, 255 - blur_image, scale=256)
    # st.image(sketch, width=300)

elif choose == "Contact":
    st.markdown('<p class="font">Contact Me</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font {
    font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)

    st.write("""
    :mailbox: Email: zhengyanglim057@gmail.com
    """)

    st.write("""
    :mailbox: Linkedin: https://www.linkedin.com/in/zheng-yang-lim-a30906180/
    """)

    st.write("""
    :mailbox: Instagram: https://www.instagram.com/zhengyang_official/
    """)

    st.write("""
    :mailbox: Facebook: https://www.facebook.com/zhengyang.lim.zac
    """)

    # st.markdown('<span icon="123"</span>', unsafe_allow_html=True)

    # st.markdown('<p class="font">Contact Page</p>', unsafe_allow_html=True)
    # with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
    #     #st.write('Please help us improve!')
    #     Name=st.text_input(label='Please Enter Your Name') #Collect user feedback
    #     Email=st.text_input(label='Please Enter Email') #Collect user feedback
    #     Message=st.text_input(label='Please Enter Your Message') #Collect user feedback
    #     submitted = st.form_submit_button('Submit')
    #     if submitted:
    #         st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
