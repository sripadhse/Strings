class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        if n==1:
            return res
        tmp = []
        for i in range(2, n+1):
            s = 0
            cnt = 0
            str1 = ""
            
            for c in range(len(res[s:])):       
                if res[s]==res[c]:              
                    cnt+=1
                    if len(res)-1 == c:                 
                        str1 += str(cnt)+str(res[s])   
                    try:    
                        if res[c+1] != res[s]:              
                            str1 += str(cnt)+str(res[s])   
                            s=c+1                           
                            cnt=0
                    except:
                        pass 
            tmp.append(str1)
            res=tmp[-1]
        return res