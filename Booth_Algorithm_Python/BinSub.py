#Binary Subtraction function
def Sub(A,B):
    Diff=""
    borrow = "0"
    for i in range(7,-1,-1):
        if (borrow=="0"):
            if(B[i]=="0" and A[i]=="0"):
                Diff="0"+Diff
                borrow="0"
                continue
            elif(B[i]=="1" and A[i]=="1"):
                Diff="0"+Diff
                borrow="0"
                continue
            elif(B[i]=="0" and A[i]=="1"):
                Diff="1"+Diff
                borrow="0"
                continue
            elif(B[i]=="1" and A[i]=="0"):
                Diff="1"+Diff
                borrow="1"
                continue
        if(borrow=="1"):
            if(B[i]=="0" and A[i]=="0"):
                Diff="1"+Diff
                borrow="1"
                continue
            elif(B[i]=="1" and A[i]=="1"):
                Diff="1"+Diff
                borrow="1"
                continue
            elif(B[i]=="0" and A[i]=="1"):
                Diff="0"+Diff
                borrow="0"
                continue
            elif(B[i]=="1" and A[i]=="0"):
                Diff="0"+Diff
                borrow="1"
                continue
    return Diff
