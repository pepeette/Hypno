import streamlit as st

def create_assess_page():
    st.title("✅ Assessment Import Test - Working!")
    st.success("The assess.py file is importing correctly")
    st.info("This confirms the import issue is fixed")
    
    # Test form
    with st.form("test_form"):
        name = st.text_input("Test name:")
        email = st.text_input("Test email:")
        submitted = st.form_submit_button("Test Submit")
        
        if submitted:
            st.success(f"✅ Form works! Name: {name}, Email: {email}")

if __name__ == "__main__":
    create_assess_page()
