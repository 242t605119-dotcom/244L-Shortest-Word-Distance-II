# LeetCode 244 - Shortest Word Distance II

## Problem

Design a data structure that receives a list of words and supports repeated queries for the shortest distance between two different words.

The `WordDistance` class should support:

* `WordDistance(wordsDict)` - Initializes the object.
* `shortest(word1, word2)` - Returns the shortest distance between the two words.

## Example

### Input

```text
wordsDict = ["practice","makes","perfect","coding","makes"]

word1 = "coding"
word2 = "practice"
```

### Output

```text
3
```

## Approach

Since multiple queries can be performed, store the positions of every word when the object is created.

For example:

```text
practice -> [0]
makes    -> [1,4]
perfect  -> [2]
coding   -> [3]
```

For each query, use two pointers to compare the sorted position lists of the two words.

## Algorithm

1. Create a dictionary to store positions of each word.
2. Traverse `wordsDict` and store every word's index.
3. For a query, get the position lists of `word1` and `word2`.
4. Use two pointers to compare the positions.
5. Calculate the absolute difference.
6. Move the pointer containing the smaller position.
7. Return the minimum distance.

## Complexity

### Constructor

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

### Shortest Query

* Time Complexity: `O(p + q)`
* Space Complexity: `O(1)`

Where `p` and `q` are the number of occurrences of the two queried words.

## Language

Python

## LeetCode

Problem: 244 - Shortest Word Distance II

## Author

**T.Nandhini**
