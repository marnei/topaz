"""
    Main program for load balance in servers use.

    USAGE: python3 main.py <input.txt> <output.tx>
"""


import sys
import load_balance

if __name__ == '__main__':
    """
        sys.argv[1] is file input
        sys.argv[2] is file output

        Read from file input:
        Line 1 number of ticks per user task
        Line 2 number of users allowed per server
        Other lines number of new users per tick

        Return in file output:
        In each line the number of current users for server,
        each server separated by a comma.
        The line last represent cost. Cost is the sum of each line cost.

"""

    try:
        file_input = open(sys.argv[1], 'r')
        open(sys.argv[2], 'w').close()
        # Cleaning output file
        file_output = open(sys.argv[2], 'w')
        num_ticks_task = int(file_input.readline())
        max_server_users = int(file_input.readline())
        if not load_balance.get_server_borders(num_ticks_task, max_server_users):
            sys.exit('ERROR: Wrong server file parameter border')
    except Exception as erro:
        sys.exit('ERROR:{}'.format(erro))

    load_balance = load_balance.Balance(num_ticks_task, max_server_users)
    while load_balance.ticks_count:
        users_to_add = file_input.readlines()
        for num_users in users_to_add:
            try:
                num_users_int = int(num_users)
                if num_users_int:
                    load_balance.add_new_users(num_users_int)
                else:
                    if load_balance.ticks_count > 1:
                        load_balance.ticks_count = load_balance.ticks_count - 1
                line = load_balance.do_tick()
                file_output.write(line + '\n')
            except Exception as erro:
                print('ERROR:{}'.format(erro))
        line = load_balance.do_tick()
        file_output.write(line + '\n')
        load_balance.ticks_count = load_balance.ticks_count - 1
    file_output.write(load_balance.get_cost() + '\n')
    file_output.close()
    file_input.close()
    sys.exit('DONE')
