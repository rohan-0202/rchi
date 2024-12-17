import os

from datasets import load_dataset
from dotenv import load_dotenv
from huggingface_hub import login

load_dotenv()

huggingface_token = os.getenv("HF_TOKEN")

login(huggingface_token)

# Loading the dataset
dataset = load_dataset(
    "pjura/mahjong_board_states",
    data_dir="data/2019/",
)

# Selecting relevant columns
selected_columns_indices = list(range(68, 135 + 1)) + list(range(238, 373 + 1)) + [510]
selected_columns_indices = [str(i) for i in selected_columns_indices]
dataset = dataset.select_columns(selected_columns_indices)

print(dataset["train"][0])
