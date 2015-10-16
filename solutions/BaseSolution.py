__author__ = 'Caunion'
class BaseSolution:
    def __init__(self):
        self.tests = []

    def push_test(self, params, expects=None, oneOf=False ):
        simpleEvaluate = False
        if expects is None:
            simpleEvaluate = True
        self.tests.append([
            params,
            expects,
            oneOf,
            simpleEvaluate
        ])

    def evaluate(self):
        for idx, test in enumerate(self.tests):
            result = self.solution(*(test[0]))
            if test[3] == False:
                passed = False
                if test[2] == True:
                    for expect in test[1]:
                        if result == expect:
                            passed = True
                elif result == test[1]:
                    passed = True

                if passed:
                    print("PASSED Test Sample #{0}, ".format(idx)),
                else:
                    print("FAILED Test Sample #{0}, ".format(idx)),
                if test[2]:
                    print "returns {0}, expect one of:{1}".format(result,test[1])
                else:
                    print "returns {0}, expect {1}".format(result,test[1])

            else:
                print "Simpletest #{0} returns {1}".format(idx, result)

    def solution(self):
        pass