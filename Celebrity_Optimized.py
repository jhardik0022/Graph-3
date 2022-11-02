# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# Time complexity : O(n)
# Space complexity : O(1)
# Leetcode : Solved and submitted

class Solution:
    def findCelebrity(self, n: int) -> int:
        # take celebrity as 0
        celeb = 0
        
        # traverse over all the members
        for i in range(1,n):
            # if any person knows the other person, then the current person cannot be a celeb
            if knows(celeb,i):
                # update the celeb
                celeb = i
        
        # check the probable celeb with other members
        for i in range(n):
            if celeb != i:
                # if condition is false anytime, then return -1
                if knows(celeb,i) or not knows(i,celeb):
                    return -1
        
        # return celeb is no issues
        return celeb
