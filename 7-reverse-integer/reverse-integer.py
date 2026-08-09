class Solution:
    def reverse(self, x: int) -> int:
        # if(x>=0):
        #     s=str(x)
        #     s=list(s)
        #     s.rever
        s=-1 if x<0 else 1
        n=abs(x)
        z=0
        while(n):
            rem=n%10
            z=(z*10)+rem
            n//=10
        z*=s
        if z < -2**31 or z > 2**31 - 1:
            return 0
        return z