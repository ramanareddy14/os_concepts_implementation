# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
import heapq

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None

        # this should be min heap to ease removal of lowest element
        self.hi_heap = []  
        self.hi_higher = None
        self.hi_lower = None

        # this should be max_heap to ease removal of highest element 
        # and inserting into higher heap
        self.low_heap = []
        self.low_higher = None
        self.low_lower = None

    def insert(self, number):
        # Write your code here.
        """
        We use two heaps
        1. heap_hi stores higher numbers [hi_low, Hi_highest, hi_len]
        2. heap_low stores lowest numbers [low_low, low_highest, low_len]

        3. if incomin number is < hi_low
                a.insert into heap_low
                b. if low_len > hi_len -1
                        remove heap_low root and insert into heap_hi
                            update all variables
                    else
                        update low - variables
            else 
                a. insert into heap_hi
                b. if hi_len > low_len -1
                    remove heap_hi hi_low and insert into heap_low
                        update all variables
                    else
                        update hi - variables

        4. Now update median
            if low_len == hi_len
                median = low_hi + hi_low /2
            else if low_len > hi_len
                median = low_hi
            else
                median = hi_low

        Time complexity: for every incomming stream[insert_into one heap + update both heaps]
                            N[logN + log N + logN]
                            N[log N]
        """
        

        if len(self.hi_heap) == 0 and len(self.low_heap) ==0 :
            heapq.heappush(self.hi_heap, number)
            self.hi_higher = number
            self.hi_lower = number
            self.median = number
            
            self.low_higher = None
            self.low_lower = None
            return

        if number  < self.hi_lower:
            heapq.heappush(self.low_heap, (-1)*number)
            if len(self.low_heap) == 1:
                    self.low_higher = self.low_lower = pop
            else:
                self.low_higher = max(self.low_higher, number)
                self.low_lower = min(self.low_lower, number)
            
            if len(self.low_heap) > len(self.hi_heap) +1: # 2,4
                pop = (-1)*heapq.heappop(self.low_heap)
                self.low_higher = (-1)*self.low_heap[0]
                # by now low heap has atleaset 2 elements so lower number doesn't change
                heapq.heappush(self.hi_heap, pop)
                # since we are pushing low heap higher into hi heap
                # the pushed num will be <= hi_lower
                # so we only updare hi_lower
                self.hi_lower = min(self.hi_lower,pop)

        else:
            heapq.heappush(self.hi_heap, number)
            # since this number is greater than hi_lower we only update hi_higher
            self.hi_higher = max(self.hi_higher,number)

            if len(self.hi_heap) > len(self.low_heap)+1:
                pop = heapq.heappop(self.hi_heap)
                self.hi_lower = self.hi_heap[0]
                # hi_higher won't change here 

                heapq.heappush(self.low_heap,(-1)*pop)
                if len(self.low_heap) == 1:
                    self.low_higher = self.low_lower = pop
                else:
                    # the lower element of hi_heap will be >= low_higher
                    self.low_higher = max(self.low_higher, pop)
                
        
        if len(self.low_heap) == len(self.hi_heap):
            self.median = (self.low_higher+ self.hi_lower)/2
        elif len(self.low_heap) > len(self.hi_heap):
            self.median = self.low_higher
        else:
            self.median = self.hi_lower

    
        self.getMedian()

    def getMedian(self):
        print("Higher heap: ",end='')
        print(self.hi_heap)
        
        print("Lower heap: ",end='')
        print(self.low_heap)
        print("median is :",self.median,'\n')
        
        return self.median

my_c = ContinuousMedianHandler()


for item in [5,10,100,200,6,13,14,50]:
    my_c.insert(item)




