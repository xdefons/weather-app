from datetime import datetime
import os

def logs():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    place = os.environ.get("CITY")

    try:

        with open("logs.txt","a") as l:
            l.write(f"{now} Pobrano dane pogodowe dla {place}\n")

    except Exception as e:
        with open("logs.txt","a") as l:
            l.write(f"{now} Błąd dla {place}: {e}\n")

def logs_read():
    with open("logs.txt","r", encoding="utf8") as my_file:
        content = my_file.read()
        print(content)

