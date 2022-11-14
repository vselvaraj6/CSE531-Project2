import grpc
from concurrent import futures
import service_pb2_grpc
import service_pb2
import time

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
       return "id: {0}, balance: {1}, branches: {2}, clock: {3}, data: {4}".format(self.id,self.balance,self.branches,self.clock,self.data)     

    def propogate_withdraw(self, event_id):

        for process in self.branches:
            host = 'localhost:'+str(process)
            with grpc.insecure_channel(host) as channel:
                self.stub = service_pb2_grpc.BranchStub(channel)
                request = service_pb2.WithdrawPropogateRequest(balance=self.balance,id=event_id)
                response = self.stub.WithdrawPropogate(request=request)
            channel.close()     

    def propogate_deposit(self, event_id):

      for process in self.branches:
          host = 'localhost:'+str(process)
          with grpc.insecure_channel(host) as channel:
              self.stub = service_pb2_grpc.BranchStub(channel)
              request = service_pb2.DepositPropogateRequest(balance=self.balance, id=event_id)
              response = self.stub.DepositPropogate(request=request)
          channel.close()             

    def event_request(self, event_id, event_name, remote_clock):
      self.clock = max(self.clock, remote_clock) + 1
      clock_event = service_pb2.ClockEvent()
      clock_event.id = event_id
      clock_event.name = event_name
      clock_event.clock = self.clock
      return clock_event

    def event_execute(self, event_id, event_name):
      self.clock = self.clock + 1  
      clock_event = service_pb2.ClockEvent()
      clock_event.id = event_id
      clock_event.name = event_name
      clock_event.clock = self.clock
      return clock_event

    def propogate_request(self, event_id, event_name, remote_clock):
      self.clock = max(self.clock, remote_clock) + 1  
      clock_event = service_pb2.ClockEvent()
      clock_event.id = event_id
      clock_event.name = event_name
      clock_event.clock = self.clock
      return clock_event

    def propogate_execute(self, event_id, event_name):
      self.clock = self.clock + 1
      clock_event = service_pb2.ClockEvent()
      clock_event.id = event_id
      clock_event.name = event_name
      clock_event.clock = self.clock
      return clock_event   

    def propogate_response(self, event_id, event_name, remote_clock):
      self.clock = max(self.clock, remote_clock) + 1 
      clock_event = service_pb2.ClockEvent()
      clock_event.id = event_id
      clock_event.name = event_name
      clock_event.clock = self.clock
      return clock_event

    def event_response(self, event_id, event_name):
      self.clock = self.clock + 1  
      clock_event = service_pb2.ClockEvent()
      clock_event.id = event_id
      clock_event.name = event_name
      clock_event.clock = self.clock
      return clock_event


    # TODO: students are expected to process requests from both Client and Branch
    def Withdraw(self, request, context):
        event = request.event
        output = service_pb2.WithdrawResponse()
        if event.interface == 2:
            output.clock_event.append(self.event_request(request.event.id, 'withdraw_request', request.clock))
            output.clock_event.append(self.event_execute(request.event.id, 'withdraw_execute'))
            output.id = self.id
            self.balance = self.balance - event.money
            output.result = 1
            output.interface = event.interface
            self.propogate_withdraw(request.event.id)
            output.clock_event.append(self.propogate_response(request.event.id, 'withdraw_propogate_response', self.clock))
        return output

    def Deposit(self, request, context):
        event = request.event
        output = service_pb2.DepositResponse()
        if event.interface == 1:
            output.clock_event.append(self.event_request(request.event.id, 'deposit_request', request.clock))
            output.clock_event.append(self.event_execute(request.event.id, 'deposit_execute'))
            output.id = self.id
            self.balance = self.balance + event.money
            output.result = 1
            output.interface = event.interface
            self.propogate_deposit(request.event.id)
            output.clock_event.append(self.propogate_response(request.event.id, 'deposit_propogate_response', self.clock))
        return output    

    def Query(self, request, context):
        output = service_pb2.QueryResponse()
        output.money = self.balance  
        output.id = self.id
        output.result = 1
        output.interface = 3
        return output

    def WithdrawPropogate(self, request, context):
        self.data.append(self.propogate_request(request.id, 'withdraw_propogate_request', request.clock))
        self.data.append(self.propogate_execute(request.id,'withdraw_propogate_execute'))
        self.balance = request.balance    
        output = service_pb2.WithdrawPropogateResponse()
        output.result = 1
        output.clock = self.clock
        return output

    def DepositPropogate(self, request, context):
        self.data.append(self.propogate_request(request.id, 'deposit_propogate_request', request.clock))
        self.data.append(self.propogate_execute(request.id,'deposit_propogate_execute'))
        self.balance = request.balance 
        output = service_pb2.DepositPropogateResponse()
        output.result = 1
        output.clock = self.clock
        return output