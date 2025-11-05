import time

from simple_tracker.tracker import Tracker


def read_interval():
    with open('config/config.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split(' = ')
            if key == 'interval':
                return int(value)

def main():
    t = Tracker()
    interval = read_interval()
    while True:
        t.increment()
        t.save_to_file()
        print(t)

        time.sleep(interval)

if __name__ == "__main__":
    main()