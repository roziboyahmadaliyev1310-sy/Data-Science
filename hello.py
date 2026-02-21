# print('salom')

class Workers:
    def __init__(self,worker,age=25):
        self.worker=worker
        self.age=age

    def age_worker(self):
        return self.age

    def name_worker(self):
        return self.worker


work="Ali"


tracker=Workers(work)
print(tracker.name_worker())
print(tracker.age_worker())
