class Car(object):
    name = 'General'
    model = 'GM'
    speed = 0
    kind = ""

    def __init__(self, name=None, model=None, kind=None):
        if name:
            self.name = name
        if model:
            self.model = model
        if kind:
            self.kind = kind

    @property
    def num_of_doors(self):
        if self.name.lower() in ['porshe', 'koenigsegg']:
            return 2
        return 4

    @property
    def num_of_wheels(self):
        if self.kind.lower() == 'trailer':
            return 8
        return 4

    def is_saloon(self):
        if self.kind.lower() != 'trailer':
            return True
        return False

    def drive(self, number):
        if number == 7:
            self.speed = 77
        elif number == 3:
            self.speed = 1000
        return self