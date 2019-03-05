# Autopilot Coding Challenge

The following documents my solution for the Autopilot coding challenge.

## Setup

This solution makes use of the k-d tree data structure implementation in Scikit-learn. Instructions to install Scikit-learn can be found [here](https://scikit-learn.org/stable/install.html).

## Usage

Run the following:
```
python3 autopilot.py
```

## Efficiency

This solution relies on a k-d tree to efficiently search for ranges of points.

### Time Complexity

Given N cars and K superchargers, building the k-d tree takes $O(N\log{N})$ time in the worst case. The following is the time complexity of the solutions to each of the problems, assuming the k-d tree has already been built:

1. Searching for neighbours within radius $r$ from a point $(x, y)$ in the k-d tree takes $O(\log{N})$ time. So, to search for the neighbours of all superchargers takes $O(K\log{N})$ time. Then, $O(KN)$ time is required to get the number of cars within radius $r$ of at least one supercharger.

2. Same as Problem 1.

3. This solution performs a binary search for the minimum radius, and at each iteration it runs the algorithm in Problem 1. So, the overall time complexity is $O(KN\log{r})$, where $r$ is the value of the minimum radius.

4. Same as Problem 3.

### Space Complexity

All of the solutions require $O(N)$ space to store the k-d tree, as well as other intermediate variables.

## Answers

1. Cars within 5 meters of at least one supercharger: **90851**

2. Cars within 10 meters of at least one supercharger: **315614**

3. Minimum radius with 80% coverage: **22m**

4. Maximum radius with at most 1000 cars covered by each supercharger: **11m**
