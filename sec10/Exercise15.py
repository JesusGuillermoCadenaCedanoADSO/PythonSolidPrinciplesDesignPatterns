from abc import ABC, abstractmethod
from enum import Enum

class State(Enum):
    ASSIGN = "Assigned"
    RESOLVE = "Resolved"
    CLOSE = "Closed"

# Step 1: Define the abstract base class TicketState
class TicketState(ABC):

    @abstractmethod
    def assign(self, ticket):
        pass

    @abstractmethod
    def resolve(self, ticket):
        pass

    @abstractmethod
    def close(self, ticket):
        pass

# Step 2: Implement the concrete state classes
class NewState(TicketState):

    def assign(self, ticket):
        # Implement the behavior for assigning a new ticket
        ticket.state = AssignedState()
        #pass

    def resolve(self, ticket):
        # Implement the behavior for resolving a new ticket
        print("cannot resolve a new ticket")
        #pass

    def close(self, ticket):
        # Implement the behavior for closing a new ticket
        print("Closing the ticket")
        ticket.state = ClosedState()
        #pass

# Implement the other concrete state classes: AssignedState, ResolvedState, and ClosedState

class AssignedState(TicketState):
    def assign(self, ticket):
        # Implement the behavior for assigning a new ticket
        print("Ticket is already assigned.")
        #pass

    def resolve(self, ticket):
        # Implement the behavior for resolving a new ticket
        print("Resolving the ticket.")
        ticket.state = ResolvedState()
        #pass

    def close(self, ticket):
        # Implement the behavior for closing a new ticket
        print("Closing the ticket")
        ticket.state = ClosedState()
        #pass

class ResolvedState(TicketState):
    def assign(self, ticket):
        # Implement the behavior for assigning a new ticket
        print("Cannot assign a resolved ticket")
        #pass

    def resolve(self, ticket):
        # Implement the behavior for resolving a new ticket
        print("Ticket is already resolved")

        #pass

    def close(self, ticket):
        # Implement the behavior for closing a new ticket
        print("Closing the ticket")
        ticket.state = ClosedState()
        #pass


class ClosedState(TicketState):
    def assign(self, ticket):
        # Implement the behavior for assigning a new ticket
        print("Cannot assign a closed ticket")
        # pass

    def resolve(self, ticket):
        # Implement the behavior for resolving a new ticket
        print("Cannot resolve a closed ticket")

        # pass

    def close(self, ticket):
        # Implement the behavior for closing a new ticket
        print("Ticket is already closed")
        #pass

# Step 3: Implement the Ticket class
class Ticket:

    def __init__(self):
        # Initialize the ticket's state attribute with an instance of the NewState class
        self.state = NewState()
        # pass

    def assign(self):
        # Delegate the assign method call to the current state object
        self.state.assign(self)
        #pass

    def resolve(self):
        # Delegate the resolve method call to the current state object
        self.state.resolve(self)
        #pass

    def close(self):
        # Delegate the close method call to the current state object
        self.state.close(self)
        #pass

# Step 4: Test the behavior of the ticket and its state transitions
def main():
    ticket = Ticket()

    # Test the initial state and transitions
    ticket.assign()
    ticket.resolve()
    ticket.close()

    # Test invalid transitions
    ticket.assign()
    ticket.resolve()

if __name__ == "__main__":
    main()
