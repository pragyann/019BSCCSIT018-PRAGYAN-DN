from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime, timedelta

def get_server_time():
    # Add delay to server
    return datetime.now().__add__(timedelta(minutes=15))

server = SimpleXMLRPCServer(('localhost', 8000))
server.register_function(get_server_time, 'get_server_time')

print('Server is listening on port 8000')
server.serve_forever()
