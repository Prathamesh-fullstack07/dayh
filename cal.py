a = int(input("ENTER number="))
b = (input("ENTER symbol="))
c = int(input("enter  number="))

match b:
 
    case '+':
        print(a+c)
    case '-':
        print(a-c)
    case '/':
        if c==0:
            print("cannot div by zero")
        else:
            print(a/c)
    case '*' :
        print(a*c)
    
                              

