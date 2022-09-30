from flask import Flask, request, session

app = Flask(__name__)

app.secret_key = 'secret_key'

@app.route("/", methods = ['GET', 'POST'])
def hello():

    if session.get('logged_in') == None:
        count = 0
    else:
       count = int(session['logged_in']) + 1

    if request.method == 'GET':
        return f"Hello World!!! Tenemos: {count} Peticiones"
    if request.method == 'POST':
        session['logged_in'] = count 
        return {'Msg':'success post'}




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
