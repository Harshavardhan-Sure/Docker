from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/items', methods=['GET'])
def get_items():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json['name']
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name) VALUES (?)', (new_item,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Item added'}), 201

if __name__ == "__main__":
    app.run(debug=True)
