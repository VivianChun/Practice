password='a123456'
i=2
while i>0:
    
    x= input ('please enter your password:')
    if x ==password:
        print ('login successful')
        break
    else:
        print ('fail',i,'times left')
    i=i-1