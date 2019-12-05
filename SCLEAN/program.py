str1=[]
def removechar(string):
    if (len(string)==1):
        str1.append(string[0])
        return (str1)

    if(len(string)>1 and string[0] == string[1]):
        while(len(string)>1 and string[0]== string[1]):
            string=string[1:]
        str1.append(string[0])
        return removechar(string[1:])
    elif(len(string)>1 and string[0] != string[1]):
        str1.append(string[0])
        return removechar(string[1:])
t=int(input())
while(t>0):
    str=list(input())
    k=removechar(str)
    print("".join(str1))
    str1=[]
    t-=1
