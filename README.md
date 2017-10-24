# merkle dags
applying a cryptographic hash function on top of a graph was ralph merkle’s big idea, and it has led to cool things like git, ipfs, blockchain.

## why?
merkle dags allow efficient (and privacy preserving, partially) verification of data collections. data might be transactions, code commits, etc.

## usage
```python
import merkle

from merkle import generate_merkle_root
transactions = ['tx1', 'tx2', 'tx3', 'tx4', 'tx5']
generate_merkle_root(transactions)  # returns e5fb69843938b939e7f1823414b2e3aaa52c1eaa
```

assuming you have the hash `e5fb69843938b939e7f1823414b2e3aaa52c1eaa` from a trusted authority, you can download chunks of data from various sources, compare its merkle root hash with the trusted one, and be confident that it's the same set of data.