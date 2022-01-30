class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
        myList=list(A)
        operator=['+','-','*','/']
        opeTotal=0
        bracesTotal=0
        #print(myList)
        num=0
        for i in myList:
            if(num<len(myList)-2):
                if(myList[num]=='(' and myList[num+2]==')'):
                    return 1

            #print(i)
            if(i in operator):
                #print(i,' O ',operator)
                opeTotal=opeTotal+1
            if(i == '('):
                #print(i,' ( ')
                bracesTotal=bracesTotal+1
            num=num+1
            
        if(opeTotal>=bracesTotal):
            return 0
        else:
            return 1
