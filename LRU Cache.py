class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = collections.OrderedDict()
        self.remain = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            v = self.dict.pop(key)
            self.dict[key] = v
            return v
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dict.popitem(last = False)
        self.dict[key] = value
