#   https://edabit.com/challenge/Yj2Rew5XQYpu7Nosq
#   Create a function that returns the number of frames shown in a given number of minutes for a certain FPS.


def frames(minutes: int, fps: int) -> int:
    try:
        total_frames = (minutes * 60) * fps
        return total_frames
    except TypeError as err:
        print(f"Error: {err}")


print(frames(1, 1))
print(frames(10, 1))
print(frames(10, 25))
print(frames("a", "b"))
