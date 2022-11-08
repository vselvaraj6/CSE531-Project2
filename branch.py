import grpc
from concurrent import futures
import service_pb2_grpc
import service_pb2
import time

class BranchServicer(service_pb2_grpc.BranchServicer):

    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # stores local clock
        self.clock = None
        # stores output data
        self.data = list()

    def __str__(self) -> str:
       return "id: {0}, balance: {1}, branches: {2}".format(self.id,self.balance,self.branches)     

    def propogate_withdraw(self):

        for process in self.branches:
            host = 'localhost:'+str(process)
          #  print('Creating branch stub to connect to ', host)
            with grpc.insecure_channel(host) as channel:
                self.stub = service_pb2_grpc.BranchStub(channel)
                request = service_pb2.WithdrawPropogateRequest(balance=self.balance)
                response = self.stub.WithdrawPropogate(request=request)
            channel.close()     

    def propogate_deposit(self):

      for process in self.branches:
          host = 'localhost:'+str(process)
        #  print('Creating branch stub to connect to ', host)
          with grpc.insecure_channel(host) as channel:
              self.stub = service_pb2_grpc.BranchStub(channel)
              request = service_pb2.DepositPropogateRequest(balance=self.balance)
              response = self.stub.DepositPropogate(request=request)
          channel.close()             

    # TODO: students are expected to process requests from both Client and Branch
    def Withdraw(self,request, context):
       
        event = request.event
        output = service_pb2.WithdrawResponse()
        if event.interface == 2:
            print("executing event..", request.event)
            output.id = self.id
            self.balance = self.balance - event.money
            output.result = 1
            output.interface = event.interface
          #  print("withdraw - customer id: ", self.id, "balance: ", self.balance)
            print("Response from server WithdrawResponse:", output)
            self.propogate_withdraw()
        return output

    def Deposit(self,request, context):
       
        event = request.event
        output = service_pb2.DepositResponse()
        if event.interface == 1:
            print("executing event..", request.event)
            output.id = self.id
            self.balance = self.balance + event.money
            output.result = 1
            output.interface = event.interface
         #   print("deposit - customer id: ", self.id, "balance: ", self.balance)
            print("Response from server DepositResponse:", output)
            self.propogate_deposit()
        return output    

    def Query(self, request, context):
        print("executing interface..", request.event)
        output = service_pb2.QueryResponse()
        output.money = self.balance  
       # print("query - customer id: ", self.id, "balance: ", self.balance)
        output.id = self.id
        output.result = 1
        output.interface = 3
        print("Response from server Query:", output)
        return output

    def WithdrawPropogate(self, request, context):
        self.balance = request.balance 
      #  print("propogate balance to branch id: ", self.id , "successful!")   
        output = service_pb2.WithdrawPropogateResponse()
        output.result = 1
      #  print("Response from server PropogateBalance:", output)
        return output   

    def DepositPropogate(self, request, context):
        self.balance = request.balance 
      #  print("propogate balance to branch id: ", self.id , "successful!")   
        output = service_pb2.DepositPropogateResponse()
        output.result = 1
      #  print("Response from server PropogateBalance:", output)
        return output       
