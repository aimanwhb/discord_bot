import logging
import os


class LoggerConfig:
    @staticmethod
    def setup_logging():
        try:
            log_dir = "log"
            # Create log directory if it doesn't exist
            if not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)
                print(f"Created log directory at: {os.path.abspath(log_dir)}")  # Debug output

            # Configure logging
            log_level = getattr(logging, os.environ.get("LOG_LEVEL", "INFO").upper(), logging.INFO)

            logging.basicConfig(
                level=log_level,
                format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                handlers=[
                    logging.FileHandler(filename=os.path.join(log_dir, "discord.log"), encoding="utf-8", mode="a"),
                    # logging.StreamHandler()  # Uncomment for console logging
                ]
            )
            print(f"Logging initialized. Log file: {os.path.abspath(os.path.join(log_dir, 'discord.log'))}")

        except Exception as e:
            print(f"Failed to initialize logging: {str(e)}")
            raise  # Re-raise the exception to see the full traceback