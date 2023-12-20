class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        F = celsius * 1.80 + 32.00
        K = celsius + 273.15
        return [K, F]
        