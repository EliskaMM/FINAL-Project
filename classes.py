"""
Classes for handling individual policy holders and primitive policy holder database.
"""
class Policyholder:
    def __init__(self, name, surname, age, phone):
        if (not name[0].isupper()) or (not surname[0].isupper()):
            pass
        self._name = name
        self._surname = surname
        self._age = age
        self._phone = phone

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age

    @property
    def phone(self):
        return self._phone

    def __str__(self):
        return f"{self.name} {self.surname}, Phone: {self.phone}, Age: {self.age}."

class PolicyDatabase:

    def __init__(self):
        self._holders = list()

    def add_policy_holder(self, person: Policyholder):
        self._holders.append(person)


    def find_policy_holder_by_name(self, name):
        policy_holders = []
        for holder in self._holders:
            if holder.name == name:
                policy_holders.append(holder)
        return policy_holders

    def find_policy_holder_by_surname(self, surname):
        policy_holders = []
        for holder in self._holders:
            if holder.surname == surname:
                policy_holders.append(holder)
        return policy_holders

    def find_policy_holder_by_complete_name(self, name, surname):
        policy_holders = []
        for holder in self._holders:
            if (holder.name == name) and (holder.surname == surname):
                policy_holders.append(holder)
        return policy_holders

    def get_policy_holders(self):
        return self._holders