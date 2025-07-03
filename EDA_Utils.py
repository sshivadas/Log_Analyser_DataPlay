from Time_utils import *

def get_all_users(parsed_logs):
    all_users = [ log["user_id"] for log in parsed_logs]
    return all_users

def get_all_activities(parsed_logs):
    all_activities = [ log["activity"] for log in parsed_logs]
    return all_activities

def get_all_user_roles(parsed_logs):
    all_user_roles = [log["roles"] for log in parsed_logs]
    return all_user_roles

def get_activities_per_user(parsed_logs, user_id):
    all_activities_per_user = [ log["activity"] for log in parsed_logs if log["user_id"] == user_id]
    return all_activities_per_user

def get_all_logs_per_user(parsed_logs, user_id):
    all_logs_per_user = [log for log in parsed_logs if log["user_id"] == user_id]
    return all_logs_per_user

def formatted_logs(parsed_logs):
    for log in parsed_logs:
        if log['activity'].lower() == 'login':
            if log['activity_detail'].lower() == 'success':
                print(f"User {log['user_id']} successfully logged in as {log['roles']} - {log['timestamp']}")
            else:
                print(f"User {log['user_id']} login as {log['roles']} failed. - {log['timestamp']} ")
        elif log['activity'].lower() == 'view_page':
            print(f"User {log['user_id']} viewed page  {log['activity_detail']} - {log['timestamp']}")
        elif log['activity'].lower() == "logout":
            print(f"User {log['user_id']} logged out as {log['roles']} - {log['timestamp']}")
        elif log['activity'].lower() == 'edit_profile':
            print(f"User {log['user_id']} edited a profile. - {log['timestamp']}") 
    return None

def formatted_logs_streamlit(logs):
    formatted_logs_list =[]
    for log in logs:
        if log['activity'].lower() == 'login':
            if log['activity_detail'].lower() == 'success':
                formatted_logs_list.append(f"User {log['user_id']} successfully logged in as {log['roles']} - {log['timestamp']}")
            else:
                formatted_logs.append(f"User {log['user_id']} login as {log['roles']} failed. - {log['timestamp']} ")
        elif log['activity'].lower() == 'view_page':
            formatted_logs_list.append(f"User {log['user_id']} viewed page  {log['activity_detail']} - {log['timestamp']}")
        elif log['activity'].lower() == "logout":
            formatted_logs_list.append(f"User {log['user_id']} logged out as {log['roles']} - {log['timestamp']}")
        elif log['activity'].lower() == 'edit_profile':
            formatted_logs_list.append(f"User {log['user_id']} edited a profile. - {log['timestamp']}") 
    return formatted_logs_list

def get_logs_timeframe(logs):
        all_timestamps = [ log["timestamp"] for log in logs]
        max_timestamp = max(all_timestamps)
        min_timestamp = min(all_timestamps)
        total_timeframe = max_timestamp - min_timestamp
        days, hrs, mins, secs = decompose_seconds(total_timeframe)
        total_duration = {"days": days,
                                "hours": hrs,
                                "minutes": mins,
                                "seconds": secs,
                                "start" :min_timestamp,
                                "end" : max_timestamp
                                }
        return total_duration
