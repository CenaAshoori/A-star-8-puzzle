class Node:
        parent: "Node"
        mat: list[list[int]]
        g: int
        h: int
        f: int

        def __init__(
                self, parent: "Node", row, col, mat: list[list[int]], mat_goal: list[list[int]], g: int, alpha: float, dic):
            self.parent = parent
            self.mat = mat
            self.g = g
            self.h = self.h1(mat,dic)
            # self.h = self.h2(mat_goal)
            self.row = row
            self.col = col
            # Alpha is the diffrence between Greedy and A*
            self.f = (2 - alpha) * self.g + alpha * (self.h)
        def h1(self, curent_mat, dic):
            counter = 0
            for row in range(len(self.mat)):
                for col in range(len(self.mat[0])):
                    r, c = dic[curent_mat[row][col]]
                    counter += abs(row - r) + abs(col - c)
            return counter

        def h2(self, goal_mat):
            counter = 0
            for r in range(len(self.mat)):
                for c in range(len(self.mat[0])):
                    if self.mat[r][c] != goal_mat[r][c]:
                        counter += 1
            return counter
