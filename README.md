# merkle root
each block in the blockchain contains a summary of all the transactions in the block, using a merkle tree. a merkle tree, also known as a binary hash tree, is a data structure used for efficiently summarizing and verifying the integrity of large sets of data.

this simple implementation calculates merkle roots.
![merkle tree](http://orm-chimera-prod.s3.amazonaws.com/1234000001802/images/msbt_0702.png) 

## usage
```python
import merkle

from merkle import generate_merkle_root
transactions = ['tx1', 'tx2', 'tx3', 'tx4', 'tx5']
generate_merkle_root(transactions)  # returns e5fb69843938b939e7f1823414b2e3aaa52c1eaa
```