class Solution:
    def fib(self, n: int) -> int:
        
        def fibonnachi(valor, memo=None): # 
            if memo is None: memo = {}
            if valor in memo: return memo[valor]
            if valor <= 1: return valor

            memo[valor] = (fibonnachi(valor-1, memo) + fibonnachi(valor-2, memo)) 

            return memo[valor]

        return fibonnachi(n)