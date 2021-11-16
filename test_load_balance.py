"""
    test_load_balance.py - for pytest use...
"""

import load_balance


def test_min_ticks_lower():
    """Min ticks test"""
    balance = load_balance.Balance()
    assert balance.do_balance(0, 2, [0]) is None


def test_man_ticks_lower():
    """Max ticks test"""
    balance = load_balance.Balance()
    assert balance.do_balance(11, 2, [0]) is None


def test_min_user_server_lower():
    """Min user test"""
    balance = load_balance.Balance()
    assert balance.do_balance(2, 0, [0]) is None


def test_max_user_lower():
    """Max user test"""
    balance = load_balance.Balance()
    assert balance.do_balance(2, 11, [0]) is None


def test_correct_behavior():
    """Test if is working"""
    balance = load_balance.Balance()
    assert balance.do_balance(4, 2,  ['1\n', '3\n', '0\n', '1\n', '0\n', '1\n']) == ['1', '2,2', '2,2', '2,2,1', '1,2,1', '2', '2', '1', '1', '0', '15']


def test_user_invalid_on_list():
    """Test and invalid user on user list """
    balance = load_balance.Balance()
    assert balance.do_balance(4, 2,  ['1\n', '3\n', '0\n', 'invalid', '1\n', '0\n', '1\n']) == ['1', '2,2', '2,2', '2,2,1', '1,2,1', '2', '2', '1', '1', '0', '15']
