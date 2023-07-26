import webbrowser
import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

with open(f"{script_directory}/mangas.txt") as MangaFile:
    mangas = MangaFile.read()
    mangasSplit = mangas.split("\n")
    x = slice(len(mangasSplit) - 1)
    urls = mangasSplit[x]

print("Available mangas: ")

for index, url in enumerate(urls):
    url_split = url.split("/")
    last_position = url_split[len(url_split) - 1]
    manga_name_dict = last_position.split("-")
    manga_name = " ".join(manga_name_dict)
    print(f"{index}. {manga_name.capitalize()}")

option = int(input("Select a manga: "))

webbrowser.open(urls[option], new=0, autoraise=True)
