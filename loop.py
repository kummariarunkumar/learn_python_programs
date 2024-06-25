  
#Assume that there are 5 passengers and each of them have 2 baggages. The below code will make sure that all baggages of each passenger have undergone the security check.
number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    for baggage_count in range(1,number_of_baggage+1):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")

#The same code in the inner loop can also be written using the while loop instead of the for loop as shown below
number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    baggage_count =1
    while (baggage_count<=number_of_baggage):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")
        baggage_count+=1
