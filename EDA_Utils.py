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
    all_logs_per_user = [(log["activity"],log["activity_detail"], log["roles"]) for log in parsed_logs if log["user_id"] == user_id]
    return all_logs_per_user

#def get_formatted_logs_per_user(parsed_log, user_id):
   # logs_per_user = 
     

