""""
    load_balance.py  Responsable for load balance users in servers
"""
import operator

SERVER_MAX_TICKS = 10
SERVER_MIN_TICKS = 1
SERVER_MAX_USERS = 10
SERVER_MIN_USERS = 1
SERVER_TICK_COST = 1


class Balance:
    """
        Do balance in servers.
        ticks_user is number of ticks for user task
        max_urers is max number of users per server.

        Must do load balance allocating users in servers for low cost
    """
    def __init__(self):
        self.ticks_count = 1
        self.cost = 0
        self.servers_list = []
        self.users_list = []
        self.output_list = []
        self.ticks_users = 0
        self.max_users = 0
        self.best_server_list = []

    def do_balance(self, ticks_user, max_users, new_users_list):
        """
            Do load balane in servers.

            Input: number o tick for user tast,
            max users per server and a list of
            nww users per tick
            Output: A list containing servers users
            separated by comma and at least the total cost
        """

        try:
            max_users = int(max_users)
            ticks_user = int(ticks_user)
        except Exception as erro:
            return None
        if max_users < SERVER_MIN_USERS or max_users > SERVER_MAX_USERS:
            return None
        if ticks_user < SERVER_MIN_TICKS or ticks_user > SERVER_MAX_TICKS:
            return None
        self.ticks_users = ticks_user
        self.max_users = max_users
        while self.ticks_count:
            # Must add the number of users in each item list one tick.
            for num_users in new_users_list:
                try:
                    num_users_int = int(num_users)
                    line = self.do_tick()
                    if num_users_int < 0:
                        print('ERROR:{}'.format('Invalid value'))
                        continue
                    if num_users_int:
                        self.add_new_users(num_users_int)
                    else:
                        if self.ticks_count > 1:
                            self.ticks_count = self.ticks_count - 1
                    # after do tick and add new user, add info from servers to output list.
                    if self.servers_list:
                        tick_server_info = ''
                        for index, server in enumerate(self.servers_list):
                            if index == 0:
                                tick_server_info = str(server.users)
                            else:
                                tick_server_info = tick_server_info + ',' \
                                                   + str(server.users)
                    else:
                        tick_server_info = '0'
                    self.cost = self.cost + (SERVER_TICK_COST * len(self.servers_list))
                    self.output_list.append(tick_server_info)
                except Exception as erro:
                    print('ERROR:{}'.format('Invalid value'))
            # do_trick must go to output list
            new_users_list.clear()
            line = self.do_tick()
            self.cost = self.cost + (SERVER_TICK_COST * len(self.servers_list))
            self.output_list.append(line)
            self.ticks_count = self.ticks_count - 1
        # At the end add cost
        self.output_list.append(str(self.cost))

        return self.output_list

    def add_new_users(self, users):
        """
            Add users to user list. Each user is allocated in a server
        """

        self.ticks_count = self.ticks_users
        # number of ticks to complete all tasks at end of users list
        for i in range(users):  # Add each user to low cost server.
            server = self.get_best_server()
            server.tick_counter = 0
            user = User(server, self.ticks_users)
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
            # to each user decrement task tick counter. I zero, remove user from server.
            # If server is empty remove server
            user.task_tick = user.task_tick - 1
            if user.task_tick == 0:
                user.server.users = user.server.users - 1
                if user.server.users == 0:
                    self.servers_list.remove(user.server)
                self.users_list.remove(user)
        if self.servers_list:
            tick_server_info = ''
            self.best_server_list.clear()
            # list all severs available
            for index, server in enumerate(self.servers_list):
                if server.users < self.max_users:
                    self.best_server_list.append(server)
                if index == 0:
                    tick_server_info = str(server.users)
                else:
                    tick_server_info = tick_server_info + ','\
                                       + str(server.users)
                server.tick_counter = server.tick_counter + 1
        else:
            tick_server_info = '0'
        # order list of servers. Best is first one.
        self.best_server_list.sort(key=operator.attrgetter('tick_counter'))

        return tick_server_info

    def get_best_server(self):
        """
            Looking for best server.
            Best server is index 0 in list. If reach max users to a server, remove.
            If list is empty create a new server and return it.
        """

        if self.best_server_list:
            self.best_server_list[0].users = self.best_server_list[0].users + 1
            best_server = self.best_server_list[0]
            if best_server.users >= self.max_users:
                self.best_server_list.remove(best_server)
        else:
            best_server = Server()
            self.servers_list.append(best_server)
            self.best_server_list.append(best_server)
        return best_server

    def get_cost(self):
        """return cost to print"""

        return str(self.cost)


class Server:
    """
        Server resources control
    """

    def __init__(self):
        self.users = 1
        self.tick_counter = 0


class User:
    """
        Users resource control
    """

    def __init__(self, server, task_tick):
        self.server = server
        self.task_tick = task_tick
