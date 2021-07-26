# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have
# that information, call make_album() with the user’s input and print the 
# dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name,album_title,album_year=None):
    """This function makes a dictionary of a music album"""
    # wrong way to build a dictionary
    # dic = f"'Artist':'{artist_name.title()}', 'Title':'{album_title.title()}'"
    dic = {'Artist': artist_name.title(), 'Title':album_title.title()}
    if album_year: # optional: if the year is specified, add it to the dic
        dic['Year'] = album_year
    return dic

# album1 = make_album('richard marx','limitless',2020)
# album2 = make_album('richard marx','stories to tell')
# album3 = make_album('bon jovi','have a nice day',2005)

# print(album1,album2,album3)
# print(album1)
# print(album2)
# print(album3)


prompt1 = "\nEnter an album's artist?"
prompt1 += "\nHit 'q' at any time to stop making albums: "

prompt2 = "\nEnter an album's title?: "
prompt2 += "\nHit 'q' at any time to stop making albums: "

while True:
    artist = input(prompt1)
    if artist == 'q':
        break
    
    title = input(prompt2)
    if title == 'q':
        break
    
    album = make_album(artist,title)
    print (f"\nNew Album made: {album}")