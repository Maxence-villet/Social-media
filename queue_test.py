from Tools import queue

def main():

    # create instance of queue
    q = queue.Queue()
    q.new_queue()

    #check if is it empty
    print(q.queue_empty())


    #add random values
    q.add_queue(48)
    q.add_queue(156)
    q.add_queue(7)
    q.add_queue(542)
    q.add_queue(4645)
    q.add_queue(4686)
    q.add_queue(145)

    
    #print list
    print(q)

    #delete 2 values
    q.delete_queue()
    q.delete_queue()

    #print list
    print(q)
main()