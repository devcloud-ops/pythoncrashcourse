# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.

# • Use insert() to add one new guest to the beginning of your list.

# • Use insert() to add one new guest to the middle of your list.

# • Use append() to add one new guest to the end of your list.

# • Print a new set of invitation messages, one for each person in your list.

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