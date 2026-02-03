class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        answer=list()
        answer.append(celsius + 273.15)
        answer.append(celsius * 1.80 + 32.00)
        return answer
      
