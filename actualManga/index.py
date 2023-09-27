import webbrowser
import sys
import sqlite3
import os


# FUNCTIONS
def createConnection(connection):
    con = None
    try:
        con = sqlite3.connect(connection)
    except sqlite3.Error as e:
        print(e)

    return con


def listMangas(cursor):
    mangas_list = []
    mangas = cursor.execute("SELECT id, name FROM mangas")
    # count = len(mangas.fetchall())
    for manga in mangas:
        # print(f"{manga[0]}. {manga[1]}")
        mangas_list.append({"id": manga[0], "name": manga[1]})

    for manga in mangas_list:
        print(f"{manga['id']}. {manga['name']}")

    return len(mangas_list)


def deleteManga(cursor, con):
    try:
        option = int(input("Select a manga: "))
        delete = cursor.execute("DELETE FROM mangas WHERE id = ?", (option,))
        con.commit()
        if delete.rowcount > 0:
            print("Delete succesfully!!!")
        else:
            print("This ID doesn't exists")
            exit(1)
    except KeyboardInterrupt:
        exit(1)
    except Exception as e:
        print(e)


def openURL(cursor):
    try:
        option = int(input("\nSelect a manga: "))
        url = cursor.execute("SELECT url FROM mangas WHERE id=?", (int(option),))
        webbrowser.open(url.fetchone()[0], new=0, autoraise=True)
    except KeyboardInterrupt:
        exit(1)


def insertManga(cursor, con):
    try:
        url = input("Introduce url: ")
    except KeyboardInterrupt:
        exit(1)

    url_split = url.split("/")
    last_position = url_split[len(url_split) - 1]
    manga_name_dict = last_position.split("-")
    manga_name = " ".join(manga_name_dict)
    manga_name = manga_name.capitalize()

    cursor.execute("INSERT INTO mangas (name, url) VALUES (?,?)", (manga_name, url))
    con.commit()


def main():
    current_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    database = f"{current_path}/mangas.db"
    con = createConnection(database)
    cursor = con.cursor()
    cursor.execute(
        """
       CREATE TABLE IF NOT EXISTS mangas (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL,
           url TEXT NOT NULL
       )
    """
    )

    args = sys.argv

    possible_options = ["ls", "new", "del"]

    if len(args) == 1:
        print("\tls -> List the mangas \n\tnew -> Add new manga \n\tdel -> Delete manga")
        exit()
    else:
        command = args[1]
        if not possible_options.count(command):
            exit(1)

    # OPTIONS
    if command == "ls":
        count = listMangas(cursor)
        # TODO: Check if the number option exists
        if count > 0:
            openURL(cursor)

    if command == "new":
        insertManga(cursor, con)

    if command == "del":
        listMangas(cursor)
        deleteManga(cursor, con)


if __name__ == "__main__":
    main()
