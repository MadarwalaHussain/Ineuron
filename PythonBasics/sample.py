def even(*args):
    try:
        for i in args:
            if i%2==0:
                print("Number is even")
            else:
                print("Number is odd")
              
    except Exception  as e :
        print(e)