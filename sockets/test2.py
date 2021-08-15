import socket
import time

start = time.perf_counter()
for i in range(1, 10000000):
    try:
        PORT = i
        SERVER = '120.138.12.113'
        ADDRESS = (SERVER, PORT)
        server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        server.bind(ADDRESS)
    except:
        pass
    else:
        print('golden port: ', i)
end = time.perf_counter()
print(end-start)
