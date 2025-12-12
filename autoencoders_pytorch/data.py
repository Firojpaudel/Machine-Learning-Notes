import torch
from torch.utils.data import DataLoader
import torchvision.datasets as Datasets
import torchvision.transforms as transforms

def get_mnist_loaders(root, batch_size, image_size=32, num_workers=2):
    """Create MNIST train and test dataloaders"""
    transform = transforms.Compose([
        transforms.Resize(image_size),
        transforms.ToTensor(),
        transforms.Normalize([0.5], [0.5])
    ])

    train_set = Datasets.MNIST(root=root, train=True, transform=transform, download=True)
    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=num_workers)

    test_set = Datasets.MNIST(root=root, train=False, transform=transform, download=True)
    test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=False, num_workers=num_workers)
    
    return train_loader, test_loader