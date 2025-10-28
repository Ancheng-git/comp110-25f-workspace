def get_weather_report() -> None:
    weather = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    else:
        if weather == "hot":
            print("Keep cool out there!")
        else:
            print("I don't recognize this weather.")


if __name__ == "__main__":
    get_weather_report()


def get_orders(dictionary: dict[str, int]) -> None:
    for i in dictionary:
        print(i + " has " + str(dictionary[i]) + " orders.")
