# A star & IDA star 8 puzzle solver
In this repo 8 Puzzle solver , solve your puzzle with A* and IDA*

---
## 8 Puzzle Solver


###Quick Start :
Notice :
in 8 Puzzle ,we have an empty cell that move in available direction, and in this solver **_assume empty cell as 0_**



Define your **start** and **goal** matrix and **PASS IT** to the class
```python
    start = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6],
    ]
    goal = [
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 6],
    ]
```
what u waiting for? **PASS IT**
``` python
Puzzle(start, goal, 1).solve()
```
OR if you want solve with IDA* 
```python
Puzzle(start, goal, 1).solve(is_idastar=True, iterate=4)
```
If you want to see the result add .print_path() 

```python
Puzzle(start, goal, 1).solve().print_path()
```
now you can see your console , The result came out.

----
Third variable in this solver is Alpha variable that determined that search algorithm be on of **THIS** :

- Uniform Cost (0)
- A* (1)
- Greedy (2)

```python
self.f = (2 - alpha) * self.g + alpha * (self.h)

# alpha = 0 (uniform cost)
self.f = 2 * self.g
# alpha = 1 (a*)
self.f = self.g + self.h
# alpha = 2 (greedy)
self.f = 2 * self.h
```
ALPHA is float variable and if you put it in range of this numbers:
-[x] [0 , 1] algorithm is OPTIMAL
-[ ] (1 , ∞) algorithm going to be GREEDY and it's NOT OPTIMAL
----
## What Is an Optimal Algorithm?
An OPTIMAL algorithm ,is an algorithm that **_all the TIME_** return the shortest path.
maybe also **Greedy** search give us the shortest path sometimes, but because in **Greedy** search always
exist possibility of finding NON-OPTIMAL path(a path that is not the shortest one), because its don't care about 
the cost that its already paid,so we can't guarantee the path be optimal.

You know , we want to be optimal , in ALL THEM TIME.

## Why Greedy Search Isn't Optimal ?
Because it forgets its history and don't care about the Cost that its already paid, and it's just looking forward and
just care about **h cost(Heuristic)** value.

## What Is The Difference Between IDS(Iterative deepening Search) And IDA(Iterative deepening A*)? 

![img_1.png](https://github.com/CenaAshoori/A-star-8-puzzle/blob/main/img.png?raw=true)
(left = IDS  right = IDA*)

As you can see in above picture, in IDS(left) we put limitation on depth of search or actually on **G cost**,
but in IDA*(right) we put limitation on **F cost (g+h)**.



### Heuristic One 
This heuristic return sum of all Manhattan Distance from current state to goal state.

This heuristic is better than next one , because it gives us more actual Estimation.
````python
    def h1(self, curent_mat, dic):
        counter = 0
        for row in range(len(self.mat)):
            for col in range(len(self.mat[0])):
                r, c = dic[curent_mat[row][col]]
                counter += abs(row - r) + abs(col - c)
        return counter
````


### Heuristic Two
This heuristic just count all cells that are not in the correct Position(in comparison with goal state).


```python
    def h2(self, goal_mat):
        counter = 0
        for r in range(len(self.mat)):
            for c in range(len(self.mat[0])):
                if self.mat[r][c] != goal_mat[r][c]:
                    counter += 1
        return counter

```



