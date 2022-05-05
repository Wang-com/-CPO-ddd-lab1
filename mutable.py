class Node(object):
    def __init__(self, key=None, value=None, next=None):
        """
            Used to initialize element nodes
            :param key:key of element node
            :param value:value of element node
            :param next:chain method to solve hash collision
        """
        self.key = key
        self.value = value
        self.next = next


class HashMap(object):
    init = object()

    def __init__(self, dict=None, length=13):
        # Initialization by dict
        if dict is not None:
            self.hashmap_from_dict(self, dict)
        self.keyList = []
        self.data = [self.init for i in range(length)]
        self.length = length
        self.index = 0

    def hash(self, key):
        hash_value = key % self.length
        return hash_value

    def add(self, key, value):
        """
           Insert key-value pairs into hash map
           :param key: The key to insert into the hash map
           :param value: element value
        """
        hash_value = self.hash(key)
        addNode = Node(key, value)
        if self.data[hash_value] == self.init:
            self.data[hash_value] = addNode
            self.keyList.append(key)
        else:
            head = self.data[hash_value]
            # loop to find the empty Node
            while head.next is not None:
                # key == ?
                if head.key == key:
                    head.value = value
                    return
                head = head.next
            # Judge whether it already exists
            if head.key == key:
                head.value = value
                return
            # Now find the empty Node
            head.next = addNode
            self.keyList.append(key)
        return

    def remove(self, key):
        '''
            Delete element in hash map by key
            :param key:element key
            :return:boolean type for delete success or failure
        '''
        hash_value = self.hash(key)
        if self.data[hash_value] is self.init:
            return False
        elif self.data[hash_value].key is key:
            self.data[hash_value] = self.data[hash_value].next
            self.keyList.remove(key)
            return True
        p = self.data[hash_value]
        q = self.data[hash_value].next
        while q.next is not None:
            if q.key == key:
                p.next = q.next
                self.keyList.remove(key)
                return True
            p = q
            q = q.next
        if q.key == key:
            p.next = None
            self.keyList.remove(key)
            return True

    def get(self, key):
        '''
            Find element in hash map by key.
            :param key:element key
            :return:element value response to the input key
        '''
        dict = self.hashmap_to_dict()
        value = dict[key]
        return value

    def get_size(self):
        '''
            Element number in hash map.
            :return:number of element in hash map
        '''
        size = len(self.keyList)
        return size

    def hashmap_from_dict(self, dict):
        '''
            add elements from dict type
            :param dict:input dict
            :return:
        '''
        for key, value in dict.items():
            self.add(key, value)

    def hashmap_from_list(self, list):
        '''
            add element from list type
            :param list:input list
        '''
        for key, value in enumerate(list):
            self.add(key, value)

    def hashmap_to_dict(self):
        '''
            transfer hashmap into dict
            :return: result dict
        '''
        Dict = {}
        if len(self.keyList) == 0:
            return Dict
        for i in range(self.length):
            if self.data[i] != self.init:
                head = self.data[i]
                while head is not None:
                    Dict[head.key] = head.value
                    head = head.next
        return Dict

    def hashmap_to_list(self):
        '''
            Transfer hashmap into list type
            :return:result list
        '''
        dict = self.hashmap_to_dict()
        list = []
        for key, value in dict.items():
            list.append(value)
        return list

    def find_even(self):
        '''
            Find element with even value in hashmap.
            :return:list with even number value
        '''
        dict = self.hashmap_to_dict()
        findlist = []
        for key, value in dict.items():
            if value % 2 == 0:
                findlist.append(value)
        return findlist

    def filter_even(self):
        '''
            Filter element with even value in hashmap.
            :return: list with not even number value
        '''
        list = self.hashmap_to_list()
        filterlist = []
        for value in list:
            if value % 2 != 0:
                filterlist.append(value)
        return filterlist

    def map(self, func):
        # map(func)
        list = self.hashmap_to_list()
        listOut = []
        for value in list:
            value = func(value)
            listOut.append(value)
        return listOut

    def reduce(self, func, init_state):
        """
            Reduce the mapSet to one value.
            :param f: the reduce method
            :param initial_state:result initial_state
            :return:final res
        """
        a = init_state
        for key in self.keyList:
            value = self.get(key)
            a = func(a, value)
        return a

    def empty(self):
        ReBuckets = []
        for i in range(self.length):
            head = Node(None, None, None)
            head.key = i
            ReBuckets.append(head)
        self.buckets = ReBuckets
        return self.buckets

    def concat(self, set):
        """
            Operation in property monoid.
            :param set:first input hash map
            :return: add element in set into self,return self
        """
        if self is None:
            return set
        elif set is HashMap:
            for key in set.keyList:
                value = set.get(key)
                self.add(key, value)
                return self
        return self

    def __iter__(self):
        iter_list = []
        for key in self.keyList:
            iter_list.append(Node(key, self.get(key)))
        return iter(iter_list)
