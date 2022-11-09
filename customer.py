import grpc
import time
import service_pb2_grpc
import service_pb2
import json
import sys

class Customer:
    def __init__(self, id, events, clock):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = None
        # local clock
        self.clock = clock
        # data
        self.data = list()

    def __str__(self) -> str:
        return "id: {0}, recv:{1}".format(self.id,self.recvMsg)  

    def __repr__(self):
        return str(self)     

    # TODO: students are expected to create the Customer stub
    def createStub(self):
       pass

    # TODO: students are expected to send out the events to the Bank
    def executeWithdrawEvents(self):
        port = 50050 + self.id
        host = 'localhost:'+str(port)
        print('Creating customer stub to connect to branch on ', host)
        
        for event in self.events:
            if event.get('interface') == 'withdraw':
                request = service_pb2.WithdrawRequest(id=self.id, clock=self.clock+1, event=event)
                with grpc.insecure_channel(host) as channel:
                    self.stub = service_pb2_grpc.BranchStub(channel)
                    response = self.stub.Withdraw(request=request)
                    self.recvMsg.append(response)
                    print('Local Clock in Withdraw:', self.clock)
                    print('Recieved WithdrawResponse: ', self.recvMsg)
                channel.close()   

    def executeDepositEvents(self):
        port = 50050 + self.id
        host = 'localhost:'+str(port)
        print('Creating customer stub to connect to branch on ', host)
        
        for event in self.events:
            if event.get('interface') == 'deposit':
                request = service_pb2.DepositRequest(id=self.id, clock=self.clock, event=event)
                with grpc.insecure_channel(host) as channel:
                    self.stub = service_pb2_grpc.BranchStub(channel)
                    response = self.stub.Deposit(request=request)
                    self.recvMsg.append(response)
                    self.clock = self.clock + 1
                    print('Local Clock in Deposit:', self.clock)
                    print('Recieved DepositResponse: ', self.recvMsg)
                channel.close()                                

    def executeQueryEvents(self):
        port = 50050 + self.id
        host = 'localhost:'+str(port)
        print('Creating customer stub to connect to branch on ', host)
        
        for event in self.events:
            if event.get('interface') == 'query':
                request = service_pb2.QueryRequest(id=self.id, clock=self.clock, event=event)
                with grpc.insecure_channel(host) as channel:
                    self.stub = service_pb2_grpc.BranchStub(channel)
                    response = self.stub.Query(request=request)
                    self.recvMsg.append(response)
                    self.clock = self.clock + 1
                    print('Local Clock in Query:', self.clock)
                    print('Recieved QueryResponse:', self.recvMsg)
                channel.close()                    

  