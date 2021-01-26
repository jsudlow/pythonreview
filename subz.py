import subprocess
import threading

def worker(num):
    """thread worker function"""
    print("Worker: %s" % num)
    HTML = subprocess.check_output("node puppet.js https://brickseek.com/deals/?pg=" + str(num))

    print("===========================@^@^@^@^@^@@^====================")
    text = str(HTML)[2:-1]

    print('going to brickseak',num)

    return

threads = []
for i in range(1,4):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()



