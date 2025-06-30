def decompose_seconds(total_duration):
    total_seconds = int(total_duration.total_seconds())
    days = total_seconds // (24 * 3600)
    remaining = total_seconds % (24 * 3600)
    hours = remaining // 3600
    remaining %= 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return days,hours, minutes, seconds