class Dog:
    def __init__(self, dog_id, name, age, breed, adopted=False, image=None):
        self.id = dog_id
        self.name = name
        self.age = age
        self.breed = breed
        self.adopted = bool(adopted)
        self.image = image  

    def __repr__(self):
        return f"<Dog {self.name} ({self.breed})>"

    def make_a_sound(self):
        return "¡Guau guau!"