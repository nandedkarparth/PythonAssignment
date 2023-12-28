
class InvalidDepositAmountError(Exception):
    def __init__(self, message="Invalid deposit amount"):
        self.message = message
        super().__init__(self.message)


class InvalidWithdrawalAmountError(Exception):
    def __init__(self, message="Invalid withdrawal amount"):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds for withdrawal"):
        self.message = message
        super().__init__(self.message)
