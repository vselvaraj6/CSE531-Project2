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
        if event.get('interface') == 'deposit' or event.get('interface') == 'withdraw':
            customer_process = Process(target=customer.executeUpdateEvents(),)        
            customer_processes.append(customer_process)
            customer_process.start()    

# sleep for 3 seconds before querying
time.sleep(3)

# Invoke query interface
for customer in customers:
    for event in customer.events:
        if event.get('interface') == 'query':
            customer_process = Process(target=customer.executeQueryEvents(),)
            customer_processes.append(customer_process)
            customer_process.start()

for customer_process in customer_processes:
    customer_process.join()    

events_list = list()
pid_dict = dict()

for customer in customers:
    #print("{ 'id': ", customer.id, "'recv:'", customer.recvMsg, "}")
    print(customer.data)
    # if len(customer.data):
    #     for data in customer.data:
    #         for clock in data:
    #             if pid_dict.keys().__contains__(clock.id):
    #                 value = pid_dict[clock.id]
    #                 value.extend([PIdData(clock.event_id, clock.name, clock.clock)])
    #             else:
    #                 pid_dict[clock.id] = [PIdData(clock.event_id, clock.name, clock.clock)]

#print('pid_dict', pid_dict)

with open('output.txt', 'w') as f:
    for customer in customers:
        f.writelines(repr(customer))