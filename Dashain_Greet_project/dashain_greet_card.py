
import streamlit as st
import time

# Function to simulate typing animation
def slow_print(text, delay=0.05):
    placeholder = st.empty()
    msg = ""
    for char in text:
        msg += char
        placeholder.markdown(msg)
        time.sleep(delay)

# Dashain banner
def dashain_banner():
    st.markdown("✨🎉" + "="*50 + "🎉✨")
    slow_print("      🪁 HAPPY DASHAIN 2082 🪁")
    st.markdown("✨🎉" + "="*50 + "🎉✨")

def dashain_art():
    st.markdown("🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱")
    st.markdown("🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱")
    st.markdown("🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱")
    st.markdown("🪁     🪁")
    st.markdown("🎊    👨‍👩‍👧‍👦    🎊")

# Greeting message
def greet(name):
    slow_print(f"Namaste {name}! 🙏", 0.06)
    slow_print("On this Dashain, may your days be filled with:", 0.04)
    slow_print("✨ Happiness\n✨ Prosperity\n✨ Peace\n✨ Blessings from elders", 0.05)
    slow_print("Enjoy tika, jamara, kites, and family gatherings ❤️", 0.05)
    slow_print("👉 Celebrate responsibly and spread love 💖", 0.05)

st.set_page_config(page_title="Dashain Greeting Card", page_icon="🪁")

dashain_banner()
name = st.text_input("Enter your name to receive a greeting:")

if name:
    dashain_art()
    greet(name)
    st.balloons() 
    st.markdown("✨🎉" + "="*50 + "🎉✨")
    st.markdown("🎉 Happy Dashain to You & Your Family 🎉")

    st.markdown("🎉✨- Asmin Shrestha ✨🎉")

    st.markdown("✨🎉" + "="*50 + "🎉✨")
