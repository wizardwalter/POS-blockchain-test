from inspect import signature
from transaction import Transaction
from wallet import Wallet

if __name__ == '__main__':

    sender = "sender"
    reciever = "reciever"
    amount = 1
    type = "TRANSFER"

    transaction = Transaction(sender, reciever, amount, type)
    
    wallet = Wallet()
    signature = wallet.sign(transaction.toJson())
    transaction.sign(signature)
    print(transaction.toJson())