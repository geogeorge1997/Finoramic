class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
        sNum=[]
        tNum=B
        for i in A:
            subList=A[:]
            #print(subList,A,'subList and A')
            subList.remove(i)
            subList.sort()
            number=self.findSum(subList,i,tNum)
            #print('number',number)
            if(len(sNum)>0):
                if(abs(tNum-number)>abs(tNum-sNum[0])):
                    number=sNum[0]
                else:
                    sNum[0]=number
            else:
                sNum.append(number)
            if(number==tNum):
                #print('Hai')
                return number
            
        return number

    def findSum(self,sList, num_1, tNum):
        i=0
        #print(sList)
        j=len(sList)-1
        #print(i,j)
        while(i<j):
            sum= num_1 + sList[i] + sList[j]
            #print(num_1,sList[i],sList[j])
            if(sum>tNum):
                j=j-1
            elif(sum<tNum):
                i=i+1
            elif(sum==tNum):
                return sum
            else:
                print('Nothing')
        return sum


