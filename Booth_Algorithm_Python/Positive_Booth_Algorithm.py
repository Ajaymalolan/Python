#Step 1: Getting inputs:
multiplicand=int(input("Please enter the multiplicand(positive value less than 128): "))
multiplier=int(input("Please enter the multiplier(positive value less than 128): "))

#Step 2: Convert to binary and format:
b_cand="{0:b}".format(multiplicand)
b_plier="{0:b}".format(multiplier)
B=b_cand
print(B)
Q=b_plier
print(Q)
for i in range(0,8-len(b_cand)):
   B="0"+B
for i in range(0,8-len(b_plier)):
   Q="0"+Q

#Step 3: Add accumulator and end bit:
steps=max(len(b_cand),len(b_plier))
A="00000000"+Q+"0"
print(A)
print("Number of steps needed =",steps)


#Step 5: Define operation:
#Addition:
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

#Subtraction:
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

#Shift:
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

#Step 4: Decide operation.
while steps>=0:
    #Seperate Operation bits:
    Op=A[15]+A[16]
    #Determine operation:
    if(Op=="00"):
        print("shift")
        A=Shift(A)
    elif(Op=="11"):
        print("shift")
        A=Shift(A)
    elif(Op=="01"):
        print("Add+shift")
        A=Add(A,B)+A[8:len(A)]
        A=Shift(A)
    elif(Op=="10"):
        print("Sub+shift")
        A=Sub(A,B)+A[8:len(A)]
        A=Shift(A)
    steps=steps-1
    print(A)

#removing additional zeros at the end
i=8-max(len(b_cand),len(b_plier))
while i>0:
    A=Shift(A)
    i=i-1
print("Final result in binary = ",int(A))

#convert to decimal
decimal=0
for i in A:
    decimal=decimal*2+int(i)
print("Product in decimal = ",decimal)
    
