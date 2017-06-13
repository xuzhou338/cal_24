import itertools

class OP():
    """Try plus, minus, multiply and divide between each of the four elements
     to get 24. """

    def __init__(self, case):
        """Import the numbers."""
        cases = itertools.permutations(case,4)
        self.cases = cases
        self.method = []

    def tryop(self):
        """There are 32 types of operation combinations for each permutation.
        This method tries all of the calculations and then append the list of
        ways to calculate 24"""
        for case in self.cases:
            if (case[0] + case[1] + case[2] + case[3]) == 24:
                method = tuple([case,'+++'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] + case[1] + case[2] - case[3]) == 24:
                method = tuple([case, '++-'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] + case[1] * case[2] + case[3]) == 24:
                method = tuple([case,'+*+'])
                if method not in self.method:
                    self.method.append(method)

            if ((case[0] + case[1]) * (case[2] + case[3])) == 24:
                method = tuple([case, '(+)*(+)'])
                if method not in self.method:
                    self.method.append(method)

            if ((case[0] + case[1] + case[2]) * case[3]) == 24:
                method = tuple([case,'(++)*'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] + case[1] / case[2] + case[3]) == 24:
                method = tuple([case, '+/+'])
                if method not in self.method:
                    self.method.append(method)

            if ((case[0] + case[1]) / (case[2] + case[3])) == 24:
                method = tuple([case,'(+)/(+)'])
                if method not in self.method:
                    self.method.append(method)

            if ((case[0] + case[1] + case[2]) / case[3]) == 24:
                method = tuple([case, '(++)/'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] - case[1] - case[2] + case[3]) == 24:
                method = tuple([case, '--+'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] - case[1] - case[2] - case[3]) == 24:
                method = tuple([case, '---'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] - case[1] * case[2] - case[3]) == 24:
                method = tuple([case, '-*-'])
                if method not in self.method:
                    self.method.append(method)

            if ((case[0] - case[1]) * (case[2] - case[3])) == 24:
                method = tuple([case, '(-)*(-)'])
                if method not in self.method:
                    self.method.append(method)

            if ((case[0] - case[1] - case[2]) * case[3]) == 24:
                method = tuple([case, '(--)*'])
                if method not in self.method:
                    self.method.append(method)

            try:
                ans = (case[0] - case[1] / case[2] - case[3])
            except ZeroDivisionError:
                pass
            else:
                if ans == 24:
                    method = tuple([case, '-/-'])
                    if method not in self.method:
                        self.method.append(method)

            try:
                ans = ((case[0] - case[1]) / (case[2] - case[3]))
            except ZeroDivisionError:
                pass
            else:
                if ans == 24:
                    method = tuple([case, '(-)/(-)'])
                    if method not in self.method:
                        self.method.append(method)

            try:
                ans = ((case[0] - case[1] - case[2]) / case[3])
            except ZeroDivisionError:
                pass
            else:
                if ans == 24:
                    method = tuple([case, '(--)/'])
                    if method not in self.method:
                        self.method.append(method)

            if (case[0] * case[1] * case[2] + case[3]) == 24:
                method = tuple([case, '**+'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] * case[1] * case[2] - case[3]) == 24:
                method = tuple([case, '**-'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] * case[1] * case[2] * case[3]) == 24:
                method = tuple([case, '***'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] * case[1] * case[2] / case[3]) == 24:
                method = tuple([case, '**/'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] / case[1] / case[2] + case[3]) == 24:
                method = tuple([case, '//+'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] / case[1] / case[2] - case[3]) == 24:
                method = tuple([case, '//-'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] / case[1] / case[2] * case[3]) == 24:
                method = tuple([case, '//*'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] / case[1] / case[2] / case[3]) == 24:
                method = tuple([case, '///'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] + case[1] * case[2] - case[3]) == 24:
                method = tuple([case, '+*-'])
                if method not in self.method:
                    self.method.append(method)

            if ((case[0] + case[1]) * (case[2] - case[3])) == 24:
                method = tuple([case, '(+)*(-)'])
                if method not in self.method:
                    self.method.append(method)

            if ((case[0] + case[1] - case[2]) * case[3]) == 24:
                method = tuple([case, '(+-)*'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] + case[1] / case[2] - case[3]) == 24:
                method = tuple([case, '+/-'])
                if method not in self.method:
                    self.method.append(method)

            try:
                ans = ((case[0] + case[1]) / (case[2] - case[3]))
            except ZeroDivisionError:
                pass
            else:
                if ans == 24:
                    method = tuple([case, '(+)/(-)'])
                    if method not in self.method:
                        self.method.append(method)

            if ((case[0] + case[1] - case[2]) / case[3]) == 24:
                method = tuple([case, '(+-)/'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] + case[1] * case[2] / case[3]) == 24:
                method = tuple([case, '+*/'])
                if method not in self.method:
                    self.method.append(method)

            if (case[0] - case[1] * case[2] / case[3]) == 24:
                method = tuple([case, '-*/'])
                if method not in self.method:
                    self.method.append(method)

