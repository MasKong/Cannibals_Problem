from collections import deque
from SearchSolution import SearchSolution
# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes

class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        # you write this part
        self.state = state
        self.parent = parent
        return

    def print_path(self):
        l = []
        l.append(self.state)
        t = self.parent

        while t!= None:
            l.append(t.state)
            t = t.parent
        print ('\n')
        print('*******************')
        for node in l[-1::-1]:
            print (node)
        print ("end")
    def dfs_get_successors(self, explored, start_state):
        # you write this part. I also had a helper function
        #  that tested if states were safe before adding to successor list
        if self.state == ():
            return ()
        l = []
        if self.parent == None:
            i=0
        else:
            if self.state[0] - self.parent.state[0] + self.state[1] - self.parent.state[1] >0:
                i=0
            else:
                i = 1
        if i % 2 == 0:
            s1 = (self.state[0]-1, self.state[1]-1, self.state[2]^1)
            s2 = (self.state[0], self.state[1]-2, self.state[2]^1)
            s3 = (self.state[0]-2, self.state[1], self.state[2]^1)
            s4 = (self.state[0]-1, self.state[1], self.state[2]^1)
            s5 = (self.state[0], self.state[1]-1, self.state[2]^1)
        else:
            s1 = (self.state[0]+1, self.state[1]+1, self.state[2]^1)
            s2 = (self.state[0], self.state[1]+2, self.state[2]^1)
            s3 = (self.state[0]+2, self.state[1], self.state[2]^1)
            s4 = (self.state[0]+1, self.state[1], self.state[2]^1)
            s5 = (self.state[0], self.state[1]+1, self.state[2]^1)

        # l_potential=[s1,s2,s3,s4,s5,s6]
        # for i in l_potential:
        #     if self.check_state(i[1], explored):
        #         l.append(i)
        # explored.append(state[1])
        #else:
        #    l.append(())
        if self.check_state(s1, explored,start_state):
            l.append(s1)
            # l.append(SearchNode(s1, self.parent))
        if self.check_state(s2, explored, start_state):
            l.append(s2)
            # l.append(SearchNode(s2, self))
        if self.check_state(s3, explored, start_state):
            l.append(s3)
            # l.append(SearchNode(s3, self))
        if self.check_state(s4, explored,start_state):
            l.append(s4)
            # l.append(SearchNode(s4, self))
        if self.check_state(s5, explored, start_state):
            l.append(s5)
            # l.append(SearchNode(s5, self))
        explored.append(self.state)   #values are parent nodes
        #explored[state[1]] = state[0]   #values are parent nodes
        # else:
        #     l.append(())
        # print (l)
        return l

    def check_state(self, state, explored, start_state):       #state[0] missionary state[1] cannibal
        if state in explored:
            return False
        if state[0] - start_state[0] + state[1] - start_state[1] >2:
            return False
        if state == start_state:
            return False
        if state[1] > state[0] and state[0] != 0:
            return False
        if state[0] < 0 or state[0] > start_state[0]:
            return False
        if state[1] < 0 or state[1] > start_state[1]:
            return False
        # if state[0] - self.start_state[0] == 1 and state[1] - self.start_state[1] == 0:
        #     return False
        # if state[0] - self.start_state[0] == 0 and state[1] - self.start_state[1] == 1:
        #     return False
        # if state[0] - self.start_state[0] != 0 and self.start_state[1] - state[1]> \
        #     (self.start_state[0] - state[0]):    #detect illegal state across the bank
        #     return False
        if state[0] != 0 and state[0] - start_state[0] != 0 and \
        start_state[1] - state[1] > (start_state[0] - state[0]):  # detect illegal state across the bank
            return False
        return True


    def goal_test(self, state):
        if state == self.goal_state:
            return True
        else:
            return False

    # I also had a goal test method. You should write one.

    def __str__(self):
        string =  "Missionaries and cannibals problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = CannibalProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)


# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions

def bfs_search(search_problem, path_printing = False):
    # explored = deque()i
    explored = {}
    frontier = deque()
    #l = search_problem.get_successors(search_problem.start_state)
    t =  search_problem.get_successors(((), search_problem.start_state), explored)
    if len(t) != 0:
        frontier.extend(t)
    if len(frontier) == 0:
        print ("illegal tree")
        return False
    #explored.append(search_problem.start_state)
    #i = 1
    while len(frontier) != 0:
        current = frontier.popleft()
        if search_problem.goal_test(current[1]):
            if path_printing == True:
                print_path(current[0], explored, search_problem.start_state, current[1])
            # print (current)
            return True
        #t = search_problem.get_successors(current, explored, i)
        if current[1] in explored.keys():
            continue
        t = search_problem.get_successors(current, explored)
        if len(t) != 0:
            frontier.extend(t)
        # i+=1

def print_path(node, explored, start_state, goal_state):
    l = []
    n = explored[node]
    l.append(n)
    while n != start_state:
        n = explored[n]
        l.append(n)
    print ('\n')
    print('*******************')
    for t in l[-1::-1]:
        print (t)
    print (goal_state)



# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    explored = []
    frontier = deque()
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")
    t = node.dfs_get_successors(explored, search_problem.start_state)
    if len(t) == 0:
        print ("No solution")
        return False
    for i in t:
        frontier.append(SearchNode(i, node))
    # frontier.extend(t)
    while len(frontier) != 0:
        current = frontier.pop()
        if search_problem.goal_test(current.state):
            current.print_path()
            return True
        else:
            t = current.dfs_get_successors(explored, search_problem.start_state)
            if len(t) != 0:
                for i in t:
                    frontier.append(SearchNode(i,current))
    # you write this part



def ids_search(search_problem, depth_limit=100):
    # you write this part
    pass


