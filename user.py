class User:
    """Create class for users."""

        user_list = [] # Empty user list

        def __init__(self, Fname, Lname, Gender, Address, e_mail, Nationality, Status, user_name, password):

            # docstring removed for simplicity
            self.Fname = Fname 
            self.Lname = Lname
            self.Gender = Gender 
            self.Address = Address
            self.e_mail = e_mail 
            self.Nationality = Nationality
            self.e_mail = e_mail 
            self.user_name = user_name
            self.password = password
        
        def save_user(self):
            """Method that saves user objects into user_list"""
            self.user_list.append(self)
        def delete_user(self):
            """Method that delete user objects into user_list"""
            self.user_list.remove(self)

    if __name__ == '__main__':
        main()