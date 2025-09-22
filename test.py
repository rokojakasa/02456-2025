import numpy as np

def data_generator(noise=0.1, n_samples=10, D1=True):
    
    X = np.linspace(-3, 3, num=n_samples).reshape(-1, 1) # 1-D
    np.random.shuffle(X)
    # y = np.random.normal((0.5*np.sin(X[:,0]*3) + X[:,0]), noise) # 1-D with trend
    
    return X

X = data_generator()
print(X)