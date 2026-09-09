# my timer.py file is a simple timer that counts down from a specified number of seconds and prints the remaining time to the console. It uses the time module to handle the countdown and sleep for one second between each decrement. The timer can be started by calling the start_timer function with the desired number of seconds as an argument.
# my 4th project

import time


def countdown(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print("\nTIME'S UP ! ! !")


seconds = int(input("ENTER THE NUMBER OF SECONDS ! ! ! : "))
countdown(seconds)