Tasks = []

while(True):
    print("\n=====TO-DO List=====")
    print("1. Add Tasks")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Exit")
    
    Choice = int(input("Choose any button: "))

    if(Choice==1):
        n_task = int(input("How many task do you want to add: "))
        
        for i in range(n_task):
            task = input("Write Your Task Here: ")
            Tasks.append({'Task':task, 'Done': False})
            print("Task Added!\n")
    elif(Choice==2):
        print("\nTasks:-")
        
        for index,task in enumerate(Tasks):
            status = "Done" if(task['Done']) else "Not Done"
            print(f"{index+1}. {Tasks[index]['Task']} - {status}")
    elif(Choice==3):
        task_index = int(input("Enter the task number you want to mark as read: "))
        
        if(task_index>=0 or task_index<len(Tasks)):
            Tasks[task_index-1]["Done"] = True
            print("Task Marked as read\n")
        else:
            print("Invalid task number\n")
    elif(Choice==4):
        print("Exiting the to-do list")
        break
    else:
        print("Invalid choice!.Please try again")