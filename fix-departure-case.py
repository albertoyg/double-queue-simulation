'''
DO NOT TOUCH THIS CODE!!
Owner : Hritik Jaiswal
Topic : To simulate a Single Server Queuing System (One-operator Barbershop problem) using Python
Subject : Modeling and simulation
'''

import random 

def generateCustomerType():
    customer_type = []
    size = 15
    time_between_arrivals = []
    for i in range(size+1):
        randValue = random.randrange(0,10)
        if randValue <= 3:
           customer_type.append('Business')
           time_between_arrivals.append(4)
        else:
            customer_type.append('Economy') 
            time_between_arrivals.append(2)
    return customer_type, time_between_arrivals


# constant service time
serviceTime = 3

# to keep track of customer numbers
cusNo = 1

# list of future events 
nextEvent = []
trash = []
# list of past events: for output
completedEvents = []

# time counter/tracker
time = 0

# server status 
server_busy = False

# length of queues
econQueue = []
busQueue = []

generalQueue = 0

queue = 0

# initialize customer types
customer_type, time_between_arrivals = generateCustomerType()
# customer_type = ['Business','Economy','Economy','Economy','Economy','Business','Business','Economy','Economy','Economy','Economy','Economy','Economy']


# first event:
curEvent = {
        'cusType': customer_type[0], 
        'cusNo': cusNo,
        'eventType': 'arrival',
        'eventTime': 0
        }

# dequeue from customer list
customer_type.pop(0)

# add first event to nextEvent
nextEvent.append(curEvent)

kill = False
# while curEvent['cusNo'] != 11:
# start loop
# while len(customer_type) >= 0:
while len(completedEvents) < 20:
    # receive event
    # if curEvent['cusNo'] == 11:
    #         kill = True 
    # else:
        curEvent = nextEvent.pop(0)

        # if event type is arrival
        if curEvent['eventType'] == 'arrival':

            # generate next arrival time
            if curEvent['cusType'] == 'Business':
                nextArrivalTime = 4 + curEvent['eventTime']
                
            else:
                nextArrivalTime = 2 + curEvent['eventTime']

            # is the service desk busy?
            if server_busy == False: # service desk is not busy

                # generate departure time: 
                departureTime = serviceTime + curEvent['eventTime']

                # generate a departure event for same customer
                departEvent = {
                                'cusType': curEvent['cusType'], 
                                'cusNo': curEvent['cusNo'],
                                'eventType': 'departure',
                                'eventTime':  departureTime,
                                }
                # add event to event list
                nextEvent.append(departEvent)

                # generate next arrival event for next customer
                arrivalEvent = {
                                'cusType': customer_type[0], 
                                'cusNo': curEvent['cusNo']+1,
                                'eventType': 'arrival',
                                'eventTime':  nextArrivalTime,
                                }
                customer_type.pop(0)
                # add event to event list
                if arrivalEvent['cusNo'] == 11:
                    trash.append(arrivalEvent)
                else:
                    nextEvent.append(arrivalEvent)

                # sort events by time
                nextEvent = sorted(nextEvent, key=lambda d: (d['eventTime'],d['cusType']))

                # add finished event to completed list
                completedEvents.append(curEvent)

            else: # service desk is busy
                # if customer type = business
                if curEvent['cusType'] == 'Business':
                    # business queue append event
                    busQueue.append(curEvent)        
                else:
                    # econ queue apend event 
                    econQueue.append(curEvent)
                # generate next arrival event 
                # add event to event list
                # sort events by time 
                arrivalEvent = {
                                'cusType': customer_type[0], 
                                'cusNo': curEvent['cusNo']+1,
                                'eventType': 'arrival',
                                'eventTime':  nextArrivalTime,
                                }
                customer_type.pop(0)

                if arrivalEvent['cusNo'] == 11:
                    trash.append(arrivalEvent)
                else:
                    nextEvent.append(arrivalEvent)

                nextEvent = sorted(nextEvent, key=lambda d: (d['eventTime'],d['cusType']))

                completedEvents.append(curEvent) # event shouldnt be processed 

            if nextArrivalTime < departureTime:    # might need to change
                server_busy = True
            else:
                server_busy = False

    
                

        # if event is departure
        else:

            # is the business queue empty?
            
            if len(busQueue) == 0:
            # yes
                # is the econ queue empty?
                if len(econQueue) == 0:
                     # yes
                    server_busy = False
                                            # service desk is not busy
                                            # idle time starts
                else:
                # no
                    server_busy = True
                    queuedEvent = econQueue.pop(0) 
                    departureTime = serviceTime + curEvent['eventTime']
                    departEvent = {
                                'cusType': queuedEvent['cusType'], # fix this <-- need to get right customer type
                                'cusNo': queuedEvent['cusNo'], 
                                'eventType': 'departure',
                                'eventTime':  departureTime,
                                }
                    
                    nextEvent.append(departEvent)
                    nextEvent = sorted(nextEvent, key=lambda d: (d['eventTime'],d['cusType']))
                                            # dequeue for econ
                                            # NEXTEVENT = econ queue pop
                                            # departure time = curevent[time] + service time
                                            # departEvent = NEXTEVENT cusnom, type, dt, depart
                                            # create departure time for econ customer
             
            else:
            # no                    queuedEvent = econQueue.pop(0) 
                server_busy = True
                queuedEvent = busQueue.pop(0) 
                departureTime = serviceTime + curEvent['eventTime']
                departEvent = {
                            'cusType': queuedEvent['cusType'], # fix this <-- need to get right customer type
                            'cusNo': queuedEvent['cusNo'], 
                            'eventType': 'departure',
                            'eventTime':  departureTime,
                            }
                    
                nextEvent.append(departEvent)
                nextEvent = sorted(nextEvent, key=lambda d:(d['eventTime'],d['cusType']))
                            # dequeue from business
                            # create departure time for business customer
            completedEvents.append(curEvent)

        # event is done and we set the service desk status accordingly 

        




