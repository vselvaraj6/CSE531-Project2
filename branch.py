import grpc
from concurrent import futures
import service_pb2_grpc
import service_pb2
import time
from clock_data import ClockData

class BranchServicer(service_pb2_grpc.BranchServicer):

    def __init__(self, id, balance, branches, clock):
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
        self.clock = clock
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

    def event_request(self, event_id, event_name, remote_clock):
      self.clock = max(self.clock, remote_clock) + 1
      return ClockData(event_id, event_name, self.clock)

    def event_execute(self, event_id, event_name):
      self.clock = self.clock + 1  
      return ClockData(event_id, event_name, self.clock)

    def propogate_request(self, event_id, event_name, remote_clock):
      self.clock = max(self.clock, remote_clock) + 1  
      return ClockData(event_id, event_name, self.clock)

    def propogate_execute(self, event_id, event_name):
      self.clock = self.clock + 1
      return ClockData(event_id, event_name, self.clock)   

    def propogate_response(self, event_id, event_name, remote_clock):
      self.clock = max(self.clock, remote_clock) + 1 
      return ClockData(event_id, event_name, self.clock)

    def event_response(self, event_id, event_name):
      self.clock = self.clock + 1  
      return ClockData(event_id, event_name, self.clock)


    # TODO: students are expected to process requests from both Client and Branch
    def Withdraw(self, request, context):
        event = request.event
        output = service_pb2.WithdrawResponse()
        if event.interface == 2:
            self.data.append(self.event_request(request.event.id, 'withdraw_request', request.clock))
            self.data.append(self.event_execute(request.event.id, 'withdraw_execute'))
            print("executing event..", request.event)
            output.id = self.id
            self.balance = self.balance - event.money
            output.result = 1
            output.interface = event.interface
          #  print("withdraw - customer id: ", self.id, "balance: ", self.balance)
            print("Response from server WithdrawResponse:", output)
            print('Local Clock in WithdrawServer:', self.clock)
            self.propogate_withdraw()
            self.data.append(self.propogate_response(request.event.id, 'withdraw_propogate_response', self.clock))
            print(self.data)
        return output

    def Deposit(self, request, context):
        event = request.event
        output = service_pb2.DepositResponse()
        if event.interface == 1:
            self.data.append(self.event_request(request.event.id, 'deposit_request', request.clock))
            self.data.append(self.event_execute(request.event.id, 'deposit_execute'))
            print("executing event..", request.event)
            output.id = self.id
            self.balance = self.balance + event.money
            output.result = 1
            output.interface = event.interface
         #   print("deposit - customer id: ", self.id, "balance: ", self.balance)
            print("Response from server DepositResponse:", output)
            print('Local Clock in DepositServer:', self.clock)
            self.propogate_deposit()
            self.data.append(self.propogate_response(request.event.id, 'deposit_propogate_response', self.clock))
            print(self.data)
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
      #  self.data.append(self.propogate_request(request.clock))
      #  self.propogate_execute()
        self.balance = request.balance 
      #  print("propogate balance to branch id: ", self.id , "successful!")   
        output = service_pb2.WithdrawPropogateResponse()
        output.result = 1
        output.clock = self.clock
      #  print("Response from server PropogateBalance:", output)
        return output   

    def DepositPropogate(self, request, context):
     #   self.propogate_request(request.clock)
     #   self.propogate_execute()
        self.balance = request.balance 
      #  print("propogate balance to branch id: ", self.id , "successful!")   
        output = service_pb2.DepositPropogateResponse()
        output.result = 1
        output.clock = self.clock
      #  print("Response from server PropogateBalance:", output)
        return output       