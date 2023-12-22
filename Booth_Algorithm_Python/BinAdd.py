#Binary addition function
def Add(A,B):
    Sum=""
    carry = "0"
    for i in range(7,-1,-1):
        if (carry=="0"):
            if(B[i]=="0" and A[i]=="0"):
                Sum="0"+Sum
                carry="0"
                continue
            elif(B[i]=="1" and A[i]=="1"):
                Sum="0"+Sum
                carry="1"
                continue
            elif(B[i]=="0" and A[i]=="1"):
                Sum="1"+Sum
                carry="0"
                continue
            elif(B[i]=="1" and A[i]=="0"):
                Sum="1"+Sum
                carry="0"
                continue
        if(carry=="1"):
            if(B[i]=="0" and A[i]=="0"):
                Sum="1"+Sum
                carry="0"
                continue
            elif(B[i]=="1" and A[i]=="1"):
                Sum="1"+Sum
                carry="1"
                continue
            elif(B[i]=="0" and A[i]=="1"):
                Sum="0"+Sum
                carry="1"
                continue
            elif(B[i]=="1" and A[i]=="0"):
                Sum="0"+Sum
                carry="1"
                continue
    return Sum
