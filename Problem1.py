'''
1. Maintain hashMaps for digits upto 19, tens upto 90
2. Any number > 3 digits can be computed using 3 digits - hundreds,tens,units place followed by one of Thousand, Million, Billion in order respectively.
3. Convert any large number to string 3 digits at a time and loop until number is > 0.
4. After computing individual sets, reverse it to get the Word as Billion - Million - ...

TC: O(logn) -> Since we are computing 3 digits at a time
SC: O(1)
'''

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen"
        }
        tens = {
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety"
        }

        postfix = ['',' Thousand', ' Million', ' Billion']

        i = 0

        def get_word(num):
            s = []
            hundreds = num // 100
            if hundreds:
                s.append(ones[hundreds] + ' Hundred')
            
            two_digits = num % 100
            if two_digits:
                if two_digits > 19:
                    tens_digit = two_digits // 10
                    if tens_digit:
                        s.append(tens[tens_digit * 10])
                    
                    units = two_digits % 10
                    if units:
                        s.append(ones[units])
                else:
                    s.append(ones[two_digits])
            return ' '.join(s)
        

        res = []
        while num > 0:
            word = get_word(num % 1000)
            if word:
                res.append(word + postfix[i])
            i += 1
            num = num // 1000    

        return ' '.join(res[::-1])