"""load_balance.py  Responsable for load balance users in servers"""


class Balance:
    """
        Do balance in servers.
        ticks_user is number of ticks for user task
        max_urers is max number of users per server.

        Must do load balance allocating users in servers for low cost
    """
    def __init__(self, ticks_user, max_users):
        self.ticks_users = ticks_user
        self.max_users = max_users
        self.ticks_count = 1
        self.cost = 0
        self.servers_list = []

    def add_new_users(self, users):
        """
            Add users to user list. Each user is allocated in a server
        """

        self.ticks_count = self.ticks_users # number of ticks to complete all tasks at end of users list
        for i in range(users): # Add each user to low cost server.
            self.servers_list.append(self.get_best_server())

    def do_tick(self):
        self.cost = self.cost + 1

    def get_best_server(self):
        """
            Looking for best server. Best server is not full with more number of users.
        """

        best_server = None
        if self.servers_list:
            for server in self.servers_list:
                if server.users < self.max_users:
                    if server.users+1 == self.max_users: # If this server is full with one more user this is almost full so, is the best
                        return server
                    if best_server and best_server.users < server.users:
                        best_server = server
                    if not best_server:
                        best_server = server
        if best_server is None:
            best_server = Server()
        return best_server


class Server:
    """
        Server resources control
    """

    def __init__(self):
        self.users = 0


class User:

    def __init__(self, server, task_tick):
        self.server = server
        self.task_tick = task_tick

