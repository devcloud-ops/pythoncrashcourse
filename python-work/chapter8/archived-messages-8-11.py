# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling 
# the function, print both of your lists to show that the original list has 
# retained its messages.

sent_msgs = []
txt_msgs = [
    "assalam o alikum",
    "how are you doing, mate?",
    "chao",
    "have a good one",
    "cheers",
    "bye bye",
    "see you!"
]

def show_messages(txt_msgs,sent_msgs):
    """Prints messages and moves them to sent items"""
    for msg in txt_msgs:
        print(f"\t{msg}.")
        sent_msgs.append(msg)
        
def print_messages(lists):
    """Prints a list"""
    for list in lists:
        print(f"{list}")


# prints each text message and moves each message to a new list called 
# sent_messages
show_messages(txt_msgs[:],sent_msgs)


# print both of your lists to make sure the messages were moved correctly
print("\nOriginal List: ")
print_messages(txt_msgs)
print("\nSent List: ")
print_messages(sent_msgs)