"""Bank Account.

Current locking mechanism implemented assuming accessed from multiple threads. Otherwise GIL might assure no such problems for this code.
"""
import threading


class BankAccount:
    """Bank account managment."""
    
    def __init__(self):
        self._lock = threading.Lock()
        self._balance = None

    def get_balance(self) -> int:
        """Retrieve account's balance."""
        with self._lock:
            self.is_possible()
            return self._balance

    def open(self):
        """Open closed account with 0 balance."""
        with self._lock:
            if self._balance is not None:
                raise ValueError('account already open')
            self._balance = 0

    def deposit(self, amount: int):
        """Deposit into account."""
        with self._lock:
            self.is_possible(amount)
            self._balance += amount

    def withdraw(self, amount: int):
        """Withdraw from account."""
        with self._lock:
            self.is_possible(amount, True)
            self._balance -= amount

    def close(self):
        """Close account."""
        with self._lock:
            self.is_possible()
            self._balance = None

    def is_possible(self, transaction_value: int | None = None, up_to_balance: bool = False) -> bool: 
        """Check if action is possible.

        :param transaction_value: if given, check it'a a positive amount
        :param up_to_balance: [optional] check amount is up to balance
        :raises ValueError: if checks fail
        :returns: True if validated and lock acquire
        """
        if self._balance is None:
            raise ValueError('account not open')
        if transaction_value is not None and transaction_value < 1:
            raise ValueError('amount must be greater than 0')
        if up_to_balance and transaction_value > self._balance:
            raise ValueError('amount must be less than balance')

        return True
