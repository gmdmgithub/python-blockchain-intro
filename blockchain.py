import functools # importing funcions (map, reduce, filter)

MINING_REWARD = 10

# Initializing our (empty) blockchain list
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Greg'
participants = {'Greg'} # set - it could be like set(['Greg'])


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_balance(participant):
    #sum from all transactions in a blockchain for a sender
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender']==participant] for block in blockchain] 
    #we add also open transactions
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender']==participant] 
    tx_sender.append(open_tx_sender)
    print(tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx)>0:
            amount_sent += tx[0]
    print(f'Amount sent is: {amount_sent}')

    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient']==participant] for block in blockchain]

    # amount_recieped = 0
    # for tx in tx_recipient:
    #     if len(tx)>0:
    #         amount_recieped += tx[0]
    
    #ltes rewrite it with reduce - very nice: Guido van Rossum (Python creator) - removed reduce form 3.x python - in 99% for loops is more readebale
    #amount_recieped = functools.reduce(lambda tx_sum, tx_amt: tx_sum +tx_amt[0] if len(tx_amt) > 0 else 0, tx_recipient, 0)
    inline_func = lambda tx_sum, tx_amt: tx_sum +tx_amt[0] if len(tx_amt) > 0 else 0
    amount_recieped = functools.reduce(inline_func, tx_recipient,0)

    print(f'Amount get is: {amount_recieped:.2f}')

    return amount_recieped - amount_sent

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]

def verify_transaction(transaction):
    """ Method to verify transaction - chcecking if sender has sofficient ballance"""
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def verify_transactions():
    """ Verify all transactions in blockchain """
    # for tx in open_transactions:
    #     if not verify_transaction(tx):
    #         return False
    # return True
    #simpler one line verification
    return all([verify_transaction(tx) for tx in open_transactions])


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True

    return False
    


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    #copy the open transaction (by value) to ensure we will not modify it
    #### 1 ####
    coppied_transactions = open_transactions[:]
    coppied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': coppied_transactions
    }

    blockchain.append(block)
    #### 2 ####
    #if anny error occure during the process it will not affect the open_transactions

    return True


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    """Prompts the user for its choice and return it."""
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    """ Output all blocks of the blockchain. """
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False otherwise."""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True




waiting_for_input = True

# A while loop for the user input interface
# It's a loop that exits once waiting_for_input becomes False or when break is called
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add the transaction amount to the blockchain
        if add_transaction(recipient, amount=amount):
            print(open_transactions)
        else:
            print('Transaction cannot be added - not sufficient amount on your account')
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        verify = verify_transactions()
        if verify:
            print('All transaction are valid')
        else:
            print('Veryfication problem - not all transaction are valid')

    elif user_choice == 'h':
        # Make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100.0}]
            }
    elif user_choice == 'q':
        # This will lead to the loop to exist because it's running condition becomes False
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        # Break out of the loop
        break
    print(f"Balance for Greg = {get_balance('Greg'):.2f}")
else:
    print('User left!')


print('Done!')
