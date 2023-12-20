class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        full =capacity
        for i in range(len(plants)):
            if plants[i]>0 and capacity>=plants[i]:
                capacity-=plants[i]
                plants[i]=0
                steps+=1
            else:
                steps+=2*(i)
                capacity = full
                if plants[i]>0 and capacity>=plants[i]:
                    capacity-=plants[i]
                    plants[i]=0
                    steps+=1
                else:
                    steps+=2*(i)
                    capacity = full
        return steps