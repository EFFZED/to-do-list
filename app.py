#from/import
import redis

#identifier
data = {}
i = True
r = redis.StrictRedis(host='localhost', port=6379, db=0)

#function
def set_task(task_name, task_content):
    if (task_name and task_content) == "" or (task_name and task_content) == " ":
        pass
    else:    
        data.update({task_name: task_content})
    try:
        r.hmset('task', data)
    except Exception as err:
        print("Error: %s" % err)

def get_task():
    num = 1

    try:
        tasks = r.hgetall('task')
    except Exception as err:
        print("Error: %s" % err)

    print("\n========== All Task ==========")
    if tasks:
        for k, v in tasks.items():
            print(num, ") Task Name: %s" % k.decode("utf-8"))
            print(num, ") Task Plan: %s" % v.decode("utf-8"))
            num += 1
    else:
        print("No Task.")
    print("==============================\n")

def del_task(delete_name):
    try:
        r.hdel('task', delete_name)
        print("Deleted: %s" % delete_name)
    except Exception as err:
        print("Error: %s" % err)

#UI
get_task()

print("(Add Task Press: \"1\")   :   (Delete Task Press: \"2\")")
print("===> Suggestion: If you want to stop add more task. Please press \"Enter\" <===")
checked = int(input("Press: "))

while i == True:
    if checked == 1:
        task_name = str(input("Enter task name: "))
        task_content = str(input("What's your plan: "))

        if (task_name and task_content) == "" or (task_name and task_content) == " ":
            get_task()
            print("Program has Stopped! \n")
            break

        set_task(task_name, task_content)
    
    elif checked == 2:
        delete_name = str(input("Enter task name that you want to delete: "))
        del_task(delete_name)
        break

    else:
        print("\nPlease press \"1\" or \"2\"")
        print("Program has Stopped!\n")
        break
