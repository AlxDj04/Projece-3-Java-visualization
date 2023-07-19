from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['F1database']
collection = db['collection']

@app.route('/api/drivers', methods=['GET'])
def obtener_drivers():
    drivers = collection.find({})
    resultados = collection.distinct('surname')

    return jsonify(resultados)

@app.route('/api/circuits', methods=['GET'])
def obtener_drivers():
    drivers = collection.find({})
    resultados = collection.distinct('circuitRef')

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
