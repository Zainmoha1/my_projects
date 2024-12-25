A=float(input("ENTER FIRST NUMBER: "))
OP=input("ENTER OPERATOR (+,-,*,//,/,**): ")
B= float(eval(input('ENTER Second NUMBER: ')))
if OP=="+":
    SUM=A+B
    print(F"{A}+{B}={SUM}")
elif OP=="-":
    SUB=A-B
    print(F"{A}-{B}={SUB}")
elif OP=="*":
    MULTIP=A*B
    print(F"{A}*{B}={MULTIP}")
elif OP=="//":
    DEVIDE=A//B
    print(F"{A}//{B}={DEVIDE}")
elif OP=="/":
    DEVIDE=A/B
    print(F"{A}/{B}={DEVIDE}")
elif OP=="**":
    EXPONENT=A**B
    print(F"{A}**{B}={EXPONENT}")