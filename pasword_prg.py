dmid='thub@123.com'
dpw=1234
for i in range(3):
    umid=input("Enter Mail Id ")
    upw=int(input("Enter Password "))
    if dmid==umid and dpw==upw:
        print('***Login succesfully***')
        break
    else:
        print('^^^Wrong credintials^^^')
    print()
else:
    print()
    print('X Account Temporarily Blocked X')
    print('X Try After 24 Hours X')
