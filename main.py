class User:  # User class that manages user actions/privileges
    def __init__(self, name, clearance):
        self.name = name
        self.clearance = clearance
        self.clearance_level = 0

    def __str__(self):
        return f"{self.name}({self.clearance})"

    def get_clearance_value(self):
        if self.clearance == "her majesty's eyes only" or self.clearance == "Her majesty's eyes only":
            self.clearance_level = 3
        elif self.clearance == "Top secret" or self.clearance == "top secret":
            self.clearance_level = 2
        elif self.clearance == "Secret" or self.clearance == "secret":
            self.clearance_level = 1
        elif self.clearance == "Public" or self.clearance == "public":
            self.clearance_level = 0
        else:
            print("Error, incorrect clearance level")
            return None

        return self.clearance_level

    def get_clearance_name(self):
        return self.clearance

    def can_access(self, file):
        return self.get_clearance_value() >= file.get_clearance_level()

    def attempt_read(self, file):
        if self.can_access(file):
            return file.read()
        else:
            print("Access denied: Insufficient clearance level for reading")

    def attempt_write(self, file, content):
        if self.can_access(file):
            return file.write(content)
        else:
            print("Access denied: Clearance level too low for writing")


class File:  # File class that manages file creation, reading, & writing
    def __init__(self, file_name, clearance):
        self.file_name = file_name
        self.clearance = clearance
        self.clearance_level = 0
        self.content = ""

    def __str__(self):
        return f"{self.file_name}({self.clearance})\n {self.content}"

    def read(self):
        return self.content

    def write(self, new_content):
        self.content = self.content + "\n" + new_content

    def get_title(self):
        return self.file_name

    def get_clearance_level(self):
        if self.clearance == "her majesty's eyes only" or self.clearance == "Her majesty's eyes only":
            self.clearance_level = 3
        elif self.clearance == "Top secret" or self.clearance == "top secret":
            self.clearance_level = 2
        elif self.clearance == "Secret" or self.clearance == "secret":
            self.clearance_level = 1
        elif self.clearance == "Public" or self.clearance == "public":
            self.clearance_level = 0
        else:
            print("Error, incorrect clearance level")
            return None

        return self.clearance_level


def main():
    user1 = User("Shemp", "public")
    print(user1)
    file1 = File("created_by_shemp.txt", user1.get_clearance_name())
    user1.attempt_write(file1, "Hi, this is Shemp. I can write this because this file is public, and I have public "
                               "clearance.")
    print(file1)

    print("\n")

    user2 = User("Curly", "secret")
    print(user2)
    user2.attempt_write(file1, "Hi, this is Curly. I can also write this file because I have secret clearance.")
    print(file1)

    print("\n")

    user3 = User("Larry", "top secret")
    print(user3)
    file2 = File("created_by_Larry", user3.get_clearance_name())
    user3.attempt_write(file2, "Hi, this is Larry. Curly should not be able to read or access this top-secret file.")
    print(file2)
    user2.attempt_read(file2)

    print("\n")

    user4 = User("Moe", "her majesty's eyes only")
    print(user4)
    user4.attempt_write(file2, "Hi, this is Moe. I can write on Larry's file because I have 'Her majesty's eyes only"
                               " clearance'.")
    print(file2)


main()
