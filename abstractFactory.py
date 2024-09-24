from abc import ABC, abstractmethod

# Abstract Factory
class UserFactory(ABC):
    @abstractmethod
    def create_user(self):
        pass

# Concrete Factories
class ViewerFactory(UserFactory):
    def create_user(self):
        return Viewer()

class SubscriberFactory(UserFactory):
    def create_user(self):
        return Subscriber()

class AdministratorFactory(UserFactory):
    def create_user(self):
        return Administrator()

# Abstract Product: User
class User(ABC):
    @abstractmethod
    def get_role(self):
        pass

# Concrete Products
class Viewer(User):
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def get_role(self):
        return "Viewer"

class Subscriber(User):
    def __init__(self, payment_details):
        self.payment_details = payment_details

    def get_role(self):
        return "Subscriber"

class Administrator(User):
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def get_role(self):
        return "Administrator"

# Client
def create_user(factory, attributes):
    user = factory.create_user(**attributes)
    return user

# Using the Abstract Factory
viewer_factory = ViewerFactory()
subscriber_factory = SubscriberFactory()
administrator_factory = AdministratorFactory()

viewer_attributes = {"ip_address": "192.168.0.1"}
subscriber_attributes = {"payment_details": "Credit Card"}
administrator_attributes = {"employee_id": "EMP123"}

viewer = create_user(viewer_factory, viewer_attributes)
subscriber = create_user(subscriber_factory, subscriber_attributes)
administrator = create_user(administrator_factory, administrator_attributes)

print(f"Viewer's role: {viewer.get_role()}, IP Address: {viewer.ip_address}")
print(f"Subscriber's role: {subscriber.get_role()}, Payment Details: {subscriber.payment_details}")
print(f"Administrator's role: {administrator.get_role()}, Employee ID: {administrator.employee_id}")
