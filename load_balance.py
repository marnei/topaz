""""
    load_balance.py  Responsable for load balance users in servers
"""

SERVER_MAX_TICKS = 10
SERVER_MIN_TICKS = 1
SERVER_MAX_USERS = 10
SERVER_MIN_USERS = 1
SERVER_TICK_COST = 1


def get_server_borders(num_ticks, max_users):
    """Tests if max_users borders"""

    if num_ticks < SERVER_MIN_TICKS or num_ticks > SERVER_MAX_TICKS \
            or max_users < SERVER_MIN_USERS or max_users > SERVER_MAX_USERS:
        return False
    return True


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
        self.users_list = []

    def add_new_users(self, users):
        """
            Add users to user list. Each user is allocated in a server
        """

        self.ticks_count = self.ticks_users
        # number of ticks to complete all tasks at end of users list
        for i in range(users):  # Add each user to low cost server.
            server = self.get_best_server()
            user = User(server, self.ticks_users)
            user.server.users = user.server.users + 1
            self.users_list.append(user)

    def do_tick(self):
        """
            For each tick decrement users task ticks count.
            If task done, remove user from server. If servers users count
            is null, then remove server.

            return tick servers info.
        """

        copy_users_list = self.users_list.copy()
        for user in copy_users_list:
            if user.task_tick == 0:
                user.server.users = user.server.users - 1
                if user.server.users == 0:
                    self.servers_list.remove(user.server)
                self.users_list.remove(user)
            user.task_tick = user.task_tick - 1
        self.cost = self.cost + (SERVER_TICK_COST * len(self.servers_list))
        if self.servers_list:
            tick_server_info = ''
            for index, server in enumerate(self.servers_list):
                if index == 0:
                    tick_server_info = str(server.users)
                else:
                    tick_server_info = tick_server_info + ','\
                                       + str(server.users)
                server.tick_counter = server.tick_counter + 1
        else:
            tick_server_info = '0'
        return tick_server_info

    def get_best_server(self):
        """
            Looking for best server.
            Best server is not full with more number
            of users or a new one if all is full.
        """

        best_server = None
        if self.servers_list:
            for server in self.servers_list:
                if server.users < self.max_users:
                    if best_server:
                        if best_server.users < server.users:
                            # Number of users is greater.
                            best_server = server
                        if best_server.users == server.users \
                                and \
                                best_server.tick_counter > server.tick_counter:
                            # Number of users is same
                            # but this server is newer.
                            best_server = server
                    if not best_server:
                        best_server = server
        if best_server is None:  # All servers full or no server on list
            best_server = Server()
            self.servers_list.append(best_server)
        return best_server

    def get_cost(self):
        """return cost to print"""

        return str(self.cost)


class Server:
    """
        Server resources control
    """

    def __init__(self):
        self.users = 0
        self.tick_counter = 0


class User:

    def __init__(self, server, task_tick):
        self.server = server
        self.task_tick = task_tick
