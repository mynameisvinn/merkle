# merkle
combining hash functions with graphs was ralph merkle’s big idea. merkle dags are everywhere you want data integrity *through self verification*: git, ipfs, blockchain.

#### whats a merkle tree?
we have a hashing function $h(x)$ and four records a, b, c, d. a merkle tree would be y:
```
h_ab = h[h(a) + h(b)]
h_cd = h[h(c) + h(d)]
root_hash = h(h_ab + h_cd)
```

#### whats a merkle dag?
a merkle dag is an *acylic* collection of merkle trees. by referencing its predecessor's root hash, a merkle dag tracks history.
```
h_ab = h[h(a) + h(b)]
h_cd = h[h(c) + h(d)]
root_hash_1 = h(h_ab + h_cd)

h_ef = h[h(e) + h(f)]
h_gh = h[h(g) + h(h)]
root_hash_2 = h(h_ef + h_gh + root_hash_1)  # 2nd root hash knows its parent
```

## usage
```python
import merkle

from merkle import generate_merkle_root
transactions = ['tx1', 'tx2', 'tx3', 'tx4', 'tx5']
generate_merkle_root(transactions)  # returns e5fb69843938b939e7f1823414b2e3aaa52c1eaa
```

assuming you have the hash `e5fb69843938b939e7f1823414b2e3aaa52c1eaa` from a trusted authority, you can download chunks of data from various sources, compare its merkle root hash with the trusted one, and be confident that it's the same set of data.