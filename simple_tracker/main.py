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
    print(f"Interval set to: {interval} seconds")

    t = Tracker()
    while True:
        t.increment()
        t.save_to_file()
        print(t)
        time.sleep(interval)

if __name__ == "__main__":
    main()
