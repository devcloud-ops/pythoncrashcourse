# parrot input

prompt = "\nLet me repeat what you just enter now: "
prompt += "\nEnter 'quit' to end the program. "

active = True
msg = ""

while active:
    msg = input(prompt)
    if msg == 'quit':
        active = False
    else:
        print(msg.upper())
    