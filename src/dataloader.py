from torch.utils.data import DataLoader, Subset
from dataset import NumberDataset

def get_number_dataloaders(train_ratio: int=8, val_ratio: int = 1, test_ratio = 1, batch_size: int = 4, shuffle: bool = True):
    dataset = NumberDataset(shuffle=shuffle)
    train_slice = (train_ratio + val_ratio + test_ratio)/train_ratio
    val_slice = (train_ratio + val_ratio + test_ratio)/val_ratio
    test_slice = (train_ratio + val_ratio + test_ratio)/test_ratio
    
    indices = []

    for i in range(len(dataset)):
        indices.append(i)

    train_range = int(train_slice*len(dataset))
    val_range = int(val_slice*len(dataset))
    test_range = int(test_slice*len(dataset))


    train_indices = indices[:train_range]
    val_indices = indices[train_range:train_range+val_range]
    test_indices = indices[train_range+val_range:train_range+val_range+test_range]

    train_set = Subset(dataset, train_indices)
    val_set = Subset(dataset, val_indices)
    test_set = Subset(dataset, test_indices)

    train_loader = DataLoader(train_set, batch_size=batch_size)
    val_loader = DataLoader(val_set, batch_size=batch_size)
    test_loader = DataLoader(test_set, batch_size=batch_size)

    return train_loader, val_loader, test_loader