import torch

torch.cuda.device_count()
torch.cuda.is_available()
torch.cuda.get_device_name(0)
X_train = torch.FloatTensor([0., 1., 2.])
X_train = X_train.cuda() 

print(X_train)
