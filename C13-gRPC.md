# Class 13 - gRPC Project

<p align="center">
    <img src="https://grpc.io/img/logos/grpc-icon-color.png" style="width:600px;"/>
</p>

> gRPC is a high-performance, open-source framework designed for efficient, cross-language RPC (Remote Procedure Call) communication using HTTP/2 and Protocol Buffers.
---

### Introduction

Alap and KC want to build an app that communicates using gRPC.

Alap will develop client that send the server a string, the server will count the # of characters in the string and respond.

We will use individual GitHub repositories for source code management.

The code will be deployed onto a Compute Engine VM on GCP using GCP Cloud Build.

---

### Theory

Remote Procedure Call (RPC) is a protocol or a technique used to enable a program to cause a procedure (subroutine) to execute in another address space (commonly on another computer on a shared network), without the programmer explicitly coding the details for this remote interaction. That is, the code execution occurs in such a way that it appears as if the procedure were being called locally.

### How RPC Works:

1. **Client Side**: On the client side, the RPC framework provides a stub, which the client application calls just like a local function.
2. **Network Communication**: The arguments to the function call are serialized and sent over the network to the server.
3. **Server Side**: The server has a corresponding stub that receives the request, unpacks the arguments, and calls the server's local function.
4. **Response**: The function on the server executes and sends the result back to the client, where it is deserialized and returned to the calling function as if it were a local call.

### RPC vs. REST API:

- **Protocol and Data Format**: RPC can use various underlying protocols (like HTTP, TCP, or named pipes) and data formats (like JSON, XML, or binary formats such as Protocol Buffers). REST, on the other hand, specifically uses HTTP as its underlying protocol and can support multiple media types (JSON, XML, etc.) for data exchange, but JSON is the most commonly used format.
- **Design Philosophy**: REST (Representational State Transfer) is an architectural style that is resource-oriented; it focuses on manipulating web resources using a predefined set of stateless operations (GET, POST, PUT, DELETE, etc.). RPC, however, is action-oriented; it focuses on executing procedures or commands on the server.
- **Idiomatic Use**: REST APIs are designed to be easily understood and used, leveraging standard HTTP methods in a way that's consistent with the protocol's original design intent. RPC APIs are more about directly calling remote services as if they were local functions, which can be more efficient but might abstract away some of the details of the HTTP protocol.
- **Use Cases**: REST is often chosen for public-facing APIs, particularly for web services that need to be easily accessible and understandable by a wide range of clients. RPC might be chosen for internal APIs, microservices, or situations where the efficiency of binary data formats and the direct nature of procedure calls are beneficial.

### gRPC

gRPC is a modern, open-source, high-performance Remote Procedure Call (RPC) framework that can run in any environment. It enables client and server applications to communicate transparently, and makes it easier to build connected systems. Developed by Google, it is part of the Cloud Native Computing Foundation (CNCF). gRPC is based on the HTTP/2 protocol, which allows for many advanced features such as bidirectional streaming, flow control, header compression, and multiplexing requests over a single connection.

Multiplexing - This technique allows multiple requests and responses to be sent back and forth simultaneously over a single TCP (Transmission Control Protocol) connection without waiting for each to complete sequentially.

---

### Project

For your project, which involves creating a client-server application using gRPC with both the server and client implemented in Python, here are comprehensive notes covering the setup, implementation, and testing phases. This guide assumes you have a basic understanding of Python and gRPC.

### Project Overview

- **Objective**: Create a gRPC application where the client sends a string to the server, and the server responds with the count of characters in the string.
- **Server**: A Python gRPC server that listens for requests containing strings and responds with the character count.
- **Client**: A Python Flask web application that allows users to input a string in a form. Upon form submission, it sends the string to the gRPC server and displays the character count received in the response.

### Environment Setup

1. **Install Python 3**: Ensure Python 3.6 or newer is installed on your system.
2. **Create Virtual Environments**: It's a good practice to create a virtual environment for Python projects to manage dependencies effectively.
   - For the server: `python3 -m venv server-env`
   - For the client: `python3 -m venv client-env`
3. **Activate the Virtual Environment**:
   - On Windows: `server-env\Scripts\activate` (for the server), `client-env\Scripts\activate` (for the client)
   - On Unix or MacOS: `source server-env/bin/activate` (for the server), `source client-env/bin/activate` (for the client)
4. **Install Dependencies**:
   - Install gRPC: `pip install grpcio grpcio-tools`
   - Install Flask for the client: `pip install Flask`

### Project Structure

- **Server**:
  - `protos/`: Directory containing `.proto` files with service definitions.
  - `server.py`: The gRPC server implementation.
- **Client**:
  - `client.py`: Flask application that serves the web form and communicates with the gRPC server.

### Implementation Steps

#### Define the gRPC Service

1. Create a `string_service.proto` file in the `protos/` directory with the following content:

```protobuf
syntax = "proto3";

package stringcounter;

service StringCounter {
  rpc CountCharacters(StringRequest) returns (CharacterCountResponse) {}
}

message StringRequest {
  string user_string = 1;
}

message CharacterCountResponse {
  int32 count = 1;
}
```

#### Generate Python gRPC Code

2. Generate the Python gRPC code from your `.proto` file:

```bash
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/string_service.proto
```

This command generates `string_service_pb2.py` and `string_service_pb2_grpc.py`.

#### Implement the gRPC Server

3. In `server.py`, implement the gRPC server:

```python
from concurrent import futures
import grpc
import string_service_pb2
import string_service_pb2_grpc

class StringCounterServicer(string_service_pb2_grpc.StringCounterServicer):
    def CountCharacters(self, request, context):
        return string_service_pb2.CharacterCountResponse(count=len(request.user_string))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    string_service_pb2_grpc.add_StringCounterServicer_to_server(StringCounterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
```

#### Implement the Flask Client

4. In `client.py`, create a Flask application that interacts with the gRPC server:

```python
from flask import Flask, request, render_template_string
import grpc
import string_service_pb2
import string_service_pb2_grpc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    count = None
    if request.method == 'POST':
        user_string = request.form.get('string', '')
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = string_service_pb2_grpc.StringCounterStub(channel)
            response = stub.CountCharacters(string_service_pb2.StringRequest(user_string=user_string))
            count = response.count
    return render_template_string('''
        <!doctype html>
        <html>
            <head><title>String Length Counter</title></head>
            <body>
                <h2>Enter a string to count its characters:</h2>
                <form method="POST">
                    <input type="text" name="string" />
                    <input type="submit" value="Count Characters" />
                </form>
                {% if count is not None %}
                    <h3>The string has {{ count }} characters.</h3>
                {% endif %}
            </body>
        </html>
    ''', count=count)

if __name__ == '__main__':
    app.run(debug=True)
```

### Testing the Application

- **Start the gRPC Server**: Run `python server.py` to start the gRPC server.
- **Run the Flask Client**: In a new terminal, activate the client's virtual environment and run `python client.py` to start the Flask application.
- **Access the Client**: Open a web browser and go to `http://localhost:5000`. Enter a string in the form and submit it to see the character count returned by the gRPC server.

### Conclusion

This project demonstrates a basic client-server application using gRPC in Python, with a Flask web client for user interaction. It covers setting up the environment, defining gRPC services, implementing the server and client, and testing the application.