class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2 = i3 = i5 = 0
        ugly_list = [1]
        for i in range (1,n):
            nextnum = min(2*ugly_list[i2],3*ugly_list[i3],5*ugly_list[i5])
            if nextnum == 2*ugly_list[i2] : i2+=1
            if nextnum == 3*ugly_list[i3] : i3+=1
            if nextnum == 5*ugly_list[i5] : i5+=1
            ugly_list.append(nextnum)
            print(nextnum)
        return ugly_list[-1]
            
            