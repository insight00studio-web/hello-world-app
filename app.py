from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    # Renderなどの環境でポート番号が指定される場合に対応
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
