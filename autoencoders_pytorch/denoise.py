import torch

def add_noise(images, noise_scale=0.3):
    """Add salt-and-pepper noise to images"""
    random_sample = (torch.bernoulli((1 - noise_scale) * torch.ones_like(images)) * 2) - 1
    noisy_images = random_sample * images
    return noisy_images