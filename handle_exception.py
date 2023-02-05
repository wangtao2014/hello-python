# ref: https://www.runoob.com/python/python-exceptions.html
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exception
finally:                 # Execute under all circumstances
    print("We can clean up resources here")


# 用户自定义异常
class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg
