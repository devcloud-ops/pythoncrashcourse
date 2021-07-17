# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.

# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.

# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.

# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.

# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

################################ 3-5 #############################################

guest_list=[]
guest_list.append ('alex')
guest_list.append ('james')
guest_list.append ('john')

print(f'\nDear All, please be informed that I have invitied {len(guest_list)} guests to dinner including {guest_list}\n')
#output: Dear All, please be informed that I have invitied 3 guests to dinner including ['alex', 'james', 'john']

print(f'Hey {guest_list[0].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey Alex, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[1].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey James, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[2].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey John, you are cordially invited to my place for dinner on 3-3-3033.

################################ 3-6 #############################################

print('Dear All, please be informed that I have found a bigger dinner table, and so I will be inviting 3 more friends to this dinner. \n')
#output: Dear All, please be informed that I have found a bigger dinner table, and so I will be inviting 3 more friends to this dinner.

guest_list.insert(0, 'alan')
guest_list.insert(2, 'robert')
guest_list.append('caroline')

print(f'Here are the list of invitee to this dinner: {guest_list}.\n')
#output: Hey Alex, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[0].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey Alex, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[1].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey James, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[2].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey John, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[3].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey Alex, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[4].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey James, you are cordially invited to my place for dinner on 3-3-3033.

print(f'Hey {guest_list[5].title()}, you are cordially invited to my place for dinner on 3-3-3033.\n')
#output: Hey John, you are cordially invited to my place for dinner on 3-3-3033.

################################ 3-7 #############################################

print(f'\nDear All, change of plans; my dinner table won\'t be arriving in due time, so I can invite only two people to this dinner now.\n')
#output: Dear All, change of plans; my dinner table won\'t be arriving in due time, so I can invite only two people to this dinner now

guest_list_before_removal = guest_list
print(guest_list_before_removal)

caroline_removed = guest_list.pop(5).title()
print(f"\n Dear {caroline_removed}, apologies, but due to unavailability of a bigger dinner table, I won't be able to host you at my place for dinner on 3-3-3033.")

john_removed = guest_list.pop(4).title()
print(f"\n Dear {john_removed}, apologies, but due to unavailability of a bigger dinner table, I won't be able to host you at my place for dinner on 3-3-3033.")

james_removed = guest_list.pop(3).title()
print(f"\n Dear {james_removed}, apologies, but due to unavailability of a bigger dinner table, I won't be able to host you at my place for dinner on 3-3-3033.")

robert_removed = guest_list.pop(2).title()
print(f"\n Dear {robert_removed}, apologies, but due to unavailability of a bigger dinner table, I won't be able to host you at my place for dinner on 3-3-3033.")


print(f'\nDear {guest_list[0].title()}, please be informed that you are still invited to my place for dinner on 3-3-3033.\n')
#output: Hey Alan, please be informed that you are still invited to my place for dinner on 3-3-3033.

print(f'Dear {guest_list[1].title()}, please be informed that you are still invited to my place for dinner on 3-3-3033.\n')
#output: Hey Alex, please be informed that you are still invited to my place for dinner on 3-3-3033.

del guest_list[0]
del guest_list[0]
print(f'The guest list: guest_list now have {len(guest_list)} members!')
