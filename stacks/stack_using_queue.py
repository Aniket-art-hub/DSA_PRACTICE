import queue


#################  APPROACH 1 BY USING TWO STACKS  ###########################
class MyStack(object):   ############## in this push is O(N) and rest is O(1) means push is costly ########################

    def __init__(self):
        self.queue1=[]
        self.queue2=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)
        i=0
        while (i<len(self.queue1)-1):
            self.queue2.append((self.queue1.pop()))
            i+=1
            

    def pop(self):
        
        """
        :rtype: int
        """
        if self.queue1:
            return self.queue1.pop()
        return -1
        

    def top(self):
        """
        :rtype: int
        """
        if self.queue1:
            return self.queue1[-1]
        return -1
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue1:
            return False
        return True

#################  APPROACH 2 BY USING One STACKS  ###########################

class MyStack(object):   ############## in this push is O(N) and rest is O(1) means push is costly ########################

    def __init__(self):
        self.queue = queue.Queue()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.put(x)
        i=0
        while (i<(self.queue.qsize())-1):
            self.queue.put((self.queue.get()))
            i+=1
            

    def pop(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue.get()
        return -1
        

    def top(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue.queue[0]
        return -1
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.queue.empty():
            return True
        return False
        
