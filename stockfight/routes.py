from stockfight import app


@app.route('/')
def home():
    return '<h1>Home</h1>'
