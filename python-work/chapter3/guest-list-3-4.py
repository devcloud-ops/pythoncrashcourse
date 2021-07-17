# If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

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
