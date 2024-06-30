class Book:
    def __init__(self, title, availability_status):
        self.title = title
        self.availability_status = availability_status

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Avalability: {self.availability_status}")

    # getter
    def get_availability(self):
        return self.availability_status

    # setter
    def set_availability(self, status):
        # why is it status in Available and Not available? where do i change the status if it's not in the setter
        if status in ["Available", "Not Available"]:
            self.availability_status = status
        else:
            print("Invalid status. Please set status to 'Available' or 'Not Available'.")



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # getter for library_id
    def get_library_id(self):
        return self.id

    # setter for library_id
    def set_library_id(self, id):  # need to pass in a libary id to update
        self.id = id

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Library ID: {self.id}")

    










