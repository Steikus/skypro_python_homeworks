class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirstName(self):
        print(self.first_name)

    def sayLastName(self):
        print(self.last_name)

    def sayBoth(self):
        print(self.first_name, self.last_name)
