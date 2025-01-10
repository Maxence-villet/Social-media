from Tools import stack

def main():

    # create instance of stack
    s = stack.Stack()
    s.new_stack()

    #check if is it empty
    print(s.stack_empty())


    #add random values
    s.add_stack(48)
    s.add_stack(156)
    s.add_stack(7)
    s.add_stack(542)
    s.add_stack(4645)
    s.add_stack(4686)
    s.add_stack(145)

    
    #print list
    print(s)

    #delete 2 values
    s.delete_stack()
    s.delete_stack()

    #print list
    print(s)
main()