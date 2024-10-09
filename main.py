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
        execute_query(conn, query, (firstname, lastname))
        
        return jsonify({"message": "Investor created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/investor/<int:id>', methods=['GET'])
def get_investor(id):
    try:
        query = "SELECT * FROM investor WHERE id = %s"
        investor = execute_read_query(conn, query, (id,))
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

### Similar CRUD for Stock, Bond, StockTransaction, BondTransaction ###

# Create CRUD APIs for stock, bond, stocktransaction, and bondtransaction similar to the investor API above.

app.run()
