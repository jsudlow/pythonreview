def run():
    total = 0
    car_range = 0
    getting_cities = True
    further_cities = ""
    City = ""
    cities = []
    distance = []
    #print('running')
    while getting_cities:
        city = input("City: ")
        if city == "done":
            
            getting_cities = False
        else: 
            cities.append(city)
        if getting_cities == True:
            miles = input("Miles: ")
            total = total + int(miles)
            distance.append(int(miles))
    #print('about to calculate')
    #print(cities)
    #print(distance)
    #print(total)
    car_range = int(input("Range: "))
    #print("range: ", car_range)

    #check if we can make it to the first stop
    if car_range < distance[0]:
        print("You cannot make it to the first stop.")
        return
    #check if we can make the whole trip
    if car_range >= total:
        print("You can make it all the way to your destination.")
        return

    #now we must be able to make it to some stop along the way

    #lets keep track of the raw distance as the trip progresses
    distance_accumulator = 0
    
    #we need to keep track of the number of times thru the for loop to take advantage
    #of the parrallel arrays
    step_counter = 0
    for i in distance:
        distance_accumulator += i
        if distance_accumulator > car_range:
            print("You can make it to ", cities[step_counter - 1], " before recharging.")
            break
        step_counter += 1

  
if __name__ == "__main__":
    run()