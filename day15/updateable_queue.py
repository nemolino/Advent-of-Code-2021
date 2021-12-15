import heapq

class UpdateableQueue:
    def __init__(self,iterable=None):
        self._heap = []
        self._entry_finder = {}
        if iterable:
            for item in iterable:
                self._entry_finder[item[0]] = item[1]
                heapq.heappush(self._heap,(item[1],item[0]))

    def __getitem__(self, key):
        if key in self._entry_finder:
            return self._entry_finder[key]
        else:
            raise KeyError('Item not found in the priority queue')

    def __len__(self):
        return len(self._entry_finder)

    def __contains__(self, key):
        return key in self._entry_finder

    def push(self, key, priority):
        self._entry_finder[key] = priority
        heapq.heappush(self._heap, (priority, key))

    def pop(self):
        if not self._heap:
            raise IndexError("The heap is empty")

        value,key = self._heap[0]
        while key not in self or self._entry_finder[key] != value:
            heapq.heappop(self._heap)
            if not self._heap:
                raise IndexError("The heap is empty")
            value,key = self._heap[0]

        value, key = heapq.heappop(self._heap)
        del self._entry_finder[key]
        return key,value
