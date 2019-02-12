import unittest # Importing the unittest module
from user import User # Importing the user class


class TestUser(unittest.TestCase):
    """Test class that defines test cases for the user class behaviour"""

    def setUp(self):
        """Set Up Method to run before each test case to check if the class has been instantiated correctly"""
        self.new_user = User("NewUser", "00000")

    def test_init(self):
        """Test to ensure that the object is initialized properly"""
        self.assertEqual(self.new_user.Fname, "carine")
        self.assertEqual(self.new_user.Lname, "Izere")
        self.assertEqual(self.new_user.Gender, "Female")
        self.assertEqual(self.new_user.Address, "Kigali")
        self.assertEqual(self.new_user.e_mail, "carizeree@gmail.com")
        self.assertEqual(self.new_user.Nationality, "Rwanda")
        self.assertEqual(self.new_user.Status, "Married")
        self.assertEqual(self.new_user.user_name, "NewUser")
        self.assertEqual(self.new_user.password, "00000")
    def test_save_user(self):
        """Method that tests wether an user credentials have been successfully saved"""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()