__author__ = 'Caunion'
class BaseSolution:
    def __init__(self):
        self.tests = []
        self.fuckinglevel = 0

    def push_test(self, params, expects=None, expect_oneof=False, expect_unordered = False):
        simpleEvaluate = False
        if expects is None:
            simpleEvaluate = True
        self.tests.append({
            'params':   params,
            'expects':  expects,
            'simple_evaluation':  simpleEvaluate,
            'expect_oneof':    expect_oneof,
            'expect_unordered': expect_unordered
        })

    def evaluate(self):
        for idx, test in enumerate(self.tests):
            result = self.solution(*(test['params']))
            if test['simple_evaluation'] == False:
                passed = False
                if test['expect_oneof'] == True:
                    for expect in test['expects']:
                        if expect == result:
                            passed = True
                elif test['expect_unordered']:
                    ordered_expects = sorted(test['expects'])
                    ordered_result = sorted(result)
                    if ordered_expects == ordered_result:
                        passed = True
                elif result == test['expects']:
                     passed = True

                if passed:
                    print("PASSED Test Sample #{0}, ".format(idx)),
                else:
                    print("FAILED Test Sample #{0}, ".format(idx)),
                if test['expect_oneof']:
                    print "returns {0}, expect one of:{1}".format(result,test['expects'])
                else:
                    print "returns {0}, expect {1}".format(result,test['expects'])

            else:
                print "Simpletest #{0} returns {1}".format(idx, result)

    def solution(self):
        pass