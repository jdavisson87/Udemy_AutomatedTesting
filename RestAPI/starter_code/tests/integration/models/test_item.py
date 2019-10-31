from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with the name {item.name}, but expected not to.")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 "Did not find item with the name {item.name}")

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with the name {item.name}, but expected not to.")