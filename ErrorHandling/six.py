try:
    print(int("hello"))
    
except (ValueError, ZeroDivisionError, FileNotFoundError, AttributeError) as err:
    print(err)