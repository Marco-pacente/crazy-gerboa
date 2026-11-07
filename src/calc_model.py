from torch import nn
from torch import tensor
import numpy as np

class CalcModel(nn.Module):
    def __init__(self, in_features:int = 3, out_features: int = 2, levels = [6, 9, 12, 9, 6]):
        super().__init__()
        self.integrated_levels = [in_features] + levels + [out_features]
        self.blocks = nn.ModuleList()
        for idx in range(len(self.integrated_levels)-1):
            self.blocks.append(nn.Linear(in_features=self.integrated_levels[idx], out_features=self.integrated_levels[idx+1]))
        self.relu = nn.ReLU()
    
    def forward(self, x):
        for block in self.blocks:
            x = block(x)
            x = self.relu(x)
        return x