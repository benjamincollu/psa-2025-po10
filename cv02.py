#!/usr/bin/env python3

class LP():
    def __init__(self, name, year, artist, duration):
        self._name = name
        self._year = year
        self._artist = artist
        self._duration = duration
    
    def to_string(self):
        out = "| {1:4} | {0:^20} | {2:20} | {3:3} |".format(self._name, self._year, self._artist, self._duration)
        return out

class Library():
    def __init__(self):
        self._library = list()
    
    def insert_LP(self, lp):
        self._library.append(lp)
    
    def delete_LP(self, lp):
        self._library.remove(lp)
    
    def clear_library(self):
        self._library.clear()
    
    def seed_library(self):
        self.insert_LP(LP("22 dní", 1945, "Miroslav Žbirka", 22))
        self.insert_LP(LP("Biely kvet", 1945, "Miroslav Žbirka", 324))
        self.insert_LP(LP("Paradise City", 1955, "Guns & Roses", 120))
        self.insert_LP(LP("Swimming", 2018, "Mac Miller", 120))
    
    def to_string(self):
        out = "| -------------------------------- |\n"
        out += "| Year | Title | Artist | Duration |\n"
        out += "| -------------------------------- |\n"
        for lp in self._library:
            out += lp.to_string() + "\n"
        out += "| -------------------------------- |"
        return out

def main():
    library = Library()

    while True:
        print("| -------------------------------- |")
        print("|              Menu                |")
        print("| -------------------------------- |")
        print(" 1. Add new LP")
        print(" 2. Remove LP")
        print(" 3. Clear Library")
        print(" 4. Print Library")
        print(" 5. Seed Library")
        print(" q. Exit program")

        choice = input("Select choice: ")

        if choice[0] == "1":
            name = input("Name: ")
            year = input("Year: ")
            artist = input("Artist: ")
            duration = input("Duration: ")
            library.insert_LP(LP(name, int(year), artist, int(duration)))
            continue
        if choice[0] == "2":
            # TODO
            continue
        if choice[0] == "3":
            library.clear_library()
            continue
        if choice[0] == "4":
            print(library.to_string())
            input("Press any key to continue.")
            continue
        if choice[0] == "5":
            library.seed_library()
            continue
        if choice[0] == "q":
            exit()

if __name__ == "__main__":
    main()