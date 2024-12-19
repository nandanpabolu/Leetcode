class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        is_neg = n < 0 #boolean to see if n is negative or positive
        n = abs(n) # converting to positive

        self.memo = {}

        res = self.fast_pow(x,n)

        return 1/res if is_neg else res

    def fast_pow(self, x, n):
        if n in self.memo:
            return self.memo[n]
        
        if n == 0:
            return 1 
        elif n == 1:
            return x 
        self.memo[n] = self.fast_pow(x, n // 2) * self.fast_pow(x, n // 2) * (x if n % 2 else 1) #Calculating power and differenciating between odd and even
        return self.memo[n]

# Time Complexity is O(log n) as we are cutting down number of computations to do by half everytime
# Space Complexity is O(log N) intermediate results are stored in self.memo dictionary 



