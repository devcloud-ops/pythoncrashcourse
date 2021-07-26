# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and 
# the text of a message that should be printed on the shirt. The function 
# should print a sentence summarizing the size of the shirt and the message 
# printed on it. Call the function once using positional arguments to make 
# a shirt. Call the function a second time using keyword arguments.

def make_shirt(size,text):
    """Prints t-shirt size and text message on the t-shirt"""
    print(f"\nThis t-shirt size is {size} and the brand is {text.upper()}.")

make_shirt('5-S',"Nike") # positional arguments call
make_shirt(text="AWS",size='15-L') # keyword arguments call