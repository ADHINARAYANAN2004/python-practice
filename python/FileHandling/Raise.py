#User Define Exceptions
class Error(Exception):
    pass
class TooSmallError(Error):
    pass
class TooLargeError(Error):
    pass

num =10
while True:
    try:
        ch = int(input("Enter the Number :"))
        if ch < 10:
            raise TooSmallError
        elif ch > 10:
            raise TooLargeError
        break
    except TooSmallError:
        print("You Entered too small number, plz try again")
    except TooLargeError:
        print("You Entered too large number, plz try again")
        print("You entered correct number")