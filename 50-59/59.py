#   https://edabit.com/challenge/QgSMSMpfcEebAyCye
#   One cause for speeding is the desire to shorten the time spent traveling.
#   In long distance trips speeding does save an appreciable amount of time.
#   However, the same cannot be said about short distance trips.
#
#   Create a function that calculates the amount of time saved
#   were you traveling with an average speed that is above the speed-limit
#   as compared to traveling with an average speed exactly at the speed-limit.
#
#   Speed = distance/time
#   The time returned should be in minutes, not hours.
#   The unit of speed is assumed to be miles per hour (mph).
#   The unit of distance is assumed to be miles.


def time_saved(spd_lmt: int, avg_spd: int, avg_spd_distance: int) -> float:
    try:
        avg_time = (avg_spd_distance / spd_lmt) * 60
        spd_time = (avg_spd_distance / avg_spd) * 60
        difference = (spd_time - avg_time) * -1
        return round(difference, 1)
    except TypeError as err:
        print(f"Error: {err}")


print(time_saved(80, 90, 40))
print(time_saved(80, 90, 4000))
print(time_saved(80, 100, 40))
print(time_saved(80, 100, 10))
