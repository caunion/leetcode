__author__ = 'Daoyuan'
from BaseSolution import *

class IntegerToEnglishWords(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (20,),
            expects = "Twenty"
        )

        self.push_test(
            params = (12345,),
            expects = "Twelve Thousand Three Hundred Forty Five"
        )

        self.push_test(
            params = (1234567,),
            expects = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        )

    def solution(self, num):
        map1 = ['Zero','One', 'Two', 'Three', 'Four', 'Five',
               'Six', 'Seven', 'Eight', 'Nine', 'Ten',
               'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
               'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
               'Nineteen',
               'Twenty', 'Thirty', 'Forty', 'Fifty',
               'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]
        map2 = ['', 'Thousand', 'Million', 'Billion']
        segs =  []
        number = num
        if num == 0:
            return "Zero"

        result = ""
        while number > 0:
            segs.append( number % 1000)
            number = number  / 1000

        for idx, seg in enumerate(segs):
            tmp = ""
            number = str(seg)
            if len(number)==3 and int(number[0]) > 0:
                tmp = map1[int(number[0])] + ' Hundred'
                number = str(int(number) % 100)

            if len(number) == 2 and int(number[0]) > 0:
                if ( int(number[0]) ==1 ):
                    tmp = tmp + ' ' + map1[int(number)]
                    result = (tmp + ' ' + map2[idx] + ' ' + result).strip()
                    continue
                else:
                    tmp = tmp + ' ' + map1[int(number[0]) + 20 -2]
                    number = str(int(number) % 10)

            if len(number) == 1 and int(number[0]) > 0:
                tmp = tmp + ' ' + map1[int(number[0])]

            if len(tmp.strip()) > 0:
                result = (tmp + ' ' + map2[idx] + ' ' + result).strip()

        return result.strip()