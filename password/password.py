import streamlit as st
import re

def check_password_strength(password):
    score = 0
    strength = "Weak"
    
    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    
    # Upper and lower case check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    
    # Number check
    if re.search(r"\d", password):
        score += 1
    
    # Special character check
    if re.search(r"[@$!%*?&#]", password):
        score += 1
    
    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score >= 4:
        strength = "Strong"
    
    return strength, score

def main():
    st.title("🔒 Password Strength Checker")
    
    password = st.text_input("Enter your password", type="password")
    
    if password:
        strength, score = check_password_strength(password)
        
        st.subheader(f"Strength: {strength}")
        st.progress(score / 5)
        
        if score < 3:
            st.warning("Consider using a longer password with a mix of uppercase, lowercase, numbers, and special characters.")
        else:
            st.success("Your password is strong!")
    
if __name__ == "__main__":
    main()
