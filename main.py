from inspect import signature
from transaction import Transaction
from wallet import Wallet
from TransactionPool import TransactionPool

if __name__ == '__main__':

    sender = "sender"
    reciever = "reciever"
    amount = 100
    type = "TRANSFER"

    wallet = Wallet()
    fraudulentWallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(reciever, amount, type)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    print(pool.transactions)