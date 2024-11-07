import logging
import os
from pathlib import Path
from lerobot.common.datasets.push_dataset_to_hub.pusht_zarr_format import load_from_raw

os.makedirs("logs", exist_ok=True)
# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    filename="logs/output.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
)

# 创建控制台处理器并设置级别为INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建格式化器并将其添加到控制台处理器
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
console_handler.setFormatter(formatter)

# 将控制台处理器添加到根记录器
logging.getLogger().addHandler(console_handler)

# 示例日志记录
logging.info("Starting the data loading process.")

raw_dir = Path("data/lerobot-raw/pusht_raw")
videos_dir = Path("data/lerobot-raw/pusht_raw/videos")
fps = 10
video = True
episodes = None
encoding = None

data_dict = load_from_raw(raw_dir, videos_dir, fps, video, episodes, False, encoding)
logging.info("Finished the data loading process.")
