"""servers.py: This file describes server functions an classes
"""

def get_server_borders(num_ticks, max_users):
    """Tests if max_users borders"""

    if num_ticks < 1 or num_ticks > 10 or max_users < 1 or max_users > 10:
        return False
    return True


