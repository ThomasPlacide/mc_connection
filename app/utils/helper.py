import logging

class Logger:
    @staticmethod
    def setup_logger(name, log_file: str = "logs/app.log", level=logging.INFO):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        
        if not logger.hasHandlers():
            ch = logging.StreamHandler()
            ch.setLevel(level)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            logger.addHandler(ch)

            fh = logging.FileHandler(log_file, mode="a+")
            fh.setLevel(level)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        return logger