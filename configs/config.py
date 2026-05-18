import logging

logging.basicConfig(level=logging.INFO)

class Config:
    def __init__(self):
        pass

    def load_config(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as file:
                # Load configuration from file
                logging.info(f'Loaded configuration from {file_path}')
        except Exception as e:
            logging.error(f'Error loading configuration: {str(e)}')
            raise