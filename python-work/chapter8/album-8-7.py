# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing 
# different albums. Print each return value to show that the dictionaries are 
# storing the album information correctly.

# Use None to add an optional parameter to make_album() that allows you to
# store the year that album was released. If the calling line includes a value 
# for the year of album release, add that value to the album’s dictionary. Make at 
# least one new function call that includes the year of release of that album.

def make_album(artist_name,album_title,album_year=None):
    """This function makes a dictionary of a music album"""
    # wrong way to build a dictionary
    # dic = f"'Artist':'{artist_name.title()}', 'Title':'{album_title.title()}'"
    dic = {'Artist': artist_name.title(), 'Title':album_title.title()}
    if album_year: # optional: if the year is specified, add it to the dic
        dic['Year'] = album_year
    return dic

album1 = make_album('richard marx','limitless',2020)
album2 = make_album('richard marx','stories to tell')
album3 = make_album('bon jovi','have a nice day',2005)

# print(album1,album2,album3)
print(album1)
print(album2)
print(album3)