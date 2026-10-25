import time

import story


def start_game():
    print(story.Prolog)
    time.sleep(1)
    mainroom()


def mainroom():
    hat_passwort = False
    hat_master_code = False

    print(story.Room)

    while True:
        decision = input(
            "\nWhat do you want to do? "
            "(type 'read note', 'use terminal' or 'open door'): "
        ).strip().lower()

        if "note" in decision:
            print(story.NOTE_TEXT)
            hat_passwort = True
        elif "terminal" in decision:
            print("\n--- TERMINAL LOGIN ---")
            if not hat_passwort:
                print("Access Denied. You need a password to decrypt files.")
                continue

            eingabe_pw = input("Enter password to read 'hints.txt': ").strip().lower()
            if eingabe_pw == "cybersec":
                print(story.HINT_TEXT_CONTENT)
                hat_master_code = True
            else:
                print("\nWrong password! Terminal locked.")
        elif "door" in decision:
            if not hat_master_code:
                print("\nThe door is locked. You need a 4-digit code to open it.")
                continue

            code = input("\nEnter the 4-digit Master Code: ").strip()
            if code == "2026":
                print("\n*KLICK* ... ACCESS GRANTED!")
                print("The heavy electronic door slides open. You escaped the Hack-Lab!")
                print("\nCongratulations! You have completed the Terminal Escape Game!")
            else:
                print("\nWRONG CODE! The system resets. GAME OVER.")
            break
        else:
            print(
                "\nI don't understand that command. Try 'read note', "
                "'use terminal' or 'open door'."
            )


if __name__ == "__main__":
    start_game()
