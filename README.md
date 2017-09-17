# merkle trees
merkle trees allow efficient and secure verification of the contents of large data structures.

why merkle trees?
* reduces the amount of data that a trusted authority has to maintain to proof the integrity of the data
* reduces the network I/O packet size to perform consistency and data verification as well as data synchronization
* separates the validation of the data from the data itself

## usage
```python
import merkle

from merkle import generate_merkle_root
transactions = ['tx1', 'tx2', 'tx3', 'tx4', 'tx5']
generate_merkle_root(transactions)  # returns e5fb69843938b939e7f1823414b2e3aaa52c1eaa
```

a simple implementation calculates merkle roots

<img src="http://orm-chimera-prod.s3.amazonaws.com/1234000001802/images/msbt_0702.png" width="100")