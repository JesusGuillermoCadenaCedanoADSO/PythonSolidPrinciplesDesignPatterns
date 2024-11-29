import json

class ConfigManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Implement the singleton pattern
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
        # pass

    def __init__(self):
        # Initialize an empty dictionary to store the configuration settings
        if not hasattr(self, "config"): # solo inicializa el diccionario si no existe
            self.config = {}
        #pass

    def load_config(self, config_file):
        # Read the JSON configuration file and store the settings in the dictionary
        with open(config_file, 'r') as file:
            self.config = json.load(file)
            # print(self.config)
        #pass

    def get_setting(self, key):
        # Retrieve the setting value by key
        # the get method fo the dictionary allows to provide a default value if the key
        # is not found
        return self.config.get(key)
        #pass

# Create a sample JSON configuration file named 'config.json'
sample_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "password"
    },
    "api": {
        "host": "0.0.0.0",
        "port": 8000
    }
}

with open("config.json", "w") as f:
    json.dump(sample_config, f)

# Testing the singleton behavior and config management
config1 = ConfigManager()
config2 = ConfigManager()

print(f"config1: {id(config1)}")
print(f"config2: {id(config2)}")

config1.load_config("config.json")
print(config1.get_setting("database"))
print(config2.get_setting("api"))

