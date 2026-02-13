class Solution:
    def intToRoman(self, num: int) -> str:
        roman_list={
            1000:'M',
            900:'CM',
            500:'D',
            400: 'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I'
        }
        roman_number = ""
        for key, value in roman_list.items():
            while num >= key:
                roman_number+=value
                num-=key
        return roman_number
