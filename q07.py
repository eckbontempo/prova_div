from flask import Flask, request

app = Flask(__name__)

@app.post('/soma')
def soma():
    n = request.get_json()
    resultado = n['x'] + n['y']
    return {"resultado": resultado}, 202

if __name__ == '__main__':
    app.run(debug=True)