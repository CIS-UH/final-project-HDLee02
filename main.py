import flask
from flask import request, jsonify
import creds
from sql import create_connection, execute_query, execute_read_query

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Set up your connection
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

### CRUD for Investor Table ###

@app.route('/api/investor', methods=['POST'])
def create_investor():
    try:
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        
        query = "INSERT INTO investor (firstname, lastname) VALUES (%s, %s)"
        execute_query(conn, query, (firstname, lastname))  # Pass the parameters
        
        return jsonify({"message": "Investor created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/investor/<int:id>', methods=['GET'])
def get_investor(id):
    try:
        query = "SELECT * FROM investor WHERE id = %s"
        investor = execute_read_query(conn, query, (id,))  # Pass ID as parameter
        return jsonify(investor), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/investor/<int:id>', methods=['PUT'])
def update_investor(id):
    try:
        data = request.get_json()
        firstname = data['firstname']
        lastname = data['lastname']
        
        query = "UPDATE investor SET firstname = %s, lastname = %s WHERE id = %s"
        execute_query(conn, query, (firstname, lastname, id))
        
        return jsonify({"message": "Investor updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/investor/<int:id>', methods=['DELETE'])
def delete_investor(id):
    try:
        query = "DELETE FROM investor WHERE id = %s"
        execute_query(conn, query, (id,))
        return jsonify({"message": "Investor deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

### CRUD for Stock Table ###

@app.route('/api/stock', methods=['POST'])
def create_stock():
    try:
        data = request.get_json()
        stockname = data['stockname']
        abbreviation = data['abbreviation']
        currentprice = data['currentprice']
        
        query = "INSERT INTO stock (stockname, abbreviation, currentprice) VALUES (%s, %s, %s)"
        execute_query(conn, query, (stockname, abbreviation, currentprice))
        
        return jsonify({"message": "Stock created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/stock/<int:id>', methods=['GET'])
def get_stock(id):
    try:
        query = "SELECT * FROM stock WHERE id = %s"
        stock = execute_read_query(conn, query, (id,))
        return jsonify(stock), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/stock/<int:id>', methods=['PUT'])
def update_stock(id):
    try:
        data = request.get_json()
        stockname = data['stockname']
        abbreviation = data['abbreviation']
        currentprice = data['currentprice']
        
        query = "UPDATE stock SET stockname = %s, abbreviation = %s, currentprice = %s WHERE id = %s"
        execute_query(conn, query, (stockname, abbreviation, currentprice, id))
        
        return jsonify({"message": "Stock updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/stock/<int:id>', methods=['DELETE'])
def delete_stock(id):
    try:
        query = "DELETE FROM stock WHERE id = %s"
        execute_query(conn, query, (id,))
        return jsonify({"message": "Stock deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

### CRUD for Bond Table ###

@app.route('/api/bond', methods=['POST'])
def create_bond():
    try:
        data = request.get_json()
        bondname = data['bondname']
        abbreviation = data['abbreviation']
        currentprice = data['currentprice']
        
        query = "INSERT INTO bond (bondname, abbreviation, currentprice) VALUES (%s, %s, %s)"
        execute_query(conn, query, (bondname, abbreviation, currentprice))
        
        return jsonify({"message": "Bond created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/bond/<int:id>', methods=['GET'])
def get_bond(id):
    try:
        query = "SELECT * FROM bond WHERE id = %s"
        bond = execute_read_query(conn, query, (id,))
        return jsonify(bond), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/bond/<int:id>', methods=['PUT'])
def update_bond(id):
    try:
        data = request.get_json()
        bondname = data['bondname']
        abbreviation = data['abbreviation']
        currentprice = data['currentprice']
        
        query = "UPDATE bond SET bondname = %s, abbreviation = %s, currentprice = %s WHERE id = %s"
        execute_query(conn, query, (bondname, abbreviation, currentprice, id))
        
        return jsonify({"message": "Bond updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/bond/<int:id>', methods=['DELETE'])
def delete_bond(id):
    try:
        query = "DELETE FROM bond WHERE id = %s"
        execute_query(conn, query, (id,))
        return jsonify({"message": "Bond deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

### CRUD for StockTransaction Table ###

@app.route('/api/stocktransaction', methods=['POST'])
def create_stock_transaction():
    try:
        data = request.get_json()
        print(data)  # Add this to see the received data
        investorid = data['investorid']
        stockid = data['stockid']
        quantity = data['quantity']
        
        query = "INSERT INTO stocktransaction (investorid, stockid, quantity) VALUES (%s, %s, %s)"
        execute_query(conn, query, (investorid, stockid, quantity))
        
        return jsonify({"message": "Stock transaction created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    
# GET all stock transactions or a specific transaction by ID
@app.route('/api/stocktransaction', methods=['GET'])
def get_all_stock_transactions():
    try:
        query = "SELECT * FROM stocktransaction"
        transactions = execute_read_query(conn, query)
        return jsonify(transactions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/stocktransaction/<int:id>', methods=['GET'])
def get_stock_transaction(id):
    try:
        query = "SELECT * FROM stocktransaction WHERE id = %s"
        transaction = execute_read_query(conn, query, (id,))
        return jsonify(transaction), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# PUT to update stock transaction
@app.route('/api/stocktransaction/<int:id>', methods=['PUT'])
def update_stock_transaction(id):
    try:
        data = request.get_json()
        quantity = data['quantity']
        
        query = "UPDATE stocktransaction SET quantity = %s WHERE id = %s"
        execute_query(conn, query, (quantity, id))
        
        return jsonify({"message": "Stock transaction updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/stocktransaction/<int:id>', methods=['DELETE'])
def delete_stock_transaction(id):
    try:
        query = "DELETE FROM stocktransaction WHERE id = %s"
        execute_query(conn, query, (id,))
        return jsonify({"message": "Stock transaction deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

### CRUD for BondTransaction Table ###

@app.route('/api/bondtransaction', methods=['POST'])
def create_bond_transaction():
    try:
        data = request.get_json()
        investorid = data['investorid']
        bondid = data['bondid']
        quantity = data['quantity']
        
        query = "INSERT INTO bondtransaction (investorid, bondid, quantity) VALUES (%s, %s, %s)"
        execute_query(conn, query, (investorid, bondid, quantity))
        
        return jsonify({"message": "Bond transaction created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# GET all bond transactions or a specific transaction by ID
@app.route('/api/bondtransaction', methods=['GET'])
def get_all_bond_transactions():
    try:
        query = "SELECT * FROM bondtransaction"
        transactions = execute_read_query(conn, query)
        return jsonify(transactions), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/bondtransaction/<int:id>', methods=['GET'])
def get_bond_transaction(id):
    try:
        query = "SELECT * FROM bondtransaction WHERE id = %s"
        transaction = execute_read_query(conn, query, (id,))
        return jsonify(transaction), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# PUT to update bond transaction
@app.route('/api/bondtransaction/<int:id>', methods=['PUT'])
def update_bond_transaction(id):
    try:
        data = request.get_json()
        quantity = data['quantity']
        
        query = "UPDATE bondtransaction SET quantity = %s WHERE id = %s"
        execute_query(conn, query, (quantity, id))
        
        return jsonify({"message": "Bond transaction updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/bondtransaction/<int:id>', methods=['DELETE'])
def delete_bond_transaction(id):
    try:
        query = "DELETE FROM bondtransaction WHERE id = %s"
        execute_query(conn, query, (id,))
        return jsonify({"message": "Bond transaction deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


app.run()