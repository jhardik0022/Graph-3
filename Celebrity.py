# Time complexity : O(n*n)
# Space complexity : O(n)
# Leetcode : Time Limit Exceeded

class Solution:
    def findCelebrity(self, n: int) -> int:
        # make an empty indegree array
        indeg = [0] * n
        
        # traverse over all the celebs
        for i in range(n):
            for j in range(n):
                # the same person cannot know itself
                if i != j:
                    # call the API and check it's value
                    if knows(i,j):
                        # increment the indeg of j and decrement of i
                        indeg[j] += 1
                        indeg[i] -= 1
        
        # a person of indeg having value of n-1 is the celeb
        for i in range(n):
            if indeg[i] == n-1:
                return i
        
        # if none found, then return -1
        return -1
