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
    except Exception as erro:
        sys.exit('ERROR:{}'.format(erro))

    num_ticks_task = file_input.readline()
    max_server_users = file_input.readline()
    new_users_list = file_input.readlines()

    l_balance = load_balance.Balance()
    output_list = l_balance.do_balance(num_ticks_task.replace('\n', ''),
                                       max_server_users.replace('\n', ''), new_users_list)
    if output_list:
        for info in output_list:
            file_output.write(info + '\n')
        err = 0
    else:
        err = 1
    file_output.close()
    file_input.close()
    if err:
        sys.exit('ERROR')
    else:
        sys.exit('DONE')
