#Group member: Qianyi, Zixuan, Chengyi, Tommy
#Date: Mar. 19, 2024
#Purpose: Create a program about the sky

def main():
    season, time_hour, time_minute, weather = inp()
    if season == "spring":
        if 19 >= time_hour and time_hour <= 7:
            if weather == "sunny":
                yes()
            else:
                no()
        else:
            no()
    if season == "summer":
        if 20 >= time_hour and time_hour <= 5:
            if weather == "sunny":
                yes()
            else:
                no()
        else:
            no()
    if season == "autumn" and season == "fall":
        if 19 >= time_hour and time_hour <= 7:
            if weather == "sunny":
                yes()
            else:
                no()
        else:
            no()
    if season == "winter":
        if 17 >= time_hour and time_hour <= 8:
            if weather == "sunny":
                yes()
            else:
                no()
        else:
            no()

def inp():
    season = input("Season (lowercase): ")
    time_hour = input("Enter the time (24hours): ")
    weather = input("Weather (sunny, cloudy, rainy, snowy):")
    return season, time_hour, weather

def no():
    print("There are no visible stars in the sky... ")
def yes():
    print("There are visible stars in the sky! ")

main()