# -*- coding: utf-8 -*-

from hashlib import sha256

def h(msg):
    # in bitcoin's merkle trees, SHA256 is applied twice (known as double-SHA256).
    return sha256(msg).hexdigest()

def generate_merkle_root(q):
    
    # if number of transactions is odd, duplicate last transaction
    n_transactions = len(q)
    if n_transactions % 2 == 1:
        q.append(q[n_transactions - 1])

    while len(q) > 1:
        a, b = q.pop(0), q.pop(0)
        c = h(a + b)
        q.append(c)
        print q
    return q