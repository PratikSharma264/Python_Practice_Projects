import os
file_path="task.txt"
class Task:
    def addTask(self):
        x = input("Enter a task: ")
        with open("task.txt", "a") as f:
            f.write(x + "\n")
    
    def viewTask(self):
        
        if os.path.exists(file_path):
            if os.path.getsize(file_path) == 0:
                print("No tasks specified.")
            else:
                with open(file_path, "r") as f:
                    print(f.read())
        else:
            print("File does not exist.")
    
    def clearAllTask(self):
       
        if os.path.exists(file_path):
            os.remove(file_path)
            print("All tasks have been removed.")
        else:
            print("File doesn't exist.")

    #def completedTask(self):


a = Task()
print("\nMenu")
print("1. Add Task")
print("2. View Task")
print("3. Remove All Tasks")
#print("4. Mark as completed")
print("4. Exit")

while True:
    print("Enter your choice:")
    x = int(input())
    if x == 1:
        a.addTask()
    elif x == 2:
        a.viewTask()
    elif x == 3:
        a.clearAllTask()
    #elif x== 4:
        #a.completedTask()
    elif x == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
