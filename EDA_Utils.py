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
    all_logs_per_user = [[log["activity"],log["activity_detail"], log["roles"], log["timestamp"]] for log in parsed_logs if log["user_id"] == user_id]
    return all_logs_per_user

def formatted_logs(logs_per_user, user_id):
    print(f"log breakdown of user {user_id}:")
    for log in logs_per_user:
        if log[0].lower() == 'login':
            if log[1].lower() == 'success':
                print(f"User successfully logged in as {log[2]} - {log[3]}")
            else:
                print(f"User login as {log[2]} failed. - {log[3]} ")
        elif log[0].lower() == 'view_page':
            print(f"User viewed page  {log[1]} - {log[3]}")
        elif log[0].lower() == "logout":
            print(f"User logged out as {log[2]} - {log[3]}")
        elif log[0].lower() == 'edit_profile':
            print(f"User edited a profile. - {log[3]}") 
    return None

def get_all_logs_timeframe(parsed_logs):
        all_timestamps = [ log["timestamp"] for log in parsed_logs]
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
