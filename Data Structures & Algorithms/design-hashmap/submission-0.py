class MyHashMap:

    def __init__(self):
        self.size = 100
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]

        for i, (bucket_key, bucket_value) in enumerate(bucket):
            if bucket_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key,value))

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]

        for bucket_key, bucket_value in bucket:
            if bucket_key == key:
                return bucket_value

        return -1
        

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]

        for i, (bucket_key, bucket_value) in enumerate(bucket):
            if bucket_key == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)