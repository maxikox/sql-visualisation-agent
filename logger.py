import logging

class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: "\033[36m",    # cyan
        logging.INFO: "\033[32m",     # green
        logging.WARNING: "\033[33m",  # yellow
        logging.ERROR: "\033[31m",    # red
        logging.CRITICAL: "\033[41m", # red background
    }
    WHITE = "\033[37m"
    RESET = "\033[0m"
    GRAY = "\033[90m"

    def format(self, record):
        level_color = self.COLORS.get(record.levelno, self.RESET)

        # Color only the level name
        levelname = f"{level_color}{record.levelname}{self.RESET}"

        # Force message to white
        message = f"{self.WHITE}{record.getMessage()}{self.RESET}"
        timestamp = f"{self.GRAY}{self.formatTime(record)}{self.RESET}"

        return f"{timestamp} - {levelname} - {message}"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(handler)

if __name__ == "__main__":
    logger.debug("This Is Debug")