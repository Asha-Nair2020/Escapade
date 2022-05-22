import unittest
from unittest import TestCase
from utils import password_checker, login, utilities, homepage, user, register


class MyTestCase(TestCase):
    def test_password_meets_requirements(self):
        self.assertEqual(password_checker(registeredpassword="Password97!"), True)  # add assertion here

    def test_password_not_meets_requirements(self):
        self.assertEqual(password_checker(registeredpassword="hi"), False)  # add assertion here

    def test_register_login(self):
        expected = {'Option': [1,2], 'Name': ['Register','Login']}
        actual = utilities.login_or_register(self)
        self.assertEqual(expected, actual)


    def test_view_menu(self):
        expected = {1: 'Attractions', 2: 'Restaurants',
                    3: 'Experience Nature', 4: 'Shopping', 5: 'Hotels', 0: 'Return to Main Menu'}
        actual = utilities.view_menu(self)
        self.assertEqual(expected, actual)


    def test_view_main_menu(self):
        expected = {1: 'Search', 2: 'Help', 0: 'Exit Application'}
        actual = utilities.view_main_menu(self)
        self.assertEqual(expected, actual)


    def test_create_table(self):
        info = {"The Alchemist", "6 Bevis Marks,London EC3A 7BA,United Kingdom", "Restaurants", "+44 20 7283 8800"}
        actual = utilities.create_table(self, info)
        self.assertIsNotNone(actual)

    def test_homepage(self):
        usr = user(9, "Suad Ali", "Suad@hotmail.com", "Suad@1234")
        self.assertEqual(homepage().name, usr.name)

    def test_register(self):
        self.assertIsNotNone(register())

    def test_login(self):
        self.assertIsNotNone(login())


if __name__ == '__main__':
    unittest.main()