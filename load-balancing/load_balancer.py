import random
import time


class LoadBalancer:
    def __init__(self, servers, strategy="round_robin"):
        if not servers:
            raise ValueError("The server list cannot be empty.")
        
        self.servers = servers
        self.strategy = strategy
        self.index = 0
        self.server_loads = {server: 0 for server in servers}  # Used for least connections or weighted algorithms

    def get_next_server(self):
        if self.strategy == "round_robin":
            return self._round_robin()
        elif self.strategy == "least_connections":
            return self._least_connections()
        elif self.strategy == "random":
            return self._random()
        else:
            raise ValueError("Unknown strategy specified.")

    def _round_robin(self):
        
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

    def _least_connections(self):
        
        server = min(self.server_loads, key=self.server_loads.get)
        self.server_loads[server] += 1
        return server

    def _random(self):
        
        return random.choice(self.servers)

    def release_server(self, server):
        
        if self.strategy == "least_connections" and server in self.server_loads:
            self.server_loads[server] -= 1
        else:
            print("No action needed for this strategy.")


# Example usage
if __name__ == "__main__":
    servers = ["Server1", "Server2", "Server3", "Server4"]
    
    lb = LoadBalancer(servers, strategy="least_connections")

    # Simulate 10 incoming requests with a delay
    for i in range(10):
        next_server = lb.get_next_server()
        print(f"Request {i + 1} sent to {next_server}")
        
        # Simulate request processing time with a delay
        time.sleep(2)  # Delay of 2 seconds for each request to simulate slow processing

        # After each request, we simulate that the server is done processing the request
        lb.release_server(next_server)


