# CPO-ddd-lab1  
CPO lab1  
## group name and list of group members  
   **group name:ddd**  
    group member :  
   **Wang Qihang:**  
       id:212320003  
       email: Wqhlw@hdu.edu.cn  
   **Wang zehao:**    
       id:212320005  
       email: 15029930122@163.com  
## Variant 4  
  ### Set based on hash-map, separate chaining  
    You can use the built-in list for storing buckets and a bucket itself  
    You need to check that your implementation correctly works with None value.  
## contribution  
    Wang Qihang Completed the mutable.py
    Wang Zehao Completed the test_mutable.py  
## descriptions of module
```
    class Node(object):  
        def __init__(self, key=None, value=None, next=None):  
    class HashMap(object):  
        init = object()  

        def __init__(self, dict=None, length=7):  
        def hash(self, key):  
         # 1. add  
        def add(self, key, value):  
        # 2. remove  
        def remove(self, key):  
        # get value  
        def get(self, key):  
        # 3. size  
        def get_size(self):  
         # 4. conversion  
         def hashmap_from_dict(self, dict):  
         def hashmap_from_list(self, list):  
         def hashmap_to_dict(self):  
         def hashmap_to_list(self):  
         # 5.find: return the even value list  
         def find_even(self):  
         # 6. filter: return the values' list except even value  
         def filter_even(self):  
         # 7.map(func)  
         def map(self, func):  
         # 8.reduce  
         def reduce(self, func, init_state):  
         # mempty and mconcat  
         def mempty(self):  
         def mconcat(self, a, b):   
```         
## Changelog   
   **4/14/2022**   
        Wang Qihang upload mutable.py  
   **4/14/2022**   
        Wang Zehao upload test_mutable.py  
## Design notes  
### Implementation restrictions
    The length of the hash table is fixed  
### Advantages and disadvantages of unittest  
   **Advantages**  
        Support automated testing
        Secondary development is convenient
        Organize test cases together by class  
   **Disadvantages**  
        Must be written in TestCase subclass
        Must write test method
        Difficult to expand
### Advantages and disadvantages of PBT tests
   **Advantages**  
        Check with automatically generated input data to ensure enough test cases
        Allows developers to increase test coverage and effectively save time  
   **Disadvantages**  
        Not covering all examples
