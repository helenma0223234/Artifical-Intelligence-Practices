# Yuchuan Ma
# Sep 18, 2023
# Dartmouth College CS 276 HW1

class FoxProblem:
    def __init__(self, start_state=(3, 3, 1), boat_size = 2):
        # stat= (no. of fox, no. of chicken, boat on left/right side)
        self.start_state = start_state
        self.goal_state = (0, 0, 0)

        #  extract constants from start_state
        self.FOX_TOTAL = start_state[0]
        self.CHICKEN_TOTAL = start_state[1]
        self.BOAT_SIZE = boat_size

    def get_successors(self, state):
        """
        Get successor states for the given state

        :param state: current state
        :type state: tuple

        :return: next states that are solid
        :rtype: list of tuple
        """
        successors = []
        # check initial input state
        if not self.is_safe_state(state):
            return successors

        boat = state[2]^1   # switch boat to other side
        # check how many foxes and chickens can cross the river with given boat size
        if state[2] == 1:
            can_pass_fox = min(state[0], self.BOAT_SIZE)
            can_pass_chicken = min(state[1], self.BOAT_SIZE)
        else:
            can_pass_fox = min(self.CHICKEN_TOTAL - state[0], self.BOAT_SIZE)
            can_pass_chicken = min(self.FOX_TOTAL - state[1], self.BOAT_SIZE)

        for f in range(0, can_pass_fox+1):
            # print("for fox range: " str(f)+ " chick range: " + str(min(self.BOAT_SIZE-f, can_pass_chicken+1)))
            for ch in range(0, min(self.BOAT_SIZE-f + 1, can_pass_chicken + 1)):
                if f == 0 and ch == 0: continue
                fox, chicken = 0, 0
                # boat side decides either adding or subtracting the animals
                if state[2] == 1:
                    fox = state[0] - f
                    chicken = state[1] - ch
                else:
                    fox = state[0] + f
                    chicken = state[1] + ch
                # check if state is safe
                if self.is_safe_state((fox, chicken, boat)):
                    successors.append((fox, chicken, boat))

        return successors

    def is_safe_state(self, state):
        """
        Test if a state is safe

        :param state: current state
        :type state: tuple

        :return: if the state safe is safe
        :rtype: bool
        """

        # check if state is legal and not repeating previous action
        if 0 <= state[0] <= self.FOX_TOTAL and 0 <= state[1] <= self.CHICKEN_TOTAL:
            # check if state is safe
            # when it's all chicken/foxes on one side
            if (state[1] == self.CHICKEN_TOTAL and state[1] >= state[0]) or (state[1] == 0 and self.CHICKEN_TOTAL - state[1] >= self.FOX_TOTAL - state[0]):
                return True
            else:
                return state[1] >= state[0] and self.CHICKEN_TOTAL - state[1] >= self.FOX_TOTAL - state[0]
        else:
            # print("here")
            return False

    def goal_test(self, state):
        """
        Teste if the state is the goal state

        :param state: current state
        :type state: tuple

        :return: if the current state is goal state
        :rtype: bool
        """
        return state==self.goal_state

    def __str__(self):
        string =  "Foxes and chickens problem with boat size: " + str(self.BOAT_SIZE) + " and start state: " +  str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    # test_cp = FoxesProblem((5, 5, 1))
    test_cp = FoxProblem((3, 3, 2))
    # [(2, 3, 0), (2, 2, 0), (1, 3, 0)]
    print(test_cp.get_successors((3, 3, 1)))
    print(test_cp)
