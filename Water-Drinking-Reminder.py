import time
from plyer import notification

def water_drinking_reminder():
    while True:
        notification.notify(
            title="Water Reminder for Muskan",
            message="Time to drink some water! Stay hydrated.",
            timeout=10  # Notification will stay for 10 seconds
        )
        time.sleep(3600)  # Wait for 1 hour before sending the next reminder
        

water_drinking_reminder()