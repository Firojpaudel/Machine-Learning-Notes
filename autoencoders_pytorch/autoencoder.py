import torch
import torch.nn as nn
import torch.nn.functional as F

class Encoder(nn.Module):
    def __init__(self, channels, ch=32, z=32):
        super(Encoder, self).__init__()
        self.conv1 = nn.Conv2d(channels, ch, 4, stride=2, padding=1)
        self.bn1 = nn.BatchNorm2d(ch)
        
        self.conv2 = nn.Conv2d(ch, ch*2, 4, stride=2, padding=1)
        self.bn2 = nn.BatchNorm2d(ch*2)
        
        self.conv3 = nn.Conv2d(ch*2, ch*4, 4, stride=2, padding=1)
        self.bn3 = nn.BatchNorm2d(ch*4)

        self.conv_out = nn.Conv2d(ch*4, z, 4, stride=1, padding=0)
        
    def forward(self, x):
        x = F.relu(self.bn1(self.conv1(x)))
        x = F.relu(self.bn2(self.conv2(x)))
        x = F.relu(self.bn3(self.conv3(x)))
        return self.conv_out(x)
    
class Decoder(nn.Module):
    def __init__(self, channels, ch=32, z=32):
        super(Decoder, self).__init__()
        self.conv1 = nn.ConvTranspose2d(z, ch*4, 4, stride=1, padding=0)
        self.bn1 = nn.BatchNorm2d(ch*4)
        
        self.conv2 = nn.ConvTranspose2d(ch*4, ch*2, 4, stride=2, padding=1)
        self.bn2 = nn.BatchNorm2d(ch*2)
        
        self.conv3 = nn.ConvTranspose2d(ch*2, ch, 4, stride=2, padding=1)
        self.bn3 = nn.BatchNorm2d(ch)
        
        self.conv4 = nn.ConvTranspose2d(ch, channels, 4, stride=2, padding=1)

    def forward(self, x):
        x = F.relu(self.bn1(self.conv1(x)))
        x = F.relu(self.bn2(self.conv2(x)))
        x = F.relu(self.bn3(self.conv3(x)))
        x = torch.tanh(self.conv4(x))
        return x
    
class AE(nn.Module):
    def __init__(self, channel_in, ch=16, z=32):
        super(AE, self).__init__()
        self.encoder = Encoder(channels=channel_in, ch=ch, z=z)
        self.decoder = Decoder(channels=channel_in, ch=ch, z=z)

    def forward(self, x):
        encoding = self.encoder(x)
        x = self.decoder(encoding)
        return x, encoding