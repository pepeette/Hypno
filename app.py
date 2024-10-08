import streamlit as st
import webbrowser
from PIL import Image

# Set page config
st.set_page_config(page_title=" Transcend Your Life💫", page_icon="./img/emojishootingstar.png", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        font-family: Georgia, serif;
        line-height: 1.6;
    }
    h1, h2, h3, h4, h5 {
        font-family: 'Arial', sans-serif;
    }
    .card {
        background-color: #F7F9F9;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #3498DB;
        color: white;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #2980B9;
    }
    </style>
""", unsafe_allow_html=True)

# Function to open Calendly
def open_calendly():
    webbrowser.open("https://calendly.com/titre/free-session")

# Header
st.markdown("## 💫 TRANSCEND YOUR LIFE WITH HYPNOTHERAPY")

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("IS IT FOR ME❔"):
        st.link_button("IS IT FOR ME❔", "https://calendly.com/titre/free-session")
        #open_calendly()

with col2:
    st.markdown("[FREE ASSESSMENT](https://calendly.com/titre/free-session)")

st.markdown("Transform your life with my hypnotherapy sessions, designed to create lasting behavior change by integrating the powerful tools of DBT (Dialectical Behavior Therapy).")

# Sidebar for navigation
page = st.sidebar.radio("Choose a page", ["Home", "Approach", "About"])

# Function to display Approach content
def show_approach():
    st.markdown("### Discover How Hypnotherapy Can Transform Your Life")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("#### 😌 Stress Relief")
        st.markdown("Overcome anxiety and find inner peace")
    with col2:
        st.markdown("#### 🤝 Improve Relationships")
        st.markdown("Enhance social skills and emotional intelligence")
    with col3:
        st.markdown("#### 🥗 Healthy Eating Habits")
        st.markdown("Achieve sustainable weight management")
    with col4:
        st.markdown("#### 🚭 Break Free from Addiction")
        st.markdown("Quit smoking and other dependencies for good")

    st.markdown("---")
    st.markdown("### The Journey to Happiness: Change, Purpose, and Method")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("Discovering true happiness is simpler than you might think.")
        st.write("However, we often complicate this journey with self-imposed limitations and destructive patterns.")
        st.write("These patterns, built up over time, obscure the clear path to contentment and self-fulfillment.")
        st.write("By embracing the 'Path of Least Resistance', we can reprogram these ingrained neural patterns and unlock our true potential.")
    with col2:
        st.image("./img/emo.jpg", width=100, caption="Embrace Your Emotions")

    st.image("./img/BehaviourMap.png", caption="Understanding Behavior Patterns", width=400)

    st.markdown("### Frequently Asked Questions")
    with st.expander("Is hypnotherapy safe?"):
        st.write("Yes, hypnotherapy is a safe and non-invasive form of therapy when conducted by a certified professional. The purpose is to rewire a self sabotaging behaviour onto a healthier and happier one.")
    with st.expander("How many sessions will I need?"):
        st.write("The number of sessions varies depending on individual needs and goals. Usually we proceed in 2 sessions : Therapy and Hypnotherapy. We'll discuss this during your initial consultation.")

# Function to display About content
def show_about():
    st.markdown("### About Me: Your Guide to Transformation")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("./img/ID.jpg", width=200, caption="Laetitia Sheppard")
    with col2:
        st.write("As a certified practitioner in Ericksonian Hypnotherapy and Cognitive Behaviour, I bring a wealth of experience and expertise to help you on your journey of self-improvement.")
        st.write("My credentials include:")
        st.markdown("- Certification from the [London College of Clinical Hypnotherapy in 2017](https://lcchinternational.co.uk/alumni/)")
        st.markdown("- Years of practical experience helping clients overcome various challenges")
        st.markdown("- Continuous professional development to stay at the forefront of hypnotherapy techniques [LinkedIn](https://www.linkedin.com/in/laetitia-sheppard)")

    st.write("My approach is tailored to each individual, ensuring that you receive personalized care and attention throughout your transformative journey.")

    st.markdown("### Testimonials : Their Takeaways")
    col1, col2 = st.columns(2)
    with col1:
        st.image("./img/client1.jpg", width=100)
        st.write("\"The hypnotherapy sessions have been life-changing. I've never felt more in control of my habits.\"")
        st.write("- Lora H., 🇺🇸 , Weight Management")
    with col2:
        st.image("./img/client3.jpg", width=100)
        st.write("\"I was skeptical at first, but the results speak for themselves. My stress levels have decreased significantly.\"")
        st.write("- Juliette P., 🇫🇷 , Stress Relief")

    st.markdown("### Get in Touch")
    contact_form = st.form("contact_form")
    name = contact_form.text_input("Name")
    email = contact_form.text_input("Email")
    message = contact_form.text_area("Message")
    submit_button = contact_form.form_submit_button("Send Message")

    if submit_button:
        st.success("Message sent successfully!")

    st.markdown("### We will meet Here")
    st.markdown("[46/9 Soi Sukhumvit 49, Klong Ton Nua, Wattana District](https://www.google.com/maps/place/the+Hive+Thonglor/@13.7320825,100.571723,17z/data=!3m1!4b1!4m6!3m5!1s0x30e29e55a95f6f93:0xf9a8634f35bf33a6!8m2!3d13.7320825!4d100.5765939!16s%2Fg%2F1q6b9rc2_?entry=ttu&g_ep=EgoyMDI0MDgyMS4wIKXMDSoASAFQAw%3D%3D)")
    st.image("./img/Map.png")

if page == "Home":
    # Subtabs for Approach and About
    tab1, tab2 = st.tabs(["Approach", "About"])
    
    with tab1:
        show_approach()
    
    with tab2:
        show_about()

elif page == "Approach":
    st.markdown("##  ")
    show_approach()
    st.markdown("##  ")

elif page == "About":
    st.markdown("##  ")
    show_about()
    st.markdown("##  ")

# Run the app
if __name__ == "__main__":
    st.sidebar.success("Select a page above.")
