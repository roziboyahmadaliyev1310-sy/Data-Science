print('salom')

class Workers:
    def __init__(self,worker):
        self.worker=worker

    def age_worker(self):
        return self.age

    def name_worker(self):
        return self.worker


work="Ali"


tracker=Workers(work)
print(tracker.name_worker())
