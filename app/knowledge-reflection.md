# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> 1. Deterministic - if you give same input (key), these function will always produce same output.
> 2. Efficient - Designed to give output quickly and efficiently
>    (Other properties do not apply because of the first ssh() function)

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> 1. Stupidly Simple Hash 
>    Advantages: Always returns the same value for the same input and also efficient
>    Disadvantages: Does not create unique outputs, all inputs cause collusion, output does not changes regardless of output and does not provide security
> 2. Sum of ASCII Values
>    Advantages: Determinism: Always produces the same output for the same input.
Efficiency: Computationally light; runs in linear time relative to the key's length.
Uniformity: Better than ssh, but clusters can still form with certain patterns in input data.
Collision Resistance: Low for similar strings (e.g., "abc" and "acb" might produce similar sums).
Sensitivity to Input Changes: Moderate; swapping characters can lead to minor differences in the sum.
>    Disadvantages: Weak; attackers can easily guess the hash function and predict outputs.
> 3. Pearson Hash
>    Advantages: Uniformity: Very good; outputs are evenly distributed when a well-randomized table is used.
Determinism: Consistently produces the same result for the same input.
Collision Resistance: Better than ASCII sum; avoids many predictable collisions.
Sensitivity to Input Changes: High; small changes in the key produce significant changes in the hash.
>    Disadvantages: Efficiency: Slower than simpler hashes due to XOR operations and table lookups.
Security: Not cryptographically secure; patterns in input might be reverse-engineered.
> 4. Built-in Hash
>    Advantages: Determinism: Consistent for the same input within a session (though Python salts hashes between sessions).
Efficiency: Very fast, as it’s implemented in C under the hood.
Uniformity: Generally good for most input distributions.
Collision Resistance: Decent for general use; handles common cases well.
Sensitivity to Input Changes: High; small changes in input typically result in large hash changes.
>    Disadvantages: Security: Not designed for cryptographic use; susceptible to hash collision attacks.
Portability: Output may vary across different Python implementations or versions.
> 5. SHA-256
>    Advantages: Uniformity: Excellent; outputs are distributed across the entire hash space.
Determinism: Always produces the same hash for the same input.
Collision Resistance: Very high; designed to minimize collisions even for malicious inputs.
Sensitivity to Input Changes: Extreme; even a single-bit change in input radically changes the output.
Security: Cryptographically secure; resistant to pre-image and collision attacks.
>    Disadvantages: Quite slow because of complexity, and too complicated for simple applications, unnecessary for applications that don't need security


3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> 1. Efficiency because hash maps are designed for fast operations and these functions must be quick. 
> 2. Uniformity because hash maps need to distribute keys evenly across the hash map. If outputs will cluster then it will downgrade the efficiency again.
> 3. Determinism because hash function need to return same output for same input, otherwhise how would we be able to look up by key efficiently

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I would choose Sum of ASCII Values (Pythonic Version) because this is fast, has concistent outputs for same inputs, uniformity performs well enough as we dont need too large hash maps, security is not an issue in our tasks and collision resistance is yet again good enough for our task.


5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> 1. import random - importing random module
> 2. random.seed(42) - this will fix specific starting point for seed so that it will be shuffled same way every time
> 3. pearson_table = list(range(256)) - Creating a table of integers from 0 to 255
> 4. random.shuffle(pearson_table) - this shuffles numbers in table while randomness spread vakues evenly
> 5. hash_ = 0 - starts hash value at 0
> 6. for char in key:  - loops through each letter(character) in key
> 7. hash_ = pearson_table[hash_ ^ ord(char)]      - converts character to numeric values, combines current hash value with character, looks up result from shuffled table to get new hash value
> 8. return hash_ % size - this will divide hash value by the size of hash map, the remainder will be returned

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> 1. I would first create array, where each element in array would be lists from PlayerLists
> 2. I would then create a hash function that would calculate index from given player unique ID
> 3. Then I would create a function to insert a Player into the hash map:
      - Generate index using the hash function and the player's unique ID.
      - If the PlayerList at that index already exists, raise error.
      - Add the player to the PlayerList at the index.

## Reflection

1. What was the most challenging aspect of this task?

> The most challenging part was figuring out how to integrate the player lists into the hash map. At first, I didn't really get how the uid was supposed to work, so I started generating it inside the Player class. After stepping back and thinking about it, I realized that the uid should actually come from outside the class when inserting the player. Once I got that, things started to click.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> If I didn't have to use a PlayerList, I would have simplified the hash map by directly using a list of players in each bucket. Instead of creating a separate linked list-like structure, I would store the players directly in the hash map buckets as a list or a set.

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.