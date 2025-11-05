class Tracker:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def save_to_file(self):
        with open("data.txt", "w") as f:
            f.write(str(self.count))
    
    def reset(self):  
        self.count = 0  
          
    def __str__(self):
        return f"Current count is: {self.count}"