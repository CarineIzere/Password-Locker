class Credentials:
    """Create class for credentials"""
   credentials_list = []
    def __init__(self, account_Gender, account_Address, account_e_mail, account_Nationality, account_Status, account_user_name, account_user_name, account_password):
        self.account_Fname = account_Fname 
        self.account_Lname = account_Lname
        self.account_Gender = account_Gender 
        self.account_Address = account_Address
        self.account_e_mail = account_e_mail 
        self.account_Nationality = account_Nationality
        self.account_Status = account_Status 
        self.account_user_name = account_user_name
        self.account_password = account_password

    def save_credentials(self):
        """Method that saves credential objects into credentials_list"""
        self.credentials_list.append(self)

    def delete_credential(self):
        """Method which deletes a particular credential"""
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_user_name(cls, account_user_name):
        """Method that takes in a user name and returns a credential that matches that particular name
        Args:
            name: account_user_name that has a password
        Returns:
            The account_user_name and it's corresponding PassWord
        """

        for credential in cls.credentials_list:
            if credential.account_user_name == account_user_name:
                return credential

    @classmethod
    def credential_exists(cls, user_name):
        """Method to check whether a credential exists
        Args:
        name: user_name of account to search whether it exists
        boolean: True or False depending if the contatc exists
        """

        for credential in cls.credentials_list:
            if credential.account_user_name == user_name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """Method which displays all current credentials"""
        return cls.credentials_list