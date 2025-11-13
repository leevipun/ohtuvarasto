from flask import Flask, render_template, request, redirect, url_for, jsonify
from varasto_manager import VarastoManager

app = Flask(__name__)
manager = VarastoManager()


@app.route('/')
def index():
    warehouses = manager.get_all_warehouses()
    return render_template('index.html', warehouses=warehouses)


@app.route('/warehouse/new', methods=['GET', 'POST'])
def new_warehouse():
    if request.method == 'POST':
        name = request.form.get('name')
        capacity = float(request.form.get('capacity', 0))
        manager.create_warehouse(name, capacity)
        return redirect(url_for('index'))
    return render_template('new_warehouse.html')


@app.route('/warehouse/<int:warehouse_id>')
def view_warehouse(warehouse_id):
    warehouse = manager.get_warehouse(warehouse_id)
    if not warehouse:
        return "Warehouse not found", 404
    return render_template('warehouse.html', warehouse=warehouse)


@app.route('/warehouse/<int:warehouse_id>/edit', methods=['GET', 'POST'])
def edit_warehouse(warehouse_id):
    warehouse = manager.get_warehouse(warehouse_id)
    if not warehouse:
        return "Warehouse not found", 404
    if request.method == 'POST':
        name = request.form.get('name')
        capacity = float(request.form.get('capacity'))
        manager.update_warehouse(warehouse_id, name, capacity)
        return redirect(url_for('view_warehouse', warehouse_id=warehouse_id))
    return render_template('edit_warehouse.html', warehouse=warehouse)


@app.route('/warehouse/<int:warehouse_id>/delete', methods=['POST'])
def delete_warehouse(warehouse_id):
    manager.delete_warehouse(warehouse_id)
    return redirect(url_for('index'))


@app.route('/warehouse/<int:warehouse_id>/item/add', methods=['POST'])
def add_item(warehouse_id):
    item_name = request.form.get('item_name')
    quantity = float(request.form.get('quantity', 0))
    success = manager.add_item(warehouse_id, item_name, quantity)
    if not success:
        return "Failed to add item", 400
    return redirect(url_for('view_warehouse', warehouse_id=warehouse_id))


@app.route('/warehouse/<int:wid>/item/<item_name>/edit', methods=['POST'])
def edit_item(wid, item_name):
    new_quantity = float(request.form.get('quantity', 0))
    success = manager.update_item(wid, item_name, new_quantity)
    if not success:
        return "Failed to update item", 400
    return redirect(url_for('view_warehouse', warehouse_id=wid))


@app.route('/warehouse/<int:wid>/item/<item_name>/delete', methods=['POST'])
def delete_item(wid, item_name):
    manager.remove_item(wid, item_name)
    return redirect(url_for('view_warehouse', warehouse_id=wid))


@app.route('/api/warehouses', methods=['GET', 'POST'])
def api_warehouses():
    if request.method == 'POST':
        data = request.get_json()
        warehouse_id = manager.create_warehouse(
            data.get('name'), float(data.get('capacity', 0))
        )
        warehouse = manager.get_warehouse(warehouse_id)
        return jsonify({
            'id': warehouse['id'],
            'name': warehouse['name'],
            'capacity': warehouse['varasto'].tilavuus,
            'balance': warehouse['varasto'].saldo
        }), 201
    warehouses = manager.get_all_warehouses()
    return jsonify([{
        'id': w['id'],
        'name': w['name'],
        'capacity': w['varasto'].tilavuus,
        'balance': w['varasto'].saldo,
        'items': w['items']
    } for w in warehouses])


@app.route('/api/warehouses/<int:warehouse_id>',
           methods=['GET', 'PUT', 'DELETE'])
def api_warehouse(warehouse_id):
    warehouse = manager.get_warehouse(warehouse_id)
    if not warehouse:
        return jsonify({'error': 'Warehouse not found'}), 404

    if request.method == 'DELETE':
        manager.delete_warehouse(warehouse_id)
        return '', 204

    if request.method == 'PUT':
        data = request.get_json()
        manager.update_warehouse(
            warehouse_id,
            data.get('name'),
            float(data.get('capacity')) if data.get('capacity') else None
        )
        warehouse = manager.get_warehouse(warehouse_id)

    return jsonify({
        'id': warehouse['id'],
        'name': warehouse['name'],
        'capacity': warehouse['varasto'].tilavuus,
        'balance': warehouse['varasto'].saldo,
        'items': warehouse['items']
    })


@app.route('/api/warehouses/<int:wid>/items', methods=['POST'])
def api_add_item(wid):
    data = request.get_json()
    success = manager.add_item(
        wid, data.get('item_name'), float(data.get('quantity', 0))
    )
    if not success:
        return jsonify({'error': 'Failed to add item'}), 400
    return jsonify({'message': 'Item added successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)
