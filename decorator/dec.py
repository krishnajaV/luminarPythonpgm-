def revert_value(func):
    def wrapper(no1,no2):
        if  no1<no2:
            (no1,no2)=(no2,no1)
            return func(no1,no2)
    return wrapper
@revert_value
def div(no1,no2):
    return no1/no2

print(div(25,5))






































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































