from flask import Flask, request

app = Flask(__name__)
memoria = {'numero': 0}

@app.post('/contador')
def novo_valor():
    valor = request.get_json()
    memoria['numero'] = valor['numero']
    return '', 201

@app.get('/contador')
def exibir():
    return {'numero': memoria['numero']}, 200

@app.put('/contador/incrementa')
def incrementa():
    memoria['numero'] += 1
    return '', 202

@app.delete('/contador')
def zerar():
    memoria['numero'] = 0
    return '', 202    

if __name__ == '__main__':
    app.run(debug=True)