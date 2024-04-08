def make_album(name,title,songs=None):
    album={'artist':name.title(), 'title':title.title()}
    if songs:
        album["songs"]=songs
    return album


#print(make_album('metallica', 'ride the lightning'))
#print(make_album('beethoven', 'ninth symphony'))
#print(make_album('willie nelson', 'red-headed stranger'))
#print(make_album('iron maiden', 'piece of mind', songs=8))

active=True
while active:
    name=input("Enter artist name: (press q to quit) ")
    if name == 'q':
        break
    title=input("Enter album name: (press q to quit) ")
    if title == 'q':
        break
    songs=input("Enter number of songs: (press q to quit) ")
    if name == 'q':
        break
    songs=int(songs)
    print(make_album(name,title,songs))