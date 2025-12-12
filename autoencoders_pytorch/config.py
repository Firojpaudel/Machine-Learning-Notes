import torch

## Training hyperparams
BATCH_SIZE = 64
LEARNING_RATE = 1e-4
NUM_EPOCHS = 10
LATENT_SIZE = 128


# Dataset settings 
ROOT_DIR = "../datasets"
IMAGE_SIZE = 32

# Denoising settings 
NOISE_SCALE = 0.3

# Model architecture
CHANNELS = 1  # Grayscale for MNIST
CH = 32  # Base channel multiplier

# Device settings
USE_CUDA = torch.cuda.is_available()
GPU_INDEX = 0
DEVICE = torch.device(GPU_INDEX if USE_CUDA else "cpu")