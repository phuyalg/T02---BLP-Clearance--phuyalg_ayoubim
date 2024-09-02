class User:  # User class that manages user actions/privileges
    def __init__(self, name, clearance):
        self.name = name
        self.clearance = clearance

    def __str__(self):
        return f"{self.name}({self.clearance})"


class File: # File class that manages file creation, reading, & writing
    def __init__(self, file_name, clearance):
        self.file_name = file_name
        self.clearance = clearance
        self.content = ""

    def read(self):
        return self.content

    def write(self, new_content):
        self.content = new_content


def main():
    user1 = User("Larry", "public")
    print(user1)


main()
