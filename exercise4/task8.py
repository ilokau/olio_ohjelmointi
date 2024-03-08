
class Task:
    _id = 1 # joku mättää tässä class variablessa???
    
    def __init__(self, description: str, programmer: str, workload: int):
        self._id = Task._id # chättis ehdotti tätä, mut ei toimi
        Task._id += 1 # chättis ehdotti tätä, mut ei toimi
        self._description = description
        self._programmer = programmer
        self._workload = int(workload)
        self._state = "Not Finished"
        
    def is_finished(self):
        return self._state == "Finished"
    
    def mark_finished(self):
        self._state = "Finished"
        
    def __str__(self):
        return f"Task {self._id}: {self._description}, Programmer: {self._programmer}, Workload: {self._workload}, State: {self._state}"
        
class OrderBook:
    def __init__(self):
        self._orders = []
    
    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self._orders.append(task)
        
    def all_orders(self):
        return self._orders
    
    def programmers(self):
        return set(order._programmer for order in self._orders)
    
    def mark_finished(self, id: int):
        for task in self._orders:
            if task._id == id:
                task.mark_finished()
                break
        else:
            raise ValueError(f"There is no task with id {id} on the list.")
    
    def finished_orders(self):
        return [task for task in self._orders if task.is_finished()]
        
    def unfinished_orders(self):
        return [task for task in self._orders if not task.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f"There is no programmer with this name.")
        
        finished_tasks = [task for task in self._orders if task.is_finished() and task._programmer == programmer]
        unfinished_tasks = [task for task in self._orders if not task.is_finished() and task._programmer == programmer]
                
        finished_hours = sum(task._workload for task in finished_tasks)
        unfinished_hours = sum(task._workload for task in unfinished_tasks)
            
        return len(finished_tasks), len(unfinished_tasks), finished_hours, unfinished_hours
        

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()
    
    def commands(self):
        print("Commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mask task as finished")
        print("5 programmers")
        print("6 status of programmer")
    
    def add_new_order(self):
        while True:
            try:
                description = input("description: ")
                programmer = input("programmer: ")
                workload = input("workload estimate: ")
                if not programmer or not workload:
                    raise ValueError("error: both programmer & workload should be provided")
                self.__orderbook.add_order(description, programmer, workload)
                print("added!")
                break
            except ValueError as e:
                print("error: enter valid input.")
        
    def list_finished_tasks(self):
        finished_orders = self.__orderbook.finished_orders()
        if not finished_orders:
            print("no finished orders")
        else:
            for task in finished_orders:
                print(task)
            
    
    def list_unfinished_tasks(self):
        unfinished_orders = self.__orderbook.unfinished_orders()
        if not unfinished_orders:
            print("no unfinished orders")
        else:
            for task in unfinished_orders:
                print(task)
    
    def mask_as_finished(self):
        while True:
            try:
                id = input("id: ")
                self.__orderbook.mark_finished(id)
                print("task marked as finished!")
                break
            except ValueError as e:
                print("error: please enter a valid id")
                print("error: ", e)
    
    def list_programmers(self):
        programmers = self.__orderbook.programmers()
        for programmer in programmers:
            print(programmer)
    
    def programmer_status(self):
        while True:
            try:
                programmer = input("programmer: ")
                finished_orders, unfinished_orders, finished_hours, unfinished_hours = self.__orderbook.status_of_programmer(programmer)
                print(f"tasks: finished {finished_orders}, unfinished {unfinished_orders}")
                print(f"hours: done {finished_hours}, scheduled {unfinished_hours}")
            except ValueError as e:
                print("error: please enter valid input")
    
    def execute(self):
        self.commands()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_new_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mask_as_finished()
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                self.programmer_status()


application = OrderBookApplication()
application.execute()
