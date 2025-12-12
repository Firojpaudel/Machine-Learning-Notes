from autoencoder import AE
from config import *
from data import get_mnist_loaders
from view import visualize_results, plot_loss
import torch

# Load data
_, test_loader = get_mnist_loaders(ROOT_DIR, BATCH_SIZE, IMAGE_SIZE)

# Load trained model
model = AE(channel_in=CHANNELS, ch=CH, z=LATENT_SIZE).to(DEVICE)
model.load_state_dict(torch.load('ae_model.pth'))

# Visualize
visualize_results(model, test_loader)