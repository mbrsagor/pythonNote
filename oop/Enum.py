import enum


class Book(enum.Enum):
    python = 1
    javascript = 2
    java = 3
    dart = 4


print(Book.python)
# using loop
for book in Book:
    print(book.name)

print(Book(2))
print(Book['dart'])


""" Start from new logic """
class Status(enum.Enum):
    START = 0
    INPROGRESS = 1
    PENDING = 2
    FINISHED = 3

class Task(object):

    def __init__(self, task_id, task_name, status):
        self.task_id = task_id
        self.task_name = task_name
        self.status = status
    
    def startTask(self):
        if self.status == Status.START:
            print "Task has been started"

task = Task(1, "Demo task", "Done")
task.startTask()
