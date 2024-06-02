class RoutdRobin(object):

    def __init__(self, servers):
        self.servers = servers
        self.current_index = 1
    
    def get_next_server(self):
        self.current_index = (self.current_index +1) % (self.servers)
        return self.servers[self.current_index]


servers = ['server1', 'server2', 'server3']
lb = RoutdRobin(servers=servers)

for i in range(6):
    server = lb.get_next_server()
    print(f"Request: {i + 1} -> {server}")
