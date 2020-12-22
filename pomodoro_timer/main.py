from datetime import timedelta
import time
import sys
import subprocess


WORK_TIME = timedelta(seconds=1500)
SHORT_BREAK = timedelta(seconds=300)
LONG_BREAK = timedelta(seconds=900)


def single_round(round_num, total_rounds):
    subprocess.run('clear')
    working = WORK_TIME
    print (f'Round {round_num} of {total_rounds}')
    while working:                  
        sys.stdout.write(f"\rTime to work: {working}")
        sys.stdout.flush()
        working -= timedelta(seconds=1)
        time.sleep(1)


def short_break():
    subprocess.run('clear')
    resting = SHORT_BREAK
    while resting: 
        sys.stdout.write(f"\rOn short break for {resting}")
        sys.stdout.flush()
        resting -= timedelta(seconds=1)
        time.sleep(1)


def long_break():
    subprocess.run('clear')
    resting = LONG_BREAK
    while resting:
        sys.stdout.write(f"\rOn long break for {resting}")
        sys.stdout.flush()
        resting -= timedelta(seconds=1)
        time.sleep(1)


def pomodoro(total_rounds, long_break_after=2):
    rounds = [i for i in range(1, total_rounds+1)]
    for round_number in rounds:
        single_round(round_number, total_rounds)
        if round_number == total_rounds:
            break
        elif round_number % long_break_after == 0:
            long_break()
        else:
            short_break()

    subprocess.run('clear')
    print(f"Good job, you've done {total_rounds} rounds")


if __name__ == "__main__":
    pomodoro(4)
