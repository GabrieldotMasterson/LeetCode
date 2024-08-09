class Solution:
    def romanToInt(self, s: str) -> int:
        valores = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        resultado = 0

        for i in range(0, len(s)):
            if i < len(s)-1:
                if valores[s[i]] >= valores[s[i+1]]:
                    resultado += valores[s[i]]
                else:
                    resultado -= valores[s[i]]
            else:
                resultado += valores[s[i]]
        return resultado