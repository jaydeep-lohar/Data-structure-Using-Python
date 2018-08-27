size = input("Enter the size of stack \t")
stack = range(size)
top = -1

def push():
	ele = input("\nEnter the element to be Pushed\t")
	if is_full():
		print("\n Stack is full\t")
	else:
		global top
		top = top + 1
		# print("================================================"+str(top))
		stack[top] = ele
		display()

def pop():
	if is_empty():
		print("Stack is empty, hence can't pop")
	else:
		global top
		pop_ele = stack[top]
		top = top-1
		print("The poped element is as "+str(pop_ele))
		display()

def peek():
	if is_empty():
		print("As the stack is empty, hence no peek element")
	else:
		peek = stack[top]
		print("The peek element is "+str(peek))
		display()

def display():
	if is_empty():
		print("Stack is empty")
	else :
		global top
		i=top
		# print("================================================"+str(top))
		for i in range(top,-1,-1):
			print(str(stack[i]))

def is_empty():
	if top == -1:
		return True
	else:
		return False

def is_full():
	if top == size-1:
		return True
	else:
		return False

def __main__():
	while True:
		ch = input(" \n Input your choice as below\n 1. Push \n 2. Pop \n 3. Peek \n 4. Display full stack \n 5. Isempty \n 6. Isfull \n 7. To exit \n \n")
		if ch == 1:
			push()
		elif ch == 2:
			pop()
		elif ch == 3:
			peek()
		elif ch == 4:
			display()
		elif ch == 5:
			if is_empty():
				print ("Stack is empty \n top = "+str(top))
			else:
				print ("Stack is not empty \n top = " + str(top))
		elif ch == 6:
			if is_full():
				print ("Stack is full \n top ="+str(top))
			else:
				print ("Stack is not full \n top =" +str(top ))
		elif ch == 7:
			exit()
		else:
			print("Invalid option")

if __name__ == "__main__":
	__main__()