class User:
    def __init__(self, name, clearance):
        self.name = name
        self.clearance = clearance
    def __str__(self):
        return f"{self.name}({self.clearance})"
def main():
    user1 = User("Larry", "public")
    print(user1)

main()
