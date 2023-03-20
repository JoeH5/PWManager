from configparser import ConfigParser
from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parents[1]

def config(config_db):
    section = 'postgresql'
    config_file_path = 'config/' + config_db
    if(len(config_file_path) > 0 and len(section) > 0):
        config_parser = ConfigParser()
        config_parser.read(config_file_path)
        
        if(config_parser.has_section(section)):
            config_params = config_parser.items(section)
            db_connection_dict = {}
            for config_param in config_params:
                key = config_param[0]
                value = config_param[1]
                db_connection_dict[key] = value
            
            return db_connection_dict