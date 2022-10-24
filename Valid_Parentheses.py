n=int(input())
while n!=0:
    #p=input()
    def paraCheck( seq ):  
        while True:  
            if '()' in seq :  
              seq = seq.replace ( '()' , '' )  
            elif '{}' in seq :  
              seq = seq.replace ( '{}' , '' )  
            elif '[]' in seq :  
              seq = seq.replace ( '[]' , '' )  
            else :  
               return not seq  
  
    seq =input()
    print(paraCheck(seq))
    n-=1