class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of the Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets


class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)