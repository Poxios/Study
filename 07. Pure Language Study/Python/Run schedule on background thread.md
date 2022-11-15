# Run schedule on background thread
```python
import schedule
import telebot
from threading import Thread
from time import sleep

TOKEN = "Some Token"

bot = telebot.TeleBot(TOKEN)
some_id = 12345 # This is our chat id.

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    return bot.send_message(some_id, "This is a message to send.")

if __name__ == "__main__":
    # Create the job in schedule.
    schedule.every().saturday.at("07:00").do(function_to_run)

    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start() 

    # And then of course, start your server.
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
```

* https://stackoverflow.com/questions/48288124/how-to-send-message-in-specific-time-telegrambot