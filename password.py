password='a123456'
i=2
while True:
    
    x= input ('please enter your password:')
    if x =='a123456':
        print ('login successful')
        break
    elif i == 0:
        print ('login failure')
        break
    else:
        print (i,'times left')
    i=i-1