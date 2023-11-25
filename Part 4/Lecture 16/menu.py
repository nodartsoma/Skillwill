import sys
import json
from diarybook import DiaryBook
from util import read_from_json_into_application


class Menu:

    def __init__(self):
        self.diarybook = DiaryBook()

        self.choices = {
            "1": self.show_all_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.sort_diaries,
            '5': self.quit
        }

    def display_menu(self):
        print("""
                Notebook Menu:
                   
                1. Show diaries
                2. Add diary
                3. Search diaries
                4. Sort diaries
                5. Quit program
                """)

    def run(self):
        self.populate_database()
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")


    def show_all_diaries(self):
        if len(self.diarybook.diaries) == 0:
            print("There are no diaries in the database!")
        else:
            for diary in self.diarybook.diaries:
                print(f"{diary.id} - {diary.memo}")

    def add_diary(self):
        memo = input("Enter a memo: ")
        tags = input("add tags: ")
        self.diarybook.new_diary(memo, tags)
        with open('../Skillwill/Part 4/data.json', 'r') as file:
            json_data = json.load(file)
        json_data.append({'memo': memo, 'tags': tags})
        with open("../Skillwill/Part 4/data.json", "w") as outfile:
            json.dump(json_data, outfile, indent=2)
        print("Your note has been added")

    def search_diaries(self):
        keyword = input("Enter a keyword")
        filtered_diaries = self.diarybook.search_diary(keyword)
        if len(filtered_diaries) == 0:
            print("The matching diary can't be found")
        else:
            for diary in filtered_diaries:
                print(f"{diary.id} - {diary.memo}")

    def sort_diaries(self):
        id_or_memo = input("Insert how you want to sort by: (id) or (memo): ")
        diaries = self.diarybook.diaries
        sorted_diaries = []
        if id_or_memo == "id":
            for diary in diaries:
                print(f"{diary.id} - {diary.memo}")
        elif id_or_memo == "memo":
            for diary in diaries:
                sorted_diaries.append(diary.memo)
            sorted_diaries.sort()
            for i in sorted_diaries:
                print(i)
        else:
            print("I said, (id) or (memo)!")
            self.sort_diaries()

    def quit(self):

        print("Thank you for using diarybook today")
        sys.exit(0)

    def populate_database(self):
        diaries1 = read_from_json_into_application('../Skillwill/Part 4/data.json')
        for diary in diaries1:
            self.diarybook.diaries.append(diary)


if __name__ == "__main__":
    Menu().run()