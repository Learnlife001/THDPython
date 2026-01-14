def seconds_to_minutes(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return minutes, remaining_seconds

seconds = int(input("Enter number of seconds: "))

minutes, remaining_seconds = seconds_to_minutes(seconds)
print(f"{seconds} seconds is equal to {minutes} minutes and {remaining_seconds} seconds.")