customers = [1,2,3,4,5,6,7,8,9,10] # good
service_Times = [3,3,3,3,3,3,3,3,3,3] # good


arrivaltimes = [] # good
customer_type = [] # good
int_Arrivals = [] # good
timeServiceBegins = []
timeServiceEnds = []

# time customer in queue  time service begins - arrival
tsiq = []
# time in system (time departed - time arrived)
# system idle 

for i in range(1,11):
    for curEvent in completedEvents:
        if curEvent['cusNo'] == i:
            if curEvent['eventType'] == 'arrival':
         # get customer type
                customer_type.append(curEvent['cusType'])
    #     # get event arrival time
                arrivaltimes.append(curEvent['eventTime'])
    #     # get int arrival time
            
         
            if curEvent['eventType'] == 'departure':
                # get time service begins 
                timeServiceBegins.append(curEvent['eventTime']-3)
                # get time service ends
                timeServiceEnds.append(curEvent['eventTime'])

for cust in customer_type:
    if cust == 'Business':
        int_Arrivals.append('4')
    else:
        int_Arrivals.append('2')
            
for i in range(10):
    tsiq.append(timeServiceBegins[i]-arrivaltimes[i])


print(customers)
print(arrivaltimes)
print(customer_type)
print(int_Arrivals)
print(timeServiceBegins)
print(timeServiceEnds)
print(tsiq)


for event in completedEvents:
    print(event)

'''
    # generate next event
    event = {'cusType': customer_type[0], 'eventType': 'arrival', 'arrivalTime': 0}
    # dequeue from customer list
    customer_type.pop(0)

    # add event to nextEvent
    nextEvent.append(event)
    
    # add finished event to completed list
    completedEvents.append(curEvent)
'''






