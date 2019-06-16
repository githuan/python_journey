#!/usr/bin/env python3


def make_album(title, artist, year=None):
    """Return a dictionary of information about album."""
    album = {'title': title, 'artist': artist}
    if year:
        album['year'] = year
    return album


while True:
    print("\nPlease tell me your song title and artist to make an album:")
    print("(Enter 'q' at any time to quit)")


    song_title = input("Song Title: ")
    if song_title == 'q':
        break


    song_artist = input("Song Artist: ")
    if song_artist == 'q':
        break

    song_year= input("Release Year: ")
    if song_year== 'q':
        break

    formatted_album = make_album(song_title, song_artist, song_year)
    print("\nHere is your album:")
    print(f"\t***{formatted_album}***")
