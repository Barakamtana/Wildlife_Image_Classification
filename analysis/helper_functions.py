import torch
from tqdm.notebook import tqdm

def get_mean_std (loader):
    channels_sum = 0
    channels_squared_mean_sum = 0
    num_batches = 0
    for batch, (images, labels) in tqdm(enumerate(loader), desc="Computing mean and std"):
        # batch_channel_mean0 = torch.mean(images, dim=[0, 2, 3])
        
        red_channel = images[:, 0, :, :].mean()
        green_channel = images[:, 1, :, :].mean()
        blue_channel = images[:, 2, :, :].mean()
        
        # Combine the individual channel means into a single tensor
        channel_mean = torch.tensor([red_channel, green_channel, blue_channel])
    
        # Squared mean for each channel (red, green, blue)
        red_channel_squared_mean = (images[:, 0, :, :]**2).mean()  # mean of squared values in red channel
        green_channel_squared_mean = (images[:, 1, :, :]**2).mean()  # mean of squared values in red channel
        blue_channel_squared_mean = (images[:, 2, :, :]**2).mean()  # mean of squared values in red channel
        
        channel_squared_mean = torch.tensor([red_channel_squared_mean, green_channel_squared_mean, blue_channel_squared_mean])
        
        # Accumulate the sum of means and squared means for all batches
        channels_sum += channel_mean
        channels_squared_mean_sum += channel_squared_mean
    
        num_batches += 1
    
    
    mean = channels_sum / num_batches
    mean_of_the_squared_values = (channels_squared_mean_sum / num_batches)
    variance = (mean_of_the_squared_values - mean ** 2)
    std = variance ** 0.5

    return mean , std
    

# get class index
def class_index(df, column_of_interest):
    return  {
        label:idx for idx, label in enumerate(df[column_of_interest].unique())
    }
    
    
