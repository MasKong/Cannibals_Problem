class CannibalProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)

        # you might want to add other things to the problem,
        #  like the total number of missionaries (which you can figure out
        #  based on start_state

    # get successor states for the given state
    def get_successors(self, state, explored):
        # you write this part. I also had a helper function
        #  that tested if states were safe before adding to successor list
        if state == ():
            return ()
        l = []
        current_state = state[1]
        parent_state = state[0]
        if state[1] ==self.start_state:
            i=0
        else:
            if current_state[0] - parent_state[0] + current_state[1] - parent_state[1] >0:
                i=0
            else:
                i = 1
        if i % 2 == 0:
            s1 = (current_state, (current_state[0]-1, current_state[1]-1, current_state[2]^1))
            s2 = (current_state, (current_state[0]-2, current_state[1], current_state[2] ^ 1))
            s3 = (current_state, (current_state[0], current_state[1]-2, current_state[2] ^ 1))
            s4 = (current_state, (current_state[0] - 1, current_state[1], current_state[2] ^ 1))
            s5 = (current_state, (current_state[0], current_state[1] - 1, current_state[2] ^ 1))
        else:
            s1 = (current_state, (current_state[0]+1, current_state[1]+1, current_state[2]^1))
            s2 = (current_state, (current_state[0]+2, current_state[1], current_state[2]^1))
            s3 = (current_state, (current_state[0], current_state[1]+2, current_state[2] ^ 1))
            s4 = (current_state, (current_state[0] +1, current_state[1], current_state[2] ^ 1))
            s5 = (current_state, (current_state[0], current_state[1] +1, current_state[2] ^ 1))

        # l_potential=[s1,s2,s3,s4,s5,s6]
        # for i in l_potential:
        #     if self.check_state(i[1], explored):
        #         l.append(i)
        # explored.append(state[1])
        #else:
        #    l.append(())
        if self.check_state(s1[1], explored):
            l.append(s1)
        if self.check_state(s2[1], explored):
            l.append(s2)
        if self.check_state(s3[1], explored):
            l.append(s3)
        if self.check_state(s4[1], explored):
            l.append(s4)
        if self.check_state(s5[1], explored):
            l.append(s5)
        explored[state[1]] = state[0]   #values are parent nodes
        # else:
        #     l.append(())
        # print (l)
        return l




    def check_state(self, state, explored):       #state[0] missionary state[1] cannibal
        if state in explored.keys():
            return False
        if state[0] - self.start_state[0] + state[1] - self.start_state[1] >2:
            return False
        if state == self.start_state:
            return False
        if state[1] > state[0] and state[0] != 0:
            return False
        if state[0] < 0 or state[0] > self.start_state[0]:
            return False
        if state[1] < 0 or state[1] > self.start_state[1]:
            return False
        # if state[0] - self.start_state[0] == 1 and state[1] - self.start_state[1] == 0:
        #     return False
        # if state[0] - self.start_state[0] == 0 and state[1] - self.start_state[1] == 1:
        #     return False
        # if state[0] - self.start_state[0] != 0 and self.start_state[1] - state[1]> \
        #     (self.start_state[0] - state[0]):    #detect illegal state across the bank
        #     return False
        if state[0] != 0 and state[0] - self.start_state[0] != 0 and \
        self.start_state[1] - state[1] > (self.start_state[0] - state[0]):  # detect illegal state across the bank
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
