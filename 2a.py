slots = {
    1: "Car",
    2: "Bike",
    3: "Car",
    4: "EV",
    5: "Bike",
    6: "EV"
}

parked = {}

n = int(input("Enter number of vehicles: "))

for i in range(n):
    vehicle = input("\nEnter vehicle type (Car/Bike/EV): ").capitalize()
    allocated = False

    for slot, slot_type in slots.items():
        if slot_type == vehicle and slot not in parked:
            parked[slot] = vehicle
            print("Slot allocated:", slot)
            allocated = True
            break

    if not allocated:
        print("No suitable parking slot available!")

print("\nParking Status:")
for slot, slot_type in slots.items():
    if slot in parked:
        print("Slot", slot, ":", parked[slot], "- Occupied")
    else:
        print("Slot", slot, ":", slot_type, "- Available")