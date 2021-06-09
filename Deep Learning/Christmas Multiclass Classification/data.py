from torch.utils.data import Dataset


class ChristmasImages(Dataset):
    
    def __init__(self, path, training=True):
        super().__init__()
        self.training = training
        if self.training:
            self.path = os.path.join(path, 'train')
            print(self.path)
        else:
            dir = os.path.join(path, 'data')
            self.path = [f for f in os.listdir(dir) if os.path.splitext(f)[-1] == '.png']
        # If training == True, path contains subfolders
        # containing images of the corresponding classes
        # If training == False, path directly contains
        # the test images for testing the classifier
        
        
    def __getitem__(self, index):
        # If self.training == False, output (image, )
        # where image will be used as input for your model
        
        if self.training == False:
            img= self.path[index]
        return (img,)
            
            
