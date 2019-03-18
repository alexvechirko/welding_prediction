import logging

# 创建一个logger
logger = logging.getLogger('tensorflow')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('log.txt', encoding='utf-8')
fh.setLevel(logging.INFO)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)


# 记录一条日志
def log_debug(message):
    logger.debug(message)


def log_info(message):
    logger.info(message)


# 记录一条错误
def log_error(error):
    logger.error('\n' + error + '\n')


def log_exception(error):
    logger.exception(error)
