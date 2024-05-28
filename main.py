class Worker:
    def __init__(self, id):
        self.id = id

class HR(Worker):
    def __init__(self, id, name, position):
        super().__init__(id)
        self.name = name
        self.position = position

    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}"

worker1 = HR(1, "Danatella", "Psixopad")
worker2 = HR(2, "Giga Chad", "Mativator")

print(worker1.get_details())
print(worker2.get_details())

# Third edition
