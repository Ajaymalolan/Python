#Binary Shift Function
def Shift(A):
    #Positive shift
    if(A[0]=="0"):
        length=len(A)
        Shifter=A
        Shifter="0"+Shifter[:length-1]
        return Shifter
    else:
        #Negative shift
        length=len(A)
        Shifter=A
        Shifter="1"+Shifter[:length-1]
        return Shifter
