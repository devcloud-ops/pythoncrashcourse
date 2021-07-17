# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.

# • Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.

# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.

# • Print a second set of invitation messages, one for each person who is still
# in your list.

guest_list=[]
guest_list.append ('alex')
guest_list.append ('paul')
guest_list.append ('john')

print(f'\nI have invitied {len(guest_list)} guests for dinner including {guest_list}\n')
#output: I have invitied 3 guests for dinner including ['alex', 'paul', 'john']

print(f'Hey {guest_list[0].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey Alex, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[1].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey Paul, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[2].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey John, you are cordially invited to my place for dinner on 3-3-3033.


################################ 3-5 #############################################

execused_guest = guest_list.pop(1)
print(f'Dear All, please be informed that {execused_guest.title()} will not be attending the dinner due to unforseen circumstances.\n')
#output: Dear All, please be informed that Paul will not be attending the dinner due to unforseen circumstances.

guest_list.insert(1, "james")

print(f'Hey {guest_list[0].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey Alex, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[1].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey James, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[2].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey John, you are cordially invited to my place for dinner on 3-3-3033.


