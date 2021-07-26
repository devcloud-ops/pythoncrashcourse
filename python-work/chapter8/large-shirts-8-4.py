# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a 
# different message.

def make_shirt(text='I love Python',size='Large'):
    """Prints t-shirt size and text message on the t-shirt"""
    print(f"\nThis t-shirt size is {size} and the message is {text.upper()}.")

make_shirt() # default value
make_shirt(size='Medium') # keyword arguments call
make_shirt('Just do it!','Small') # keyword arguments call