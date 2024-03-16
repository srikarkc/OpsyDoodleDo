from flask import Flask, request, render_template_string
import grpc
import string_service_pb2
import string_service_pb2_grpc

app = Flask(__name__)

# HTML template for the input form and to display the result
HTML_TEMPLATE = '''
<!doctype html>
<html>
    <head><title>String Length Counter</title></head>
    <body>
        <h2>Enter a string to count its characters:</h2>
        <form method="POST">
            <input type="text" name="string" />
            <input type="submit" value="Count Characters" />
        </form>
        <h3>The string has {{ count }} characters.</h3>
    </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    count = None
    if request.method == 'POST':
        user_string = request.form.get('string', '')
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = string_service_pb2_grpc.StringCounterStub(channel)
            response = stub.CountCharacters(string_service_pb2.StringRequest(user_string=user_string))
            count = response.count
    return render_template_string(HTML_TEMPLATE, count=count)

if __name__ == '__main__':
    app.run(debug=True)