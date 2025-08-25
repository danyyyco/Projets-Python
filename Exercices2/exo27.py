def convert_seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

total_seconds = 3665
hours, minutes, seconds = convert_seconds_to_hms(total_seconds)
print(f"{total_seconds} secondes correspond à {hours} heures, {minutes} minutes et {seconds} secondes.")
