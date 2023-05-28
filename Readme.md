# Python gRPC implementation example

This repository contains an example gRPC service implemented in Python. It includes a server and a client that communicate using Protocol Buffers.

## Prerequisites

- Python 3.x
- `grpcio` and `grpcio-tools` packages (can be installed via pip)

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/royyanwibisono/grpcexample.git
```

2. Install the required packages:
```bash
   pip install grpcio grpcio-tools
```

## Usage

1. Start the server by running server.py:

```bash
  python server.py
```
The server will start listening on port 50051.

2. In another terminal window, run the client script client.py:
```bash
  python client.py
```
The client script will connect to the server and send requests to it. You should see the server's responses printed in the terminal.

## Customization

- Modify the example.proto file to define your own gRPC service and message types. Once modified, regenerate the Python code using the following command:
```bash
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. example.proto
```

## License
This project is licensed under the MIT License.