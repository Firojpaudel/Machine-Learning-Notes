import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm, trange

from config import *
from autoencoder import AE
from data import get_mnist_loaders
from denoise import add_noise

def train():
    # Load data
    train_loader, test_loader = get_mnist_loaders(ROOT_DIR, BATCH_SIZE, IMAGE_SIZE)
    
    # Create model
    ae_net = AE(channel_in=CHANNELS, ch=CH, z=LATENT_SIZE).to(DEVICE)
    
    # Setup optimizer and loss
    optimizer = optim.Adam(ae_net.parameters(), lr=LEARNING_RATE)
    loss_func = nn.MSELoss()
    
    loss_log = []
    train_loss = 0
    
    # Training loop
    pbar = trange(0, NUM_EPOCHS, leave=False, desc="Epoch")
    for epoch in pbar:
        pbar.set_postfix_str('Loss: %.4f' % train_loss)
        for i, data in enumerate(tqdm(train_loader, leave=False, desc="Training")):
            image = data[0].to(DEVICE)
            
            # Create noisy data
            noisy_img = add_noise(image, NOISE_SCALE)
            
            # Forward pass
            recon_data, _ = ae_net(noisy_img)
            
            # Calculate loss
            loss = loss_func(recon_data, image)
            loss_log.append(loss.item())
            train_loss = loss.item()
            
            # Backward pass
            ae_net.zero_grad()
            loss.backward()
            optimizer.step()
    
    # Save model
    torch.save(ae_net.state_dict(), 'ae_model.pth')
    
    return ae_net, loss_log, test_loader

if __name__ == "__main__":
    model, losses, test_loader = train()