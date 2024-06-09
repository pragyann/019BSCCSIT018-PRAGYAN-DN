import threading

# Global variables
file_lock = threading.Lock()
shared_file = "shared_file.txt"

def node1():
    global file_lock
    global shared_file
    with file_lock:
        with open(shared_file, 'a+') as f:
            f.seek(0)
            content = f.read()
            print("Node 1 reads:", content)
            f.write("\nNode 1 updated")
            print("Node 1 writes:", "Node 1 updated")

def node2():
    global file_lock
    global shared_file
    with file_lock:
        with open(shared_file, 'a+') as f:
            f.seek(0)
            content = f.read()
            print("Node 2 reads:", content)
            f.write("\nNode 2 updated")
            print("Node 2 writes:", "Node 2 updated")

if __name__ == "__main__":
    t1 = threading.Thread(target=node1)
    t2 = threading.Thread(target=node2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
