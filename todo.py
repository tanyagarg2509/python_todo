"""The sys module provides functions and variables used to manipulate different parts of the Python runtime environment."""
import sys
from datetime import datetime 
"""argv is a list of command line arguments.""" 
try:
    operation = sys.argv[1]
except IndexError:
    """if argv[1] doesn't exist"""
    operation = "help" 
if operation=='add':
    try:
        with open('todo.txt','a') as f:
            f.write(str(sys.argv[2])+"\n")
            print('Added todo: "',str(sys.argv[2]),'"',sep="")
            f.close()
    except IndexError:
        print('Error: Missing todo string. Nothing added!')
elif operation=='ls':
    try:
        myTodoList = []
        with open('todo.txt','r') as f:
            for line in f:
                content = line.split('\n')[0]
                if line:
                    myTodoList.append(content)
            if len(myTodoList)==0:
                print('There are no pending todos!')
            else:
                for i in range(len(myTodoList),0,-1):
                    todo = "["+str(i)+"] "+str(myTodoList[i-1])+"\n"
                    sys.stdout.buffer.write(todo.encode('utf8'))
            f.close()
    except FileNotFoundError:
        print('There are no pending todos!')
elif operation=='help':
    help = """Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics"""
    sys.stdout.buffer.write(help.encode('utf8'))
    

elif operation=='del':
    try:
        number = int(sys.argv[2])
        newTodoList = ""
        counter = 1
        flag = False
        if number>0:
            with open('todo.txt','r') as f:
                for line in f:
                    if line:
                        if counter==number:
                            flag = True
                            newTodoList+=""
                        else:
                            newTodoList+=line
                        counter+=1
                f.close()
            with open('todo.txt','w') as f:
                f.write(newTodoList)
                f.close()
        if flag == True:
            print("Deleted todo #",str(number), sep="")
        else:
            print('Error: todo #',str(number),' does not exist. Nothing deleted.',sep="")
    except IndexError:
        print("Error: Missing NUMBER for deleting todo.")
    except FileNotFoundError:
        print('There are no pending todos!')
elif operation=='done':
    try:
        number = int(sys.argv[2])
        newTodoList = ""
        counter = 1
        flag = False
        if number>0:
            with open('todo.txt','r') as f:
                for line in f:
                    if line:
                        if counter==number:
                            flag = True
                            newTodoList+=""
                            currentDate = datetime.today().strftime('%Y-%m-%d')
                            with open('done.txt','a') as f1:
                                f1.write('x '+currentDate+' '+line)
                                f1.close()
                        else:
                            newTodoList+=line
                        counter+=1
                f.close()
            with open('todo.txt','w') as f:
                f.write(newTodoList)
                f.close()
        if flag == True:
            print("Marked todo #",str(number)," as done.",sep="")
        else:
            print('Error: todo #',str(number),' does not exist.',sep="")
    except IndexError:
        print('Error: Missing NUMBER for marking todo as done.')
    except FileNotFoundError:
        print('There are no pending todos!')
elif operation=='report':
    try:
        pendingList = []
        completedList = []
        with open('todo.txt','r') as f:
            for line in f:
                if line:
                    content = line.split('\n')[0]
                    pendingList.append(content)
            f.close()
        with open('done.txt','r') as f:
            for line in f:
                if line:
                    content = line.split('\n')[0]
                    completedList.append(content)
        completed = len(completedList)
        pending = len(pendingList)
        print(datetime.today().strftime('%Y-%m-%d'),"Pending :",pending,"Completed :",completed)
    except FileNotFoundError:
        print('There are no pending todos!')
