# 8-9. Messages: Make a list containing a series of short text messages. Pass 
# the list to a function called show_messages(), which prints each text message.

txt_msgs = [
    "assalam o alikum",
    "how are you doing, mate?",
    "chao",
    "have a good one",
    "cheers",
    "bye bye",
    "see you!"
]

def show_messages(msgs):
    for msg in msgs:
        print(f"\t{msg}.")
        
show_messages(txt_msgs)
