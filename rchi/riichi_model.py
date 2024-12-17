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
from torch.utils.data import DataLoader, Dataset  # For data loading
from model_load_save import load_model, save_model
from datasets import load_dataset
import numpy as np


DEFENSE_SCALING = 0.75
PATHVALUE_SCALING = 0.001
LEARNING_RATE = 0.001


class MahjongDataset(Dataset):
    def __init__(self, dataset, split="train"):
        self.data = dataset[split]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        # Convert features to tensor, excluding GameID (511) and using 0-509 as features
        features = torch.tensor(item[:510], dtype=torch.float32)
        # Use column 510 (discard) as label
        label = torch.tensor(item[510], dtype=torch.long)
        return features, label


class Path:
    def __init__(self, amounts, points):
        self.remaining = len(amounts)
        self.amounts = amounts
        self.points = points

    def value(self):
        numer = 1
        for i in self.amounts:
            numer *= i
        return ((numer ** (1 / self.remaining)) * self.points) / np.exp(self.remaining)


def pathSum(paths):
    sum = 0
    for i in paths:
        sum += i.value()
    return sum


def findPaths(n, paths):  # will find all paths of length n and append them to paths
    pass


def atkLoss(tiles):  # input would be current hand of 13 tiles
    paths = []
    n = 1
    while n < 5 and len(paths) == 0:
        findPaths(n, paths)

    return np.exp(-PATHVALUE_SCALING * pathSum(paths))


def Lriichi(t, discards, exact_matches):
    if t in discards:
        return 0


def Lnext(t, discards, exact_matches):
    pass


def Lnormal(discards, exact_matches):
    return 1 / (1 + 2 * exact_matches)


def defLoss(t, wallamt):
    end = 1
    p1_discards = []
    p2_discards = []
    p3_discards = []
    exact_matches = p1_discards.count(t) + p2_discards.count(t) + p3_discards.count(t)

    if p1_discards:  # Should actually check if player is in riichi
        end *= 1 - Lnext(t, p1_discards, exact_matches)
    else:
        end *= 1 - Lriichi(t, p1_discards, exact_matches)

    if p2_discards:  # Should actually check if player is in riichi
        end *= 1 - Lnormal(p2_discards, exact_matches)
    else:
        end *= 1 - Lriichi(t, p2_discards, exact_matches)

    if p3_discards:  # Should actually check if player is in riichi
        end *= 1 - Lnormal(p3_discards, exact_matches)
    else:
        end *= 1 - Lriichi(t, p3_discards, exact_matches)

    return 1 - (1 - (wallamt / 70)) * end


class Riichi(LightningModule):
    def __init__(self):
        super.__init__(self)

    def forward(self, x):
        pass

    def calculate_loss(self, batch, batchidx):
        x, y = batch
        atk = atkLoss(x)
        return atk - (DEFENSE_SCALING * atk * (1 - defLoss(x)))

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=LEARNING_RATE)


def setup_training():
    # Load dataset
    dataset = load_dataset("pjura/mahjong_board_states", data_dir="data/2019/")

    # Create dataloaders
    train_dataset = MahjongDataset(dataset, split="train")
    val_dataset = MahjongDataset(dataset, split="validation")

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=4)

    val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False, num_workers=4)

    # Initialize model and trainer
    model = Riichi()
    trainer = Trainer(max_epochs=10, accelerator="auto", devices=1)

    return model, trainer, train_loader, val_loader


if __name__ == "__main__":
    model, trainer, train_loader, val_loader = setup_training()
    trainer.fit(model, train_loader, val_loader)
    model_path = "models/rchi.pth"
    model = Riichi()
    load_model(model=model, path=model_path)
    save_model(model=model, path=model_path)
