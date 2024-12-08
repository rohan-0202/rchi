import model_load_save
import matplotlib.pyplot as plt  # For plotting
import torch  # PyTorch for deep learning
import torch.nn as nn  # Neural networks module
import torchvision.transforms as transforms  # For image transformations
from lightning.pytorch.utilities.model_summary import ModelSummary  # For model summary
from pytorch_lightning import (  # For PyTorch Lightning framework
    LightningModule,
    Trainer,
)
from torch.nn import functional as F  # For functional API
from torch.utils.data import DataLoader  # For data loading
from model_load_save import load_model, save_model
from datasets import load_dataset


class Riichi(LightningModule):
    pass


if __name__ == "__main__":
    dataset = load_dataset("pjura/mahjong_board_states", data_dir="data/2019/")
    model_path = "models/rchi.pth"
    model = Riichi()
    load_model(model=model, path=model_path)
    save_model(model=model, path=model_path)
