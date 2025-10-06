#!/usr/bin/env python3

class LP():
    def __init__(self, name, year, artist, duration):
        self._name = name
        self._year = year
        self._artist = artist
        self._duration = duration
    
    def to_string(self):
        out = "| {1:4} | {0:^20} | {2:20} | {3:8} |".format(self._name, self._year, self._artist, self._duration)
        return out

class Library():
    def __init__(self):
        self._library = list()
    
    def insert_LP(self, lp):
        self._library.append(lp)
    
    def delete_LP(self, index):
        self._library.pop(index)
    
    def clear_library(self):
        self._library.clear()
    
    def seed_library(self):
        self.insert_LP(LP("22 dní", 1945, "Miroslav Žbirka", 22))
        self.insert_LP(LP("Biely kvet", 1945, "Miroslav Žbirka", 324))
        self.insert_LP(LP("Paradise City", 1955, "Guns & Roses", 120))
        self.insert_LP(LP("Swimming", 2018, "Mac Miller", 120))
    
    def to_string(self):
        out = "|{}|\n".format("-"*68)
        out += "| ID | Year | {:^20} | {:^20} | Duration |\n".format("Title", "Artist")
        i = 0
        for lp in self._library:
            out += "| {:2} {}\n".format(str(i), lp.to_string())
            i += 1
        out += "|{}|\n".format("-"*68)
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
            name = input("name: ")
            year = input("year: ")
            artist = input("artist: ")
            duration = input("duration: ")
            library.insert_LP(LP(name, int(year), artist, int(duration)))
            continue
        if choice[0] == "2":
            print(library.to_string())
            try:
                index = int(input("index: "))
                library.delete_LP(index)
                print(library.to_string())
            except ValueError:
                print("ERROR: Selected value is not an index.")
            except IndexError:
                print("ERROR: Selected value is out of range.")
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