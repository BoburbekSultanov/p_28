import time
import threading

from pythonProject1.module_3.Lesson_2.sendemail.send_messange import password


def send_email(receiver_email):
    time.sleep(2.5)
    print("Finish")


start = time.time()
threads = []

for email in range(100000):
    t = threading.Thread(target=send_email, args=(email,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

print(time.time() - start)
