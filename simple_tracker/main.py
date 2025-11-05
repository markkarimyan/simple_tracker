import time
from simple_tracker.tracker import Tracker


def read_interval():
    with open('config/config.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            if key.strip() == 'interval':
                return int(value.strip())


def main():
    interval = read_interval()
    print(f"Simple Tracker is starting... Interval: {interval} seconds")


    tracker = Tracker()
    while True:
        tracker.increment()
        print(tracker)
        tracker.save_to_file()
        time.sleep(interval)


if __name__ == "__main__":
    main()
