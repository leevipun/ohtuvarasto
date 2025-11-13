from varasto import Varasto


class VarastoItem:  # pylint: disable=too-few-public-methods
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class VarastoManager:
    def __init__(self):
        self.warehouses = {}
        self.next_id = 1

    def create_warehouse(self, name, capacity):
        warehouse_id = self.next_id
        self.next_id += 1
        self.warehouses[warehouse_id] = {
            'id': warehouse_id,
            'name': name,
            'varasto': Varasto(capacity),
            'items': {}
        }
        return warehouse_id

    def get_warehouse(self, warehouse_id):
        return self.warehouses.get(warehouse_id)

    def get_all_warehouses(self):
        return list(self.warehouses.values())

    def update_warehouse(self, warehouse_id, name=None, capacity=None):
        if warehouse_id not in self.warehouses:
            return False
        warehouse = self.warehouses[warehouse_id]
        if name is not None:
            warehouse['name'] = name
        if capacity is not None:
            old_saldo = warehouse['varasto'].saldo
            warehouse['varasto'] = Varasto(capacity, old_saldo)
        return True

    def delete_warehouse(self, warehouse_id):
        if warehouse_id in self.warehouses:
            del self.warehouses[warehouse_id]
            return True
        return False

    def add_item(self, warehouse_id, item_name, quantity):
        if warehouse_id not in self.warehouses:
            return False
        warehouse = self.warehouses[warehouse_id]
        if quantity > warehouse['varasto'].paljonko_mahtuu():
            return False
        if item_name in warehouse['items']:
            warehouse['items'][item_name] += quantity
        else:
            warehouse['items'][item_name] = quantity
        warehouse['varasto'].lisaa_varastoon(quantity)
        return True

    def update_item(self, warehouse_id, item_name, new_quantity):  # pylint: disable=too-many-statements
        if warehouse_id not in self.warehouses:
            return False
        warehouse = self.warehouses[warehouse_id]
        if item_name not in warehouse['items']:
            return False
        old_quantity = warehouse['items'][item_name]
        diff = new_quantity - old_quantity
        if diff > 0 and diff > warehouse['varasto'].paljonko_mahtuu():
            return False
        if diff > 0:
            warehouse['varasto'].lisaa_varastoon(diff)
        elif diff < 0:
            warehouse['varasto'].ota_varastosta(-diff)
        warehouse['items'][item_name] = new_quantity
        return True

    def remove_item(self, warehouse_id, item_name):
        if warehouse_id not in self.warehouses:
            return False
        warehouse = self.warehouses[warehouse_id]
        if item_name not in warehouse['items']:
            return False
        quantity = warehouse['items'][item_name]
        warehouse['varasto'].ota_varastosta(quantity)
        del warehouse['items'][item_name]
        return True

    def get_items(self, warehouse_id):
        if warehouse_id not in self.warehouses:
            return None
        return self.warehouses[warehouse_id]['items']
