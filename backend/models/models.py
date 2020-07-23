import torch.nn as nn
from efficientnet_pytorch import EfficientNet
from torchvision.transforms import Compose, ToTensor, ToPILImage, Normalize

class EfficientNetB0(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = EfficientNet.from_pretrained('efficientnet-b0') 
        self.model._fc = nn.Linear(1280, 1)
        
    def forward(self, x):
        y = self.model(x).view(-1)
        return y

augs_test = Compose([
    ToPILImage(),
    ToTensor(), # also scales to [0, 1]
    Normalize(mean = [0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225])
])