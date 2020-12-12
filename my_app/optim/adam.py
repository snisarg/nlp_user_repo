from dataclasses import dataclass
from typing import Tuple

import torch

@dataclass
class AdamConf:
    __target__: str = "torch.optim.Adam"
    lr: float = 1e-3
    betas: Tuple[float, float] = (0.9, 0.999)
    eps: float = 1e-8
    weight_decay: float = 0
    amsgrad: bool = False
