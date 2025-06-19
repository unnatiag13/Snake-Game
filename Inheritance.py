class Animal:
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater.")
    def swim(self):
        print("Moving in water.")

nemo_the_fish= Fish()
nemo_the_fish.breathe()