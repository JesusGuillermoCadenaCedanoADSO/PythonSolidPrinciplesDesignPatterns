# lazy instantiation
class ClassicSingleton:

    # class-level variable to store single class instance
    _instance = None
    
    # override the __init__ method to control initialization
    def __init__(self):
        # raise an error to prevent constructor utilization
        raise RuntimeError('Call instance() instead')
        
    @classmethod
    def get_instance(cls):
        if not cls._instance: Note: lazy instantiation
        # create new instance of the class
            cls._instance = cls.__new__(cls)
        # return the single instance of the class, either
        # newly created one or existing one
        return cls._instance


class Singleton:
    # class-level variable to store the single
    # instance of the class
    _instance = None
    # override the __new__ method to
    # control how new objects are created
    def __new__(cls):
        # create new instance of the class
        # and sotre it in _instance
        cls._instance = super().__new__(cls)
    # return the single instance of the class, either.
    # newly created one or existing one
    return cls._instance
    
#Singleton Metaclass

class SingletonMeta(type):
    # dictionary stores single instance of the class for each subclass of the singletonmeta metaclass
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        # single instance of the class already been created?
        if cls not in cls._instances:
            # create the instance by calling the __call__
            # method of the parent's (super().__call__())
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
        
# our actual singleton class
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass
        

# using metaclass we can create an eager loading singleton:
class SingletonMeta(type):
    # Dictionary store single instance of the class for 
    # each subclass of the singletonmeta metaclass
    # override: called during creation of sub-types
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # Eager loading of the class instance
        cls._instances[cls] = super().__call__()
    # returns the singleton instance
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

# our actual singleton class
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        pass

# Thread-Safe Implementation of Singleton Pattern

import threading

class ThreadSafeSingleton:
    # class-level variable. Stores single class instance
    _instance=None
    # class-level lock to ensure thread safety
    _lock  = threading.Lock()
    # __new__ method override. Thread-safe implementation
    def __new__(cls):
        # acquire the lock to ensure thread safety
        with cls._lock:
            # check if single instance has been created yet
            if not cls._instance:
                # create the single instnace of the class
                cls._instance = super().__new__(cls)
        # return the single instance of the class
        return cls._instance
        
      
    
    
    