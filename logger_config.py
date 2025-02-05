import logging
import os

class LoggerConfig:
    @staticmethod
    def setup_logging():
        # Get log level from .env or default to INFO
        log_level = getattr(logging, os.environ.get("LOG_LEVEL", "INFO").upper(), logging.INFO)

        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(filename="discord.log", encoding="utf-8", mode="a"),
                # logging.StreamHandler()  # log to console
            ]
        )