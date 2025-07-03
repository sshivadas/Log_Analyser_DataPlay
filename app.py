import streamlit as st
from PIL import Image
from collections import Counter
from Parse_Utils import parse_logs
from EDA_Utils import get_all_users,get_all_logs_per_user, get_logs_timeframe, formatted_logs_streamlit
from Session_Utils import identify_sessions


st.set_page_config(page_title="Log Analyzer", layout="wide")
logo = Image.open("DP.jpg")
col1, col2 = st.columns([1, 5])
with col1:
    st.image("DP.jpg", width=156)
with col2:
    st.title("Log Analyzer")


# Cached wrapper for parselogs
@st.cache_data
def get_parsed_logs(raw_text):
    return parse_logs(raw_text)

def styled_header(text, tag="h4", color="black", underline=False, bold=True):
    style = f"{'text-decoration: underline;' if underline else ''} color: {color}; font-weight: {'bold' if bold else 'normal'};"
    st.markdown(f"<{tag} style='{style}'>{text}</{tag}>", unsafe_allow_html=True)

# --- Input Logs ---
input_logs = st.text_area("Paste your log entries here (max ~50):", height=300)
#analyze_button = st.button("🔍 Analyze Logs")

if input_logs:
    # Parse Logs 
    parsed_logs = get_parsed_logs(input_logs)
    active_users = list(set(get_all_users(parsed_logs)))
    #Dropdown for users
    selected_user = st.selectbox("Select a user (or 'All')", ['All'] + active_users)
    # Filter by selected user
    if selected_user != "All":
        try:
            filtered_logs = get_all_logs_per_user(parsed_logs,selected_user)
            total_log_duration = get_logs_timeframe(filtered_logs)
            styled_header(f"User activity was seen from {total_log_duration['start']} to {total_log_duration['end']}")
            st.write(f"A total of {total_log_duration['days']} days, {total_log_duration['hours']} hours, {total_log_duration['minutes']} minutes and {total_log_duration['seconds']} seconds")
            user_logs = formatted_logs_streamlit(filtered_logs)
            for log in user_logs:
                st.write(log)        
            styled_header(f"Session wise activity of user {selected_user}:")
            activities_per_user =[log['activity'] for log in filtered_logs] 
            # Count frequencies of all activites
            activity_counter = Counter(activities_per_user)
            styled_header(f"User Activity Summary:")
            for item, count in activity_counter.items():
                st.write(f"{item}: {count}")

            styled_header("Session wise activities of the user:")
            user_sessions = identify_sessions(activities_per_user)        
            for session_id,session_activities in user_sessions.items():
                st.write(f"Activites in session {session_id}: {session_activities}")
                # Count frequencies
                session_activity_counter = Counter(session_activities)
                # Find the max frequency
                max_count = max(session_activity_counter.values())
                # Get all actions that have this max frequency
                most_frequent_activity = [activity for activity, count in session_activity_counter.items() if count == max_count]
                st.write(f"The most frequent activity is {most_frequent_activity}")
        except Exception as e:
            st.error(f"❌ Failed to call parse_logs: {e}")
    else:
        
        try:
            total_log_duration = get_logs_timeframe(parsed_logs)
            styled_header(f"Total log duration {total_log_duration['start']} to {total_log_duration['end']}")
            st.write(f"A total of {total_log_duration['days']} days, {total_log_duration['hours']} hours, {total_log_duration['minutes']} minutes and {total_log_duration['seconds']} seconds")
            all_logs = formatted_logs_streamlit(parsed_logs)
            #for log in all_logs:
                #st.write(log)
            all_activites = [log['activity'] for log in parsed_logs]
            # Count frequencies of all activites
            all_activity_counter = Counter(all_activites)
            styled_header(f"Activity Summary:")
            for item, count in all_activity_counter.items():
                st.write(f"{item}: {count}")
        except Exception as e:
            st.error(f"❌ Failed to call parse_logs: {e}")
else: 
    styled_header("Please Input log data in the given text area")
        
        
        
