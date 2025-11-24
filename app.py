import streamlit as st
import os
from dotenv import load_dotenv
from agents.researcher import ResearcherAgent
from agents.planner import PlannerAgent

# Page Config
st.set_page_config(page_title="Nomad AI Concierge", page_icon="🌍")

# Load environment variables
load_dotenv()

# --- HEADER ---
st.title("🌍 Nomad: AI Travel Concierge")
st.markdown("""
Welcome to **Nomad**. I am an AI Agent system designed to plan your perfect trip.
I use **Google Gemini 2.0** and **DuckDuckGo** to find real-time info and build a custom itinerary.
""")

# --- SIDEBAR (User Inputs) ---
with st.sidebar:
    st.header("Trip Details")
    destination = st.text_input("Destination", "Paris")
    days = st.number_input("Duration (Days)", min_value=1, max_value=14, value=3)
    
    st.divider()
    
    # API Key handling for Deployment
    # If looking for a key in secrets (Cloud) or .env (Local)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        api_key = st.text_input("Enter Gemini API Key", type="password")
        if api_key:
            os.environ["GEMINI_API_KEY"] = api_key

# --- MAIN LOGIC ---
if st.button("🚀 Plan My Trip"):
    if not os.environ.get("GEMINI_API_KEY"):
        st.error("Please provide a Google Gemini API Key to proceed.")
        st.stop()
    
    # Initialize Agents
    researcher = ResearcherAgent()
    planner = PlannerAgent()

    # Create a status container
    with st.status("🤖 Agents are working...", expanded=True) as status:
        
        # Step 1: Research
        st.write("🕵️‍♂️ **Scout (Researcher)** is searching real-time data...")
        try:
            research_summary = researcher.perform_research(destination)
            st.write("✅ Research Complete.")
            with st.expander("See Raw Research Data"):
                st.write(research_summary)
        except Exception as e:
            st.error(f"Research failed: {e}")
            st.stop()

        # Step 2: Planning
        st.write("🗺️ **Atlas (Planner)** is building the itinerary...")
        try:
            final_plan = planner.create_itinerary(research_summary, days)
            status.update(label="Itinerary Ready!", state="complete", expanded=False)
        except Exception as e:
            st.error(f"Planning failed: {e}")
            st.stop()

    # --- OUTPUT ---
    st.divider()
    st.subheader(f"📅 Your {days}-Day Itinerary for {destination}")
    st.markdown(final_plan)