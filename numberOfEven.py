def evenNumber(i):
    count1 = 0
    while(i):
        digit = i%10
        i//=10
        count1+=1
    print (count1)

a =  evenNumber(1234)