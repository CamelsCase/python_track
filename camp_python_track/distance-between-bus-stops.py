class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        cl = 0
        anti = 0
        leng = len(distance)
        start1,start2 = start,start
        
        while start1!=destination:
            cl+=distance[start1]
            start1 +=1
            if start1==leng:
                start1 = 0
            print(start1,destination,cl)
        print("the clock wise is finished")
        while start2!=destination:
            start2 = start2-1
            if start2==-1:
                start2=leng-1
            anti+=distance[start2]
            
            print(start2,destination,anti)
        print("the anti clock wise is finished")
        print(cl,anti)
        return min(cl,anti) 