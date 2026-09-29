# STUDENT TASK MANAGER
# ➕ Add task — e.g. "Complete CS301 assignment"
# 📋 View tasks
# 🗑️ Delete task
# ✅ Mark task as completed
# ⭐ Set priority — Low / Medium / High
# 📅 Due date — when is it due?
# 🔍 Search tasks — find a particular assignment/task
print("\n Student Task Manager"
      "\n 1.Add_task"
      "\n 2.View_task"
      "\n 3.Delete task"
      "\n 4.Completed task"
      "\n 5.Set_priority"
      "\n 6.Due Date"
      "\n 7.Search_task")
def add_task():
    with open("task.txt","a") as file:
       quantity=int(input("Enter how many task you have to add: "))
       for i in range(quantity):
         task=input(" Enter the task (what you have to do):  ")
         file.write(task+"\n")
def view_task():
    print("The task you have entered:")
    with open("task.txt","r") as file:
       task=file.read()
       print(task)
def del_task():
   delete_task=input("Enter the task that you want to  delete:")
   with open("task.txt","r") as file:
      tasks=file.readlines()
   with open ("dup.txt","w") as temp:
         for task in tasks:
           if delete_task != task.strip():
             temp.write(task)
   import os
   os.replace("dup.txt","task.txt")
   print("Task removed successfully")
def completed_task():
    with open("task.txt", "r") as file:
        tasks = file.readlines()

    done_task = input("Enter the task that is done: ")

    found = False

    for i, task in enumerate(tasks):
        if done_task == task.strip():
            tasks[i] = task.strip() + " - Completed\n"
            found = True
            break

    if found:
        with open("task.txt", "w") as file:
            file.writelines(tasks)

        print(f"This {done_task} is completed")
    else:
        print("Invalid Command")
def set_priority():
        with open("task.txt","r") as file:
           x=file.readlines()
        for i,y in enumerate(x):
              print(i,"   ",y.strip() )
        task_num=int(input("enter task number:"))
        priority=input("Enter your priority:")
        selected_task=x[task_num]
        show=selected_task.strip() + "-_" + priority + "\n"
        x[task_num]=show
        with open ("task.txt","w") as file:
                file.writelines(x)
def due_date():
    with open("task.txt","r") as file:
        task=file.readlines()
    for i,y in enumerate(task):
        date=input(f"Enter date: {y.strip()}")
        task[i]=y.strip() + "  " +" Due " + date + "\n "
    with open("task.txt","w") as file:
        file.writelines(task)
def search_task():
   with open("task.txt","r") as file:
       task=file.readlines()
   enter_task=input("Enter the task that you search for: ")
   found=False
   for i in range(len(task)):
      if enter_task in task[i]:
          print(f"We found it{task[i].strip()}")
          found=True
   if found==False:
          print("Cannot find the search data")
while True:  
   choice=int(input("\n Enter your choice for task management: "))
   if choice==1:
    add_task()
   elif choice==2:
    view_task()
   elif choice==3:
      del_task()
   elif choice==4:
      completed_task()  
   elif choice==5:
      set_priority()
   elif choice==6:
       due_date()
   elif choice==7:
       search_task()
   else:
      print("Invalid Command")
      break

