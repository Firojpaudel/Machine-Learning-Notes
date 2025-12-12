import torch
import matplotlib.pyplot as plt
import torchvision.utils as vutils
import os

from config import DEVICE, NOISE_SCALE
from denoise import add_noise

# Create output directory if it doesn't exist
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_loss(loss_log, save_path=None):
    """Plot training loss"""
    if save_path is None:
        save_path = os.path.join(OUTPUT_DIR, "loss.png")
    
    plt.figure(figsize=(10, 5))
    plt.plot(loss_log)
    plt.title("MSE Loss")
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.savefig(save_path, dpi=100, bbox_inches='tight')
    print(f"Loss plot saved to {save_path}")
    plt.close()

def visualize_results(model, test_loader, output_dir=None):
    """Visualize ground truth, noisy input, and reconstruction"""
    if output_dir is None:
        output_dir = OUTPUT_DIR
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Get test images
    dataiter = iter(test_loader)
    test_images = next(dataiter)[0]
    
    # Create noisy images
    noisy_test_img = add_noise(test_images, NOISE_SCALE)
    
    # Ground Truth
    plt.figure(figsize=(20, 10))
    out = vutils.make_grid(test_images[0:8], normalize=True)
    plt.imshow(out.numpy().transpose((1, 2, 0)))
    plt.title("Ground Truth")
    plt.axis('off')
    gt_path = os.path.join(output_dir, "ground_truth.png")
    plt.savefig(gt_path, dpi=100, bbox_inches='tight')
    print(f"Ground truth saved to {gt_path}")
    plt.close()
    
    # Noisy Input
    plt.figure(figsize=(20, 10))
    out = vutils.make_grid(noisy_test_img[0:8], normalize=True)
    plt.imshow(out.numpy().transpose((1, 2, 0)))
    plt.title("Noisy Input")
    plt.axis('off')
    noisy_path = os.path.join(output_dir, "noisy_input.png")
    plt.savefig(noisy_path, dpi=100, bbox_inches='tight')
    print(f"Noisy input saved to {noisy_path}")
    plt.close()
    
    # Reconstruction
    plt.figure(figsize=(20, 10))
    model.eval()
    with torch.no_grad():
        recon_data, _ = model(noisy_test_img.to(DEVICE))
    out = vutils.make_grid(recon_data.detach().cpu()[0:8], normalize=True)
    plt.imshow(out.numpy().transpose((1, 2, 0)))
    plt.title("Reconstruction")
    plt.axis('off')
    recon_path = os.path.join(output_dir, "reconstruction.png")
    plt.savefig(recon_path, dpi=100, bbox_inches='tight')
    print(f"Reconstruction saved to {recon_path}")
    plt.close()