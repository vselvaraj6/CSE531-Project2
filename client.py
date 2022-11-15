import json
import sys
import time
from customer import Customer
from pid_data import PIdData
from eventid_data import EventIdData
from multiprocessing import Process


def parse_input_file():
    customer_input_items = list()
    try:
        with open(input_file, 'r') as f:
            input_items = json.load(f)    

            for input_item in input_items:
                if('customer' == input_item.get('type')):
                    customer_input_items.append(input_item)           
    except:
        print("Invalid format. Please check the content of input.json file") 
    return customer_input_items                   


if len(sys.argv) < 2:
    print("Missing input file. Pass input.json file as argument!")
    exit()

input_file = sys.argv[1]
customer_input_items = parse_input_file()

customers = []
customer_processes = []

for customer_input_item in customer_input_items:
    customer = Customer(customer_input_item.get('id'),customer_input_item.get('events'), 1)
    customers.append(customer)

#Invoke withdraw and deposit interface
for customer in customers:
    for event in customer.events:
        if event.get('interface') == 'deposit':
            # print("---customer events deposit ---", customer.events)
            customer_process = Process(target=customer.executeDepositEvents(),)
            customer_processes.append(customer_process)
            customer_process.start()

        elif event.get('interface') == 'withdraw':
            # print("---customer events withdraw ---", customer.events)
            customer_process = Process(target=customer.executeWithdrawEvents(),)
            customer_processes.append(customer_process)
            customer_process.start()    

# sleep for 3 seconds before querying
time.sleep(3)

# Invoke query interface
for customer in customers:
    for event in customer.events:
        if event.get('interface') == 'query':
            # print("---customer events for query ---", customer.events)
            customer_process = Process(target=customer.executeQueryEvents(),)
            customer_processes.append(customer_process)
            customer_process.start()

for customer_process in customer_processes:
    customer_process.join()    

# print("Final_Response")

eventid_dict = dict()
pid_dict = dict()

for customer in customers:
    #print("{ 'id': ", customer.id, "'recv:'", customer.recvMsg, "}")
    #print(customer.data)
    if len(customer.data):
        for data in customer.data:
            for clock in data:
                if pid_dict.keys().__contains__(clock.id):
                    value = pid_dict[clock.id]
                    value.extend([PIdData(clock.event_id, clock.name, clock.clock)])
                else:
                    pid_dict[clock.id] = [PIdData(clock.event_id, clock.name, clock.clock)]

                if eventid_dict.keys().__contains__(clock.event_id):
                    value = eventid_dict[clock.event_id]    
                    value.extend([EventIdData(clock.clock, clock.name)])
                else:
                    eventid_dict[clock.event_id] = [EventIdData(clock.clock, clock.name)]


pid_dict_str = [{'pid': key, 'data': str(pid_dict[key])} for key in pid_dict]
eventid_dict_str = [{'eventid': key, 'data': str(eventid_dict[key])} for key in eventid_dict]

print(json.dumps(pid_dict_str, indent=2), flush=True)
print(json.dumps(eventid_dict_str, indent=2), flush=True)

with open('output.txt', 'w') as f:
    for customer in customers:
        f.writelines(repr(customer))