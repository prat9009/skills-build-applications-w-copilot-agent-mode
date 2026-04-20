# CRUD Operations in Python

class CRUD:
    def __init__(self):
        self.data = []

    def create(self, item):
        self.data.append(item)
        return item

    def read(self, item):
        return item if item in self.data else None

    def update(self, old_item, new_item):
        if old_item in self.data:
            index = self.data.index(old_item)
            self.data[index] = new_item
            return new_item
        return None

    def delete(self, item):
        if item in self.data:
            self.data.remove(item)
            return item
        return None
