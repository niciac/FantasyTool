import logging


class MyLogger(logging.Logger):
    def __init__(self, name, level=logging.DEBUG):
        super().__init__(name=name, level=level)

    def add_stream_handler(self, level=logging.DEBUG):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        self.addHandler(console_handler)

    def add_file_handler(self, level=logging.DEBUG, filename="log.log"):
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(level)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        self.addHandler(file_handler)
