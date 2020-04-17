import unittest

from DataBase import *


class TestDataBase(unittest.TestCase):

    def test_init(self):
        db = DataBase('data')
        self.assertEqual(
            os.path.exists('data.csv'),
            True,
            "File does not exist")

    def test_del(self):
        db = DataBase('data')
        db.__del__()
        self.assertEqual(os.path.exists('data.csv'), True, "File was deleted")

    def test_delete(self):
        db = DataBase('data')
        db.delete()
        self.assertEqual(
            os.path.exists('data.csv'),
            False,
            "File was not deleted")

    def test_add_with_phone(self):
        db = DataBase('data')
        db.add_with_phone(1, 'a', 'b', '8')
        self.assertEqual(
            db.data_base[1]['PhoneNum'],
            '8',
            "Phone Num was not added")

    def test_add_without_phone(self):
        db = DataBase('data')
        db.add_without_phone(1, 'a', 'b')
        self.assertEqual(
            db.data_base[1]['PhoneNum'],
            r'¯\_(ツ)_/¯',
            "Phone Num was not added")

    def test_edit_id(self):
        db = DataBase('data')
        db.add_with_phone(1, 'a', 'b', '8')
        db.edit_id(1, 2)
        self.assertEqual(db.data_base[2]['PhoneNum'], '8', "ID was not edited")

    def test_edit_name(self):
        db = DataBase('data')
        db.add_with_phone(1, 'a', 'b', '8')
        db.edit_name(1, 'c')
        self.assertEqual(db.data_base[1]['Name'], 'c', "Name was not edited")

    def test_edit_surname(self):
        db = DataBase('data')
        db.add_with_phone(1, 'a', 'b', '8')
        db.edit_surname(1, 'c')
        self.assertEqual(
            db.data_base[1]['Surname'],
            'c',
            "Surname was not edited")

    def test_edit_phone_num(self):
        db = DataBase('data')
        db.add_with_phone(1, 'a', 'b', '8')
        db.edit_phone_num(1, 'c')
        self.assertEqual(
            db.data_base[1]['PhoneNum'],
            'c',
            "Phone Num was not edited")


if __name__ == '__main__':
    unittest.main()
