# Dependency inversion principle (DIP)
# In the initial code, the NotificationService class directly depends on the concrete
# classes EmailService and SmsService
# this violates the DIP, which states that high-level modules should not depend on
# low-level modules; both should depend on abstractions
# The direct dependency on concrete classes makes the NotificationService less
# flexible and harder to change or extend, as it's tightly coupled to specific
# implementations of the email and SMS services

class EmailService:
    def send_email(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")

class SmsService:
    def send_sms(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver}")

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()
    
    def send_notification(self, message, receiver, method):
        if method == "email":
            self.email_service.send_email(message, receiver)
        elif method == "sms":
            self.sms_service.send_sms(message, receiver)

# correction
# The NotificationService class now depends on the abstraction IMessageService
# rather than the concrete classes EmailService and SmsService
# this adheres to the DIP because both high-level and low-level classes depend
# on abstractions rather than concrete implementations, making the code more flexible
# and easier to change or extend.

from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass

class EmailService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending email : {message} to {receiver}")

class SmsService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver}")

class NotificationService:
    def __init__(self, message_service: IMessageService):
        self.message_service = message_service
    
    def send_notification(self, message, receiver):
        self.message_service.send(message, receiver)
        

