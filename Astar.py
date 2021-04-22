from node import Node


class Puzzle:
    queue: list["Node"] = []
    children_counter = 0
    answer_node: "Node"

    def __init__(self, start_mat: list[list[int]], goal_mat: list[list[int]], alpha):
        self.start_mat = start_mat
        self.goal_mat = goal_mat
        self.alpha = alpha
        self.mat_height = len(self.start_mat)
        self.mat_width = len(start_mat[0])
        self.val = {}
        self.IDASTAR = False
        self.max_f = 1
        row, col = self.find_start_point()
        # create First Node
        self.start_node = Node(None, row, col, start_mat, goal_mat, 0, alpha, self.val)

    def find_start_point(self):
        for r in range(len(self.goal_mat)):
            for c in range(len(self.goal_mat[0])):
                self.val[self.goal_mat[r][c]] = (r, c)
                if self.start_mat[r][c] == 0:
                    return (r, c)

    def find_best_node(self) -> (int, "Node"):
        best_node = (0, self.queue[0])
        for i in range(len(self.queue)):
            if self.queue[i].f < best_node[1].f:
                best_node = (i, self.queue[i])
        return best_node

    def create_children(self, node: "Node"):
        row, col = node.row, node.col
        node_mat = node.mat
        for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_row = row + dir[0]
            new_col = col + dir[1]
            if 0 <= new_row < self.mat_height and 0 <= new_col < self.mat_width:
                new_mat = [row[:] for row in node_mat]
                temp_var = node_mat[row][col]
                new_mat[row][col] = node_mat[new_row][new_col]
                new_mat[new_row][new_col] = temp_var


                if self.is_not_duplicated(node.parent, new_mat):
                    node = Node(node, new_row, new_col, new_mat, self.goal_mat, node.g + 1, self.alpha, self.val)
                    self.children_counter += 1

                    # IF Algorithm Was IDA STAR
                    if self.IDASTAR:
                        if node.f <= self.max_f:
                            self.queue.append(node)
                    else:
                        self.queue.append(node)

    def is_not_duplicated(self, node: "Node", new_mat: list[list[int]]) -> bool:
        while node != None:
            if node.mat == new_mat:
                return False
            node = node.parent
        return True

    def print_path(self):
        ans_list: list["Node"] = []
        node = self.answer_node
        while node != None:
            ans_list.append(node)
            node = node.parent
        ans_list.reverse()
        for node in ans_list:
            for row in node.mat:
                print(row)
            print("")
        print(f"All Children : {self.children_counter}")
        print(f"Best Path Length: {len(ans_list) - 1}")

    def solve(self, is_idastar=False, iterate=1):
        self.children_counter = 0
        self.max_f = 0
        self.IDASTAR = is_idastar
        while True:
            self.max_f += iterate
            self.queue.append(self.start_node)
            while len(self.queue) != 0:
                # find_best_node return a tuple with (index , node)
                best_node = self.find_best_node()
                if best_node[1].h == 0:
                    self.answer_node = best_node[1]
                    self.queue.clear()
                    return self
                self.create_children(best_node[1])
                self.queue.pop(best_node[0])
            if not is_idastar:
                return


if __name__ == "__main__":
    start = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6],
    ]
    goal = [
        [4, 5, 0],
        [1, 2, 3],
        [7, 8, 6],
    ]
    Puzzle(start, goal, .6).solve().print_path()
    # Puzzle(start, goal, 1).solve(is_idastar=True, iterate=27).print_path()
