# BankingSystem

This project is to implement distributed banking system - where customer is allowed to perform desposit, withdraw and query operations in a branch. A customer can access only one specific branch, however, the balance is propagated to all the other branches. This project implements gRPC APIs to perform communications between customer-and-branch, branch-and-branch.

## Technologies used
- Python 3.10.X
- gRPC
- Protobuf
- grpcio-tools
- Linux - Ubuntu 22.04

The message types and services are defined in `/proto/service.proto`. The client stub for gRPC is auto-generated using grpcio-tools by running the following command

To generate grpc server and client stub files:
```
python3 -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/service.proto
```

## Project Execution

To run server and spin up branch processes, open a terminal and run the following command. You need to pass `input.json` as an argument to `server.py`:
```bash
python3 server.py input.json
```

To run client and execute events, open a new terminal and run the following command.  You need to pass `input.json` as an argument to `server.py`::
```bash
python3 client.py input.json
```
You, will see a few print statements in the terminal for logging purposes. The final output is saved in `output.txt` file in the current directory
