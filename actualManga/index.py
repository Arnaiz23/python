import webbrowser

urls = [
    "https://lectortmo.com/library/manga/78340/el-sabio-desterrado-creo-una-clase-invencible",
    "https://lectortmo.com/library/manhwa/53005/trash-of-the-counts-family",
]

print("Available mangas: ")

for index, url in enumerate(urls):
    url_split = url.split("/")
    last_position = url_split[len(url_split) - 1]
    manga_name_dict = last_position.split("-")
    manga_name = " ".join(manga_name_dict)
    print(f"{index}. {manga_name.capitalize()}")

option = int(input("Select a manga: "))

webbrowser.open(urls[option], new=0, autoraise=True)
