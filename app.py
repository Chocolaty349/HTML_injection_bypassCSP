from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    input = request.args.get('input','')
    r = make_response(render_template('index.html', input=input))
    r.headers.set('Content-Security-Policy', "default-src 'self'; script-src 'self' 'unsafe-inline' ajax.googleapis.com")
    # return render_template('index.html', input=input)
    return r
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)