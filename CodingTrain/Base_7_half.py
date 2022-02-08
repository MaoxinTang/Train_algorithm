class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(0)
        if num <0:
            num = -num
            is_nega = 1
        else:is_nega = 0
        high_num = []
        b_list = []
        while num:
            a = int(num/7)
            high_num.append(str(a))
            b = num % 7
            b_list.append(str(b)) 
            
        
            if len(high_num) <=2 and len(high_num)>1:
                if is_nega:
                    ans = "-" +''.join(high_num[0]) + b_list[0]
                else:
                    ans = ''.join(high_num[0]) + b_list[0]
            else:
                if is_nega:
                    ans = "-" +''.join(high_num[1:]) + b_list[len(high_num) -2]
                else:
                    ans = ''.join(high_num[1:]) + b_list[len(high_num) -2]
            num = a
        return(ans)