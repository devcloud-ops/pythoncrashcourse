# parrot input

prompt = "\nLet me repeat what you just enter now: "
prompt += "\nEnter 'quit' to end the program. "

msg = ""
while msg != 'quit':
    msg = input(prompt)
    if msg != 'quit':
        print(msg.upper())