#Group member: Qianyi, Zixuan, Chengyi, Tommy
#Date: Mar. 19, 2024
#Purpose: Create a program about the sky

def main():
    season, time_hour, weather = inp()
    if season == "spring":
        if time_hour >= 19 or time_hour <= 7:
            if weather == "sunny":
                yes()
            else:
                no_weather()
        else:
            no_time()
    elif season == "summer":
        if time_hour >= 20 or time_hour <= 5:
            if weather == "sunny":
                yes()
            else:
                no_weather()
        else:
            no_time()
    elif season == "autumn" or season == "fall":
        if time_hour >= 19 or time_hour <= 7:
            if weather == "sunny":
                yes()
            else:
                no_weather()
        else:
            no_time()
    elif season == "winter":
        if time_hour >= 17 or time_hour <= 8:
            if weather == "sunny":
                yes()
            else:
                no_weather()
        else:
            no_time()
    else:
        print("N/A")

def inp():
    season = input("Season (lowercase): ")
    time_hour = int(input("Enter the time (24hours): "))
    weather = input("Weather (sunny, cloudy, rainy, snowy): ")
    return season, time_hour, weather

def no_weather():
    print("There are no visible stars in the sky... ")
    print("Find a better weather")
def no_time():
    print("There are no visible stars in the sky... ")
    print("Wait for the sunset...")
def yes():
    print("There are visible stars in the sky! ")

main()