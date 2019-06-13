import torch
print('Construct a 5x3 matrix, uninitialized:')
x = torch.empty(5, 3)
print(x)

# 设置随机种子
torch.manual_seed('2019')
x = torch.rand(5, 3)
print(x)

print('Construct a matrix filled zeros and of dtype long:')
x = torch.zeros(5, 3, dtype=torch.long)
print(x)
print('Construct a tensor directly from data:')
x = torch.tensor([5.5, 3])
print(x)

print(' create a tensor based on an existing tensor:')
x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
print(x)
print(' override dtype!result has the same size:')
x = torch.randn_like(x, dtype=torch.float)    
print(x)
print('Get its size:')
print(x.size())

print('Operations Addition,1:')
y = torch.rand(5, 3)
print(x + y)
print('Operations Addition,2:')
print(torch.add(x, y))