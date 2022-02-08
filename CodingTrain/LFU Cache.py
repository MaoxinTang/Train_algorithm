class LFUCache:
    """
    Least Frequently Used Class with O(1) average get() and put()

    1. Initialized with a capacity
    2. When put() is called, if the number of elements >= capacity, then the least frequently used element is evicted
    3. If there are multiple elements with the same usage count, then the least recently used element is evicted
        to break the tie

    Approach:

    1. Store the capacity, current number of elements, and the min_use_count value as fields on the object
    2. Maintain a map of key -> DLL Node for O(1) lookups of elements
    3. Maintain a map of usage_count -> DoubleLinkedList (DLL) to enable LFU and LRU properties
        - Each bucket has a DLL that is sorted by most recently used to least recently used
        - We enable LFU by tracking the min_use_count so we can find the LFU bucket in O(1)
        - We enabled LRU by maintaining an LRU ordering of the DLL nodes per bucket, so the LRU item is last
    """

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.size: int = 0
        self.min_use_count: int = 0

        # key value store to enable O(1) lookups
        self.kv_store: Dict[int, 'Node'] = {}

        # kv store to track usage counts so we can enable LFU properties, with LRU tie breaks
        # The DoubleLinkedList is sorted by LRU properties, with the first element being the most recent,
        #   and the last element being the oldest element to be modified (for the usage count bucket)
        self.usage_counters: Dict[int, 'DoubleLinkedList'] = {}

    def get(self, key: int) -> int:
        """
        1. Return the value associated with the key in O(1) time
        2. Return -1 if not present (more commonly, throw a key error)

        Because the element has been used, we must invoke self.__update_usage_count update it's usage frequency
        """

        if key not in self.kv_store:
            return -1

        node = self.kv_store[key]
        self.__update_usage_count(node)
        return node.value.value

    def put(self, key: int, value: int) -> None:
        """
        Upsert the key value pair in the cache in O(1) time on average

        1. Insertion:
            - When a new key, value pair is inserted, it's use count is 1, so it is prepended to the
                DLL for usage count 1
            - If the cache is at capacity, evict the least frequently used element, if there are ties
                then the least recently used element (among the LFU cohort) is removed see the self.__evict() method
        2. Update:
            - When an existing key is updated to a new value, it's value is updated, then __update_usage_count() is
                invoked to update it's usage frequency
        """
        if self.capacity == 0:
            return None

        if key in self.kv_store:
            node = self.kv_store[key]
            node.value.value = value
            self.__update_usage_count(node)
            return
        else:
            # should never be > but lets be safe...
            if self.size >= self.capacity:
                self.__evict()

            new_cache_entry = CacheEntry(key, value)
            self.min_use_count = new_cache_entry.use_count

            node = Node(new_cache_entry)

            self.kv_store[key] = node
            dllist = self.usage_counters.get(self.min_use_count, DoubleLinkedList())
            dllist.prepend(node)
            self.usage_counters[self.min_use_count] = dllist
            self.size += 1

        return

    def __update_usage_count(self, node: 'Node'):
        """
        Updates a cache entries usage frequency

            1. Remove the node from the DLL it is currently in
            2. If the DLL for the usage count is now empty, delete the map entry
            3. If the DLL for the usage count is now empty and the usage count == min_count, increment min_count by 1
            4. Increment the cache entry usage count by 1
            5. Prepend the node to the DLL associated with the new usage count, creating the DLL if not present
                The node is prepended because it is the most recently used item in the set, and we maintain LRU order
                in the DLL, which is sorted from most recently used to least recently used
        """

        old_dllist = self.usage_counters.get(node.value.use_count, None)

        # this shouldn't be None but just to be safe...
        if old_dllist is not None:
            old_dllist.remove(node)

            if old_dllist.is_empty():
                del self.usage_counters[node.value.use_count]
                self.min_use_count = self.min_use_count if node.value.use_count != self.min_use_count else self.min_use_count + 1

        node.value.use_count += 1
        dllist = self.usage_counters.get(node.value.use_count, DoubleLinkedList())
        dllist.prepend(node)
        self.usage_counters[node.value.use_count] = dllist

    def __evict(self):
        """
        Removes the least frequently used element from the cache. If there are multiple element with the same usage
            frequency, then the least recently used policy is used to break ties

            1. To evict an element, get the DLL associated with the min_use_count value,
            2. Remove the last element of the DLL (LRU) from the cache
            3. If the DLL is now empty, O(n) search the keys for the new min usage count
                ** Technically this violates the O(1) runtime, but the problem indicates to target O(1) on average,
                    so on average eviction is O(1) unless we get unlucky and remove the last element from the bucket
            4. Delete the entry in the kv store associated with the cache entry
            5. Decrement size by 1
        """

        min_dll = self.usage_counters.get(self.min_use_count, None)
        # shouldn't happen but lets be safe ...
        if min_dll is None:
            self.min_use_count = self.__find_min_usage_count()
            min_dll = self.usage_counters.get(self.min_use_count)

        node = min_dll.remove_last()
        if node is None:
            return
        if min_dll.is_empty():
            del self.usage_counters[self.min_use_count]
            self.min_use_count = self.__find_min_usage_count()

        del self.kv_store[node.value.key]
        self.size -= 1
        return

    def __find_min_usage_count(self) -> int:
        """
        Naively O(n) search all the keys for the min usage
        """
        min_usage = float('inf')
        for key in self.usage_counters:
            min_usage = min(min_usage, key)
        return min_usage


class CacheEntry:
    def __init__(self, key: int, value: int, use_count: int = 1):
        self.key: int = key
        self.value: int = value
        self.use_count: int = use_count


class Node:
    def __init__(self, value: 'CacheEntry', prev: 'Node or None' = None, nxt: 'Node or None' = None):
        self.value: 'CacheEntry' = value
        self.prev: 'Node or None' = prev
        self.nxt: 'Node or None' = nxt


class DoubleLinkedList:
    def __init__(self):
        self.first: 'Node or None' = None
        self.last: 'Node or None' = None

    def is_empty(self) -> bool:
        return self.first is None

    def prepend(self, node: 'Node') -> None:
        node.prev = None
        node.nxt = None

        if self.first is None:
            self.first = node
            self.last = node
        else:
            node.nxt = self.first
            self.first.prev = node
            self.first = node
        return

    def remove_last(self) -> 'Node or None':
        return self.remove(self.last)

    def remove(self, node: 'Node') -> 'Node or None':
        if node is None:
            return None

        prev = node.prev
        nxt = node.nxt

        if prev is None and nxt is None:
            self.first = None
            self.last = None
            return node

        if prev is None:
            self.first = nxt
            if nxt is not None:
                nxt.prev = None
        else:
            prev.nxt = nxt

        if nxt is None:
            self.last = prev
            if prev is not None:
                prev.nxt = None
        else:
            nxt.prev = prev

        return node