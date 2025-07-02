def identify_sessions(user_activites):
    all_user_sessions = {}
    session_counter = 1
    current_session = []
    for activity in user_activites:
        if activity.lower() in ['login', 'logout']:
            if len(current_session) > 0:
                # End previous session at this login or logout
                all_user_sessions[session_counter] = current_session
                session_counter += 1
            # start new session
            current_session = []
        else:
            current_session.append(activity)
    if len(current_session) > 0:
        all_user_sessions[session_counter] = current_session
    return all_user_sessions


                





