import torch

print(torch.cuda.device_count())
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
X_train = torch.FloatTensor([0., 1., 2.])
X_train = X_train.cuda()
print(X_train)
