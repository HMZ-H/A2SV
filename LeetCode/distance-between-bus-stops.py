class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        clockwise = sum(distance[min(start, destination):max(start, destination)])
        counterclockwise = total - clockwise
        return min(counterclockwise, clockwise)

        