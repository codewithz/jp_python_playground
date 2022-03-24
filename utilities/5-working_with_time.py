import time

print(time.time())

def send_email():
    for i in range(100000):
        pass

start=time.time()
send_email()
end=time.time()

duration=end-start

print("Duration:",duration)
