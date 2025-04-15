import time
import datetime
import winsound  # For Windows

# Function to play the alarm sound (replace with your preferred sound)
def play_alarm_sound():
    winsound.Beep(1000, 2000)  # Beep for 2 seconds at 1000 Hz

# Get the alarm time from the user
while True:
    try:
        alarm_hour = int(input("Enter alarm hour (24-hour format): "))
        alarm_minute = int(input("Enter alarm minute: "))
        break
    except ValueError:
        print("Invalid input. Please enter integers.")

# Main loop to check the time
while True:
    current_time = datetime.datetime.now()
    current_hour = current_time.hour
    current_minute = current_time.minute

    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("Wake up!")
        play_alarm_sound()
        break  # Stop the loop after the alarm goes off

    time.sleep(1)  # Check the time every second

print("Alarm set.")
