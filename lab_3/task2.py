import datetime


def input_train_data():
    N = 10

    trains = {}

    for i in range(N):
        print(f"Train {i + 1}: ")
        while True:
            train_number = input("   Train number: ").strip()
            if train_number:
                break
            else:
                print("   Error: The train number cannot be empty.")

        while True:
            destination = input("   Destination (for example, 'Kiev - Chernivtsi': ").strip()
            if destination:
                break
            else:
                print("   Error: Destination cannot be empty.")

        departure_time = input_time("   Departure time (in HH:MM format): ")
        arrival_time = input_time("   Arrival time (in HH:MM format): ")

        if arrival_time < departure_time:
            print("   Error: The departure time must be later than the arrival time. Please enter "
                  "the train data again.\n")
            continue

        trains[train_number] = {
            "destination": destination,
            "departure_time": departure_time,
            "arrival_time": arrival_time
        }
        print()

    return trains


def input_time(prompt):
    while True:
        time_input = input(prompt).strip()
        try:
            time_obj = datetime.datetime.strptime(time_input, "%H:%M").time()
            return time_obj
        except ValueError:
            print("   Error: Enter the time in the correct HH:MM format (for example, 09:30).")


def find_trains_at_time(trains, check_time):
    trains_at_station = []

    for train_number, info in trains.items():
        if info["departure_time"] <= check_time < info["arrival_time"]:
            trains_at_station.append({
                "number": train_number,
                "destination": info["destination"],
                "departure_time": info["departure_time"],
                "arrival_time": info["arrival_time"]
            })

    return trains_at_station


def print_trains(trains):
    if not trains:
        print("There are no trains at the station at the specified time.")
    else:
        print(f"\nTrains at the station at the specified time ({check_time.strftime('%H:%M')}): ")
        for train in trains:
            print(f"  Train number: {train['number']}")
            print(f"  Destination: {train['destination']}")
            print(f"  Departure time: {train['departure_time'].strftime('%H:%M')}")
            print(f"  Arrival time: {train['arrival_time'].strftime('%H:%M')}\n")


if __name__ == "__main__":
    trains_schedule = input_train_data()

    print("Enter the time for which you want to find trains at the station: ")
    check_time = input_time("   Time (HH:MM format): ")

    trains_at_station = find_trains_at_time(trains_schedule, check_time)

    print_trains(trains_at_station)
