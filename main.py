from taipy import Gui
import taipy.gui.builder as tgb
#from taipy.gui import Gui, get_user_content_url, Markdown
import os

with tgb.Page() as root_page:
    with tgb.part(class_name="background-image"):
        tgb.text("#### 💫 TRANSCEND YOUR LIFE WITH HYPNOTHERAPY", mode="md", style="color: white; font-size: 3em; text-align: center;")
        def open_calendly():
            import webbrowser
            webbrowser.open("https://calendly.com/titre/free-session")  # Replace with your actual Calendly link
        tgb.text("   ")
        tgb.text("   ")
        #with tgb.layout("1 2"):
        tgb.button(" IS IT FOR ME? FREE ASSESSMENT ", on_action=open_calendly, style="display: flex; align-items: center; justify-content: center;")
        tgb.text("Transform your life with my hypnotherapy sessions, designed to create lasting behavior change by integrating the powerful tools of DBT (Dialectical Behavior Therapy).")# Unlock your full potential and achieve enduring results through a unique blend of therapeutic techniques.", style="color: white; text-align: center;")
        tgb.text("   ")
        tgb.text("   ")
        tgb.text("---", mode="md")

        tgb.navbar(class_name="primary")

        
        
initial_state = {
    "Name": "",
    "Email": "",
    "Message": "",
    "success_message": "",
    "error_message": "",
    "image_enlarged": False  # New state variable for image enlargement
}

#small emo to big 
def toggle_image(state):
    state.image_enlarged = not state.image_enlarged  # Toggle the boolean value
# Update the image rendering based on the state
image_width = "100px" if not initial_state["image_enlarged"] else "100%"  # Determine the width based on the state

# Contact function
messages = []

def send_message(state):
    if hasattr(state, 'Name') and hasattr(state, 'Email') and hasattr(state, 'Message'):
        name = state.Name
        email = state.Email
        message = state.Message

        if name and email and message:
            messages.append({
                "name": name,
                "email": email,
                "message": message
            })
                
            # Clear the form fields after successful submission
            state.Name = ""
            state.Email = ""
            state.Message = ""
                
            # Show a success message
            state.success_message = "Message sent successfully!"
            state.error_message = ""
        else:
            # Show an error message if any field is empty
            state.error_message = "Please fill in all fields."
            state.success_message = ""
    else:
        state.error_message = "Form fields are not properly initialized."
        state.success_message = ""


with tgb.Page() as page1:
    # What We Offer Section
    tgb.text(
        "#### Discover How Hypnotherapy Can Transform Your Life", mode="md",style="text-align: center; margin-top: 50px;"
    )
    #tgb.text("Explore how Ericksonian Hypnotherapy can help you break free from these limitations:", mode="md")
    
    with tgb.layout("1 1 1 1"):
        with tgb.part("card"):
            tgb.text(
                "##### 😌 Stress Relief",
                mode="md",
            )
            tgb.text(
                "Overcome anxiety and find inner peace", #"Find inner peace and manage anxiety effectively"
                mode="md", hover_text=True
            )

        with tgb.part("card"):
            tgb.text(
                "##### 🤝 Improve Relationships",
                mode="md",
            )
            tgb.text(
                "Enhance social skills and emotional intelligence", #Enhance self-esteem and personal growth
                mode="md", hover_text=True
            )

        with tgb.part("card"):
            tgb.text(
                "##### 🥗 Healthy Eating Habits",
                mode="md",
            )
            tgb.text(
                "Achieve sustainable weight management", #Achieve sustainable weight loss through mindset change
                mode="md", hover_text=True
            )

        with tgb.part("card"):
            tgb.text(
                "##### 🚭 Break Free from Addiction",
                mode="md",
            )
            tgb.text(
                "Quit smoking and other dependencies for good", #"Break free from harmful habits and dependencies"
                mode="md", hover_text=True
            )
    tgb.text("---", mode="md")

    # Benefits Section
    tgb.text("#### The Journey to Happiness: Change, Purpose, and Method", mode="md",style="text-align: center; margin-top: 50px;")
    tgb.text("---", mode="md")
    with tgb.layout("3 1"):
        with tgb.part():
            tgb.text(
                "Discovering true happiness is simpler than you might think."
            )
            tgb.text(
                "However, we often complicate this journey with self-imposed limitations and destructive patterns."
            )
            tgb.text(
                "These patterns, built up over time, obscure the clear path to contentment and self-fulfillment."
            )
            tgb.text(
                "By embracing the 'Path of Least Resistance', we can reprogram these ingrained neural patterns and unlock our true potential."
            )

        # Image component
        tgb.image("./img/emo.jpg", width=image_width, label="Embrace Your Emotions", on_action=toggle_image)

        #tgb.image("./img/emo.jpg", width="100px", label="Embrace Your Emotions")
    tgb.text("---", mode="md")
    tgb.image("./img/BehaviourMap.png", label="Understanding Behavior Patterns", width="50%")
    tgb.text("---", mode="md")
    
    # FAQ Section
    tgb.text("#### Frequently Asked Questions", mode="md", style="text-align: center; margin-top: 50px;")
    with tgb.part("accordion"):
        tgb.text("##### Is hypnotherapy safe?", mode="md")
        tgb.text("Yes, hypnotherapy is a safe and non-invasive form of therapy when conducted by a certified professional. The purpose is to rewire a self sabotaging behaviour onto a healthier and happier one.")
        tgb.text("##### How many sessions will I need?", mode="md")
        tgb.text("The number of sessions varies depending on individual needs and goals. Usually we proceed in 2 sessions : Therapy and Hypnotherapy. We'll discuss this during your initial consultation.")
    
    tgb.text("---", mode="md")
    tgb.navbar(class_name="primary")
    tgb.text("---", mode="md")

