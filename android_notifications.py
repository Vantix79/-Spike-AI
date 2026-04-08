import os

def send_notification(title, message):
    os.system(f'termux-notification --title "{title}" --content "{message}"')

if __name__ == "__main__":
    send_notification("Alert", "This is a test notification from Termux API.")