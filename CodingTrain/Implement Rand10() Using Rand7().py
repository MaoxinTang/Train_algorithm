# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):

        while True:
            v1=rand7()
            v2=rand7()
            idx=(v1-1)*7+v2
            if idx<=40:
                return 1+(idx-1)%10
            v1=idx-40
            v2=rand7()
            idx=(v1-1)*7+v2
            if idx<=60:
                return 1+(idx-1)%10
            v1=idx-60
            v2=rand7()
            idx=(v1-1)*7+v2
            if idx<=20:
                return 1+(idx-1)%10
        