# Page 2 content
with tgb.Page() as page2:
    # About us section
    tgb.text("#### About Me: Your Guide to Transformation", mode="md")
    tgb.text("---", mode="md")

    with tgb.layout("1 3"):
        tgb.image("./img/ID.jpg", width="50%", label="Laetitia Sheppard")
        
        with tgb.part():
            tgb.text(
                "As a certified practitioner in Ericksonian Hypnotherapy and Cognitive Behaviour, I bring a wealth of experience and expertise to help you on your journey of self-improvement."
            )
            tgb.text(
                "My credentials include:"
            )
            tgb.text(
                "- Certification from the London College of Clinical Hypnotherapy (2017)"
            )
            tgb.text(
                "- Years of practical experience helping clients overcome various challenges"
            )
            tgb.text(
                "- Continuous professional development to stay at the forefront of hypnotherapy techniques"
            )

    tgb.text(
        "My approach is tailored to each individual, ensuring that you receive personalized care and attention throughout your transformative journey."
    )

    tgb.text("---", mode="md")

    # Testimonials Section
    tgb.text("#### Testimonials : Their Takeaways", mode="md")
    with tgb.layout("1 1"):
            with tgb.part("card"):
                tgb.image("./img/client1.jpg", width="100px", style="border-radius: 50%;")
                tgb.text("\"The hypnotherapy sessions have been life-changing. I've never felt more in control of my habits.\"", style="font-style: italic;")
                tgb.text("- Lora H., 🇺🇸 , Weight Management")
            with tgb.part("card"):
                tgb.image("./img/client2.jpg", width="100px", style="border-radius: 50%;")
                tgb.text("\"I was skeptical at first, but the results speak for themselves. My stress levels have decreased significantly.\"", style="font-style: italic;")
                tgb.text("- Juliette P., 🇫🇷 , Stress Relief")


    tgb.text("---", mode="md")

    # Contact Section
    with tgb.layout("1 1"):  # Creates a two-column layout

        # Left Column: Google Map Directions
        with tgb.part():
            tgb.text("#### Find Us Here", mode="md", style="text-align: center;")
            # Embed Google Maps (Replace the URL with your actual Google Maps link)
            tgb.text("You can find us at: [46/9 Soi Sukhumvit 49, Klong Ton Nua, Wattana District](https://www.google.com/maps/place/the+Hive+Thonglor/@13.7320825,100.571723,17z/data=!3m1!4b1!4m6!3m5!1s0x30e29e55a95f6f93:0xf9a8634f35bf33a6!8m2!3d13.7320825!4d100.5765939!16s%2Fg%2F1q6b9rc2_?entry=ttu&g_ep=EgoyMDI0MDgyMS4wIKXMDSoASAFQAw%3D%3D)", mode='md')
            tgb.image("./img/Map.png", width="100%")

        # Right Column: Get in Touch Form
        with tgb.part():
            tgb.text("#### Get in Touch", mode="md", style="text-align: center; margin-top: 50px;")
            tgb.input("Name", state="Name")
            tgb.input("Email", state="Email")
            tgb.input("Message", multiline=True, state="Message")
            tgb.button("Send Message", on_action=send_message)
            
            # Add success and error message displays
            tgb.text("{success_message}", style="color: green;")
            tgb.text("{error_message}", style="color: red;")

    tgb.text("---", mode="md")

    # Display submitted messages (for demonstration purposes)
    tgb.text("#### Submitted Messages", mode="md", style="text-align: center; margin-top: 50px;")
    for msg in messages:
        with tgb.part(class_name="card"):
            tgb.text(f"**From:** {msg['name']} ({msg['email']})", mode="md")
            tgb.text(f"**Message:** {msg['message']}", mode="md")

    # tgb.text("#### Get in Touch", mode="md", style="text-align: center; margin-top: 50px;")
    # tgb.input("Name")
    # tgb.input("Email")
    # tgb.input("Message", multiline=True)
    # tgb.button("Send Message")
    
    tgb.text("---", mode="md")
    tgb.navbar(class_name="primary")
    tgb.text("---", mode="md")
    
pages = {
    "/": root_page,
    "Approach": page1,
    "About": page2,
}
gui_multi_pages = Gui(pages=pages)


if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    gui_multi_pages.run(
        host="0.0.0.0", 
        use_reloader=False,
        title="Transcend Your Life💫",
        port=5000,#port=port,
        dark_mode=False,
        favicon='./img/emojishootingstar.png',
        styles={
            "h1, h2, h3, h4, h5": {"font-family": "'Arial', sans-serif"},
            "p": {"font-family": "Georgia, serif", "line-height": "1.6"},
            "body": {"font-family": "Georgia, serif", "line-height": "1.6"},
            ".card": {"background-color": "#F7F9F9", "border-radius": "10px", "padding": "20px", "box-shadow": "0 4px 8px rgba(0,0,0,0.1)", "margin-bottom": "20px"},
            ".primary": {"background-color": "#3498DB", "color": "white"},
            "button": {"transition": "background-color 0.3s", "cursor": "pointer"},
            "button:hover": {"background-color": "#2980B9"},
            ".background-image": {
                "background-image": "url('/img/OIP.jpg')",  # Correctly formatted URL
                "background-size": "cover",
                "height": "100vh",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "flex-direction": "column"
            }
        },
        state=initial_state
    )
