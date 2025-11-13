# ohtuvarasto

[![GHA workflow badge](https://github.com/leevipun/ohtuvarasto/actions/workflows/CI/badge.svg)](https://github.com/leevipun/ohtuvarasto/actions)

[![codecov](https://codecov.io/gh/leevipun/ohtuvarasto/graph/badge.svg?token=SYTZO04NX1)](https://codecov.io/gh/leevipun/ohtuvarasto)

## Web User Interface

A warehouse management web application built with Flask that supports managing multiple warehouses and their inventory items.

### Features

- **Warehouse Management**: Create, view, edit, and delete warehouses
- **Inventory Management**: Add, update, and remove items within warehouses
- **Capacity Tracking**: Monitor warehouse capacity, current balance, and available space
- **Web Interface**: User-friendly HTML interface with responsive design
- **REST API**: JSON API endpoints for programmatic access

### Running the Application

Install dependencies:
```bash
poetry install
```

Start the Flask development server:
```bash
cd src
poetry run python app.py
```

The application will be available at `http://127.0.0.1:5000`

### API Endpoints

- `GET /api/warehouses` - List all warehouses
- `POST /api/warehouses` - Create a new warehouse
- `GET /api/warehouses/<id>` - Get warehouse details
- `PUT /api/warehouses/<id>` - Update warehouse
- `DELETE /api/warehouses/<id>` - Delete warehouse
- `POST /api/warehouses/<id>/items` - Add item to warehouse

### Running Tests

```bash
poetry run pytest src/tests/
```

### Code Quality

```bash
poetry run pylint src --ignore=tests
```
