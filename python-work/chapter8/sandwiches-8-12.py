# 8-12. Sandwiches: Write a function that accepts a list of items a person 
# wants on a sandwich. The function should have one parameter that collects 
# as many items as the function call provides, and it should print a summary 
# of the  sandwich that’s being ordered. Call the function three times, 
# using a different number of arguments each time.

# sandwich_options = ['mayo','butter','cream cheese','tomatoes','cucumbers']

def sandwich_maker(*sides):
    """Makes a sandwich with all """
    print("\nThe sandwich being made includes these items: ")
    for side in sides:
        print(f"\t{side.title()}")

def sandwich_done(sandwich):
    """Confirms if the sandwich is ready!"""
    print(f"{sandwich.title()} sandwich is ready!")
    
sandwich1 = sandwich_maker('mayo','butter')
sandwich_done('mayo butter')

sandwich2 = sandwich_maker('boiled chicken','tomatoes','cucumbers')
sandwich_done('boiled chicken')

sandwich3 = sandwich_maker('boiled egg','tomatoes','ketchup', 'hot sauce')
sandwich_done('boiled egg')