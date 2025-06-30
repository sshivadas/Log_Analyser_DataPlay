from datetime import datetime

def parse_logs(logs):
    parsed_logs = []
    raw_logs = logs.strip().splitlines()
    for i,log in enumerate(raw_logs,1):
        try:
            log_parts = log.split()
            if len(log_parts) < 5:
                print(f"Log {i} skipped (malformed): {log}")
                continue  # Skip malformed lines
            log_timestamp = get_timestamp(log_parts[0], log_parts[1])
            log_user_id = log_parts[2]
            log_user_activity = log_parts[3]
            log_user_role = get_user_roles(log_parts[-1])
            log_user_activity_detail =  log_parts[4] if len(log_parts) == 6 else ""
            
            parsed_logs.append({
                'timestamp': log_timestamp,
                'user_id': log_user_id,
                'activity': log_user_activity,
                'activity_detail': log_user_activity_detail,
                'roles': log_user_role
            })
        except Exception as e:
            print(f"Log {i} failed: {e}")
            continue
    return parsed_logs
       

def get_timestamp(date_part, time_part):
    # convert to datetime object
    try:
        timestamp = datetime.strptime(f"{date_part[1:11]} {time_part[:8]}", '%Y-%m-%d %H:%M:%S')
        return timestamp
    except ValueError as e:
        print(f"[Timestamp Error] Failed to parse: {date_part} {time_part} | Error: {e}")
        return None

def get_user_roles(user_role_part):
    #multiple user role parsing
    return user_role_part.split(",") if "," in user_role_part else user_role_part
