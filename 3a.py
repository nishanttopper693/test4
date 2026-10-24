def traffic_signal(density, waiting):
    if density > 70 or waiting > 60:
        green = 60
    elif density > 40 or waiting > 30:
        green = 40
    else:
        green = 20

    print("Traffic Density:", density, "%")
    print("Waiting Time:", waiting, "seconds")
    print("Green Signal Time:", green, "seconds")

    if green == 60:
        print("Traffic Status: Heavy")
    elif green == 40:
        print("Traffic Status: Moderate")
    else:
        print("Traffic Status: Light")


density = int(input("Enter traffic density (0-100): "))
waiting = int(input("Enter waiting time (seconds): "))

if 0 <= density <= 100 and waiting >= 0:
    traffic_signal(density, waiting)
else:
    print("Invalid input!")