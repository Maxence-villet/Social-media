class Queue:
    def __init__(self):
        self.queue:list

    def new_queue(self):
        self.queue = []

    def add_queue(self, value):
        self.queue.append(value)

    def delete_queue(self):
        self.queue.pop(0)

    def queue_empty(self):
        return len(self.queue) == 0
    
    def __str__(self):
        return f"La liste est {self.queue}" # type: ignore