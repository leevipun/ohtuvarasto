import unittest
from varasto_manager import VarastoManager


class TestVarastoManager(unittest.TestCase):
    def setUp(self):
        self.manager = VarastoManager()

    def test_create_warehouse(self):
        warehouse_id = self.manager.create_warehouse("Test", 100)
        self.assertIsNotNone(warehouse_id)
        warehouse = self.manager.get_warehouse(warehouse_id)
        self.assertEqual(warehouse['name'], "Test")
        self.assertEqual(warehouse['varasto'].tilavuus, 100)

    def test_get_all_warehouses(self):
        self.manager.create_warehouse("W1", 100)
        self.manager.create_warehouse("W2", 200)
        warehouses = self.manager.get_all_warehouses()
        self.assertEqual(len(warehouses), 2)

    def test_update_warehouse(self):
        wid = self.manager.create_warehouse("Old", 100)
        success = self.manager.update_warehouse(wid, name="New")
        self.assertTrue(success)
        warehouse = self.manager.get_warehouse(wid)
        self.assertEqual(warehouse['name'], "New")

    def test_delete_warehouse(self):
        wid = self.manager.create_warehouse("Test", 100)
        success = self.manager.delete_warehouse(wid)
        self.assertTrue(success)
        self.assertIsNone(self.manager.get_warehouse(wid))

    def test_add_item(self):
        wid = self.manager.create_warehouse("Test", 100)
        success = self.manager.add_item(wid, "Item1", 10)
        self.assertTrue(success)
        items = self.manager.get_items(wid)
        self.assertEqual(items['Item1'], 10)

    def test_update_item(self):
        wid = self.manager.create_warehouse("Test", 100)
        self.manager.add_item(wid, "Item1", 10)
        success = self.manager.update_item(wid, "Item1", 20)
        self.assertTrue(success)
        items = self.manager.get_items(wid)
        self.assertEqual(items['Item1'], 20)

    def test_remove_item(self):
        wid = self.manager.create_warehouse("Test", 100)
        self.manager.add_item(wid, "Item1", 10)
        success = self.manager.remove_item(wid, "Item1")
        self.assertTrue(success)
        items = self.manager.get_items(wid)
        self.assertNotIn('Item1', items)

    def test_add_item_exceeds_capacity(self):
        wid = self.manager.create_warehouse("Test", 10)
        success = self.manager.add_item(wid, "Item1", 20)
        self.assertFalse(success)
