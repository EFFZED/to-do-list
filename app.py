import redis

data = {}

def get_task():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    try:
        tasks = r.hgetall('task')
        return tasks
    except Exception as err:
        print("Error: %s" % err)

def del_task(name):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    try:
        r.hdel('task', name)
    except Exception as err:
        print("Error: %s" %err)

def set_task(name, content):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    if (len(name) <= 0) or (name == " "):
        pass
    elif (len(content) <= 0) or (content == " "):
        pass
    else:
        data.update({name: content})

    try:
        r.hmset('task', data)
    except Exception as err:
        print("Error: %s" % err)



while True:
    task = get_task()
    print("========== All Tasks ========== \n")
    if task:
        for k, v in task.items():
            #Remove b'bytes' symbol.
            task_name = k.decode("utf-8")
            task_content = v.decode("utf-8")

            print("Task name: \"%s\" " % task_name)
            print("Your: \"%s\" plan is: \"%s\" \n" % (task_name, task_content))
    else:
        print("No task. \n")
    print("=============================== \n")

    print("(Add Task Press \"1\")  :  (Delete Task Press \"2\")  :  (Stop Program Press \"3\")")
    checked = int(input("Press: "))

    if (checked == 1):
        print("\n===> Suggestion: If you don't want to add more task. Please press \"Enter\" <=== ")
        task_name = str(input("Task name: "))
        task_content = str(input("What's your plan?: "))
        set_task(task_name, task_content)
        if task_name == "" or task_content == "":
            print("\nProgram has stopped. \n")
            break
        
    elif checked == 2:
        delete_task = str(input("\nWhat task you want to Delete?: "))
        del_task(delete_task)

    elif checked == 3:
        print("\nProgram has stopped. \n")
        break