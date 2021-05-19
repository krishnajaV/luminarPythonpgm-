def change_pin(user,pin):
    if user=="admin" :
        mypim=pin
        return mypim
    else:
        raise Exception ("not able to perform")
def delete(user,username):
    if user=="admin" :
        mypim=pin
        return mypim
    else:
        raise Exception ("not able to perform")
    return username+ "deleted"