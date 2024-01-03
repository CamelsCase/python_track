class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        st = 0
        en = len(people)
        saved = 0
        rescBoats = 0
        while st<en:
            if people[st] + people[en-1] <= limit:
                en -= 1
                st += 1
                saved+=2
                rescBoats+=1
            else:
                    saved+=1
                    en-=1
                    rescBoats+=1
        return rescBoats