import yaml

class Config:
    def __init__(self, config_file="config/config.yml"):
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        return config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage:
if __name__ == "__main__":
    app_config = Config()
    conf_log_level = app_config.config.get("log_level",   "DEFAULT")
    conf_log_path = app_config.config.get("log_path")
    conf_logger_name = app_config.config.get("logger_name")

    print(f"Log Level: {conf_log_level}")
    print(f"Log Path: {conf_log_path}")
    print(f"Logger Name: {conf_logger_name}")
    