"""

# Seed 
random.seed(10)

# No. of Customer
size = 10

# Series of customer
customer = [i for i in range(1,size+1)]

customer_type, time_between_arrivals = generateCustomerType()

# Inter Arrival Time 

# Service Time
service_time = [3 for i in range(size)]

print(len(service_time))

# Calculate arrival time
arrival_time = [0 for i in range(size)]

# initial
arrival_time[0] = 0

for i in range(1,size):
#   arrival_time[i] = inter_arrival_time[i]+arrival_time[i-1]
    arrival_time[i] = time_between_arrivals[i-1]+arrival_time[i-1]
 

Time_Service_Begin = [0 for i in range(size)]
Time_Customer_Waiting_in_Queue = [0 for i in range(size)]
Time_Service_Ends = [0 for i in range(size)]
Time_Customer_Spend_in_System = [0 for i in range(size)]
System_ideal = [0 for i in range(size)]

Time_Service_Begin[0] = arrival_time[0]
Time_Service_Ends[0] = Time_Service_Begin[0] + service_time[0]
Time_Customer_Spend_in_System[0] = service_time[0]



for i in range(1,size):
  # Time Service Begin 
  Time_Service_Begin[i] = max(arrival_time[i],Time_Service_Ends[i-1])

  # Time customer waiting in queue   
  Time_Customer_Waiting_in_Queue[i] = Time_Service_Begin[i]-arrival_time[i]

  # Time service ends
  Time_Service_Ends[i] = Time_Service_Begin[i] + service_time[i]  

  # Time Customer Spend in the system
  Time_Customer_Spend_in_System[i] = Time_Service_Ends[i] - arrival_time[i]

  # Time when system remains ideal
  if (arrival_time[i]>Time_Service_Ends[i-1]):
    System_ideal[i] = arrival_time[i]-Time_Service_Ends[i-1]
  else:
    System_ideal[i] = 0 
    

from prettytable import PrettyTable

x = PrettyTable()

column_names = ['Customer','AT','ST','TSB','TCWQ','TSE','TCSS','System Ideal','type','arrivals']
data = [customer,arrival_time,service_time, Time_Service_Begin, Time_Customer_Waiting_in_Queue, Time_Service_Ends, Time_Customer_Spend_in_System, System_ideal, customer_type, time_between_arrivals]

length = len(column_names)

for i in range(length):
  x.add_column(column_names[i],data[i])
  
print(x)

'''
Performance measure 

Average waiting time = Total time customer wait in queue (minutes) / total number of customers 
 
Probability of customer (Wait) = Number of customer who wait / total number of customer 
 
Probability of Idle server =  Total Idle time of  server /  total  runtime of simulation
 
Average time between arrival = sum of all time times between arrival / number of arrivals -1 
 
Average waiting time those who wait = total time customers wait in the queue / total no. of customer who wait 
 
Average time customer spent in the system  = total time customers customer spent in the system / total no. of customer 
'''

# Average waiting time 
Average_waiting_time = sum(Time_Customer_Waiting_in_Queue)/size 

# Probability of customer were waiting
no_customer_who_are_waiting = len(list(filter(lambda x:x>0,Time_Customer_Waiting_in_Queue)))

prob_customer_waiting = no_customer_who_are_waiting / size

# Average service time
Average_service_time = sum(service_time)/size

# Probability of idle server
prob_ideal_server = sum(System_ideal) / Time_Service_Ends[size-1]  

# Average time between arrival
Average_Time_Between_Arrival = arrival_time[size-1] / (len(arrival_time) - 1)

# Average waiting time those who wait
average_waiting_time = sum(Time_Customer_Waiting_in_Queue) / no_customer_who_are_waiting

# Average time customer spent in the system 
time_customer_spent = sum(Time_Customer_Spend_in_System)/size

print("Average waiting time : {:.2f}".format(Average_waiting_time))
print('-'*50)

print("Probability of customer were waiting : {:.2f}".format(prob_customer_waiting))
print('-'*50)

print("Average service time : {:.2f}".format(Average_service_time))

print('-'*50)

print("Probability of idle server : {:.2f}".format(prob_ideal_server))

print('-'*50)

print("Average Time Between Arrival : {:.2f}".format(Average_Time_Between_Arrival))
print('-'*50)

print("Average waiting time those who wait : {:.2f}".format(average_waiting_time))
print('-'*50)

print("Average time customer spent in the system : {:.2f}".format(time_customer_spent))

"""