import xmlrpc.client
from datetime import datetime

def calculate_time_difference(client_time, server_time):
    time_difference = abs((client_time - server_time).total_seconds()) / 60
    return round(time_difference)

serverProxy = xmlrpc.client.ServerProxy('http://localhost:8000')

client_time = datetime.now()

server_time = serverProxy.get_server_time()

if not isinstance(server_time, datetime):
    server_time = datetime.strptime(server_time.value, "%Y%m%dT%H:%M:%S")

print("Time from server:", server_time.strftime("%Y-%m-%d %H:%M:%S"))

time_difference = calculate_time_difference(client_time, server_time)

print("Client time:", client_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Server time:", server_time.strftime("%Y-%m-%d %H:%M:%S"))
print("Difference in time:", time_difference, "minutes")
