'''
DO NOT TOUCH THIS CODE!!
Owner : Hritik Jaiswal
Topic : To simulate a Single Server Queuing System (One-operator Barbershop problem) using Python
Subject : Modeling and simulation
'''
from prettytable import PrettyTable
import random 


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
# customer_type, time_between_arrivals = generateCustomerType()
# customer_type = ['Business','Economy','Economy','Economy','Economy','Business','Business','Economy','Economy','Economy','Economy','Economy','Economy']
random.seed(10)
customer_type = (random.choices(["Business", "Economy"], weights=[0.6, 0.4], k=15))


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

            if nextArrivalTime <= departureTime:    # might need to change
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

   
        
customers = [1,2,3,4,5,6,7,8,9,10] # good
service_Times = [3,3,3,3,3,3,3,3,3,3] # good
int_Arrivals = [0]

arrivaltimes = [] # good
customer_type = [] # good
# int_Arrivals = [] # fix: need to change to since last 
timeServiceBegins = []
timeServiceEnds = []

# time customer in queue  time service begins - arrival
tsiq = []
# time in system (time departed - time arrived)
tis = []
# system idle 
idle = []

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

for i in range(10):
    if customer_type[i] == 'Business':
        int_Arrivals.append(4)
    else:
        int_Arrivals.append(2)

int_Arrivals.pop(-1)
            
for i in range(10):
    tsiq.append(timeServiceBegins[i]-arrivaltimes[i])
    tis.append(timeServiceEnds[i]-arrivaltimes[i])

arrivaltimes.append(0)

timeServiceBeginsSorted = sorted(timeServiceBegins)
timeServiceEndsSorted = sorted(timeServiceEnds)
timeServiceBeginsSorted.append(timeServiceEndsSorted[-1])

idle.append(0)

for i in range(10):
    if timeServiceEndsSorted[i]<timeServiceBeginsSorted[i+1]:
        idle.append(timeServiceBeginsSorted[i+1]-timeServiceEnds[i])
    else:
        idle.append(0)

arrivaltimes.pop(-1)
idle.pop(-1)


x = PrettyTable()

column_names = ['Customer','IAT','AT','ST','TSB','TCWQ','TSE','TCSS','System Ideal','type']
data = [customers,int_Arrivals,arrivaltimes,service_Times, timeServiceBegins, tsiq, timeServiceEnds, tis, idle, customer_type]

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
Average_waiting_time = sum(tsiq)/10 

# Probability of customer were waiting
no_customer_who_are_waiting = len(list(filter(lambda x:x>0,tsiq)))

prob_customer_waiting = no_customer_who_are_waiting / 10

# Average service time
Average_service_time = sum(service_Times)/10

# Probability of idle server
prob_ideal_server = sum(idle) / timeServiceEnds[10-1]  

# Average time between arrival
Average_Time_Between_Arrival = arrivaltimes[10-1] / (len(arrivaltimes) - 1)

# Average waiting time those who wait
average_waiting_time = sum(tsiq) / no_customer_who_are_waiting

# Average time customer spent in the system 
time_customer_spent = sum(tis)/10

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


