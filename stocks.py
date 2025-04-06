import numpy as np

def stock_simulation(T, dt, t, mu, sigma, R, S0):
    """
    Function to simulate a stock price using the Geometric Brownian Motion model.
    """
    N = int(T/dt)  # Number of time steps
    L = np.linalg.cholesky(R)
    # 先生成4个独立的布朗运动
    stepwise_brownians = [np.cumsum(np.random.choice([-1,1],size=(N)) *dt),
                        np.cumsum(np.random.choice([-1,1],size=(N)) *dt),
                        np.cumsum(np.random.choice([-1,1],size=(N)) *dt),
                        np.cumsum(np.random.choice([-1,1],size=(N)) *dt)]
    stepwise_brownians = np.vstack(stepwise_brownians)

    # 使用相关性矩阵的correlation matrix点乘独立的布朗运动来获得相关的布朗运动
    correlated_brownians = np.dot(L, stepwise_brownians)


    # 几何布朗运动模拟
    S=np.zeros((4, N))
    S[:, 0]=S0  # 初始价格

    for i in range(1, N):
        drift=(mu-0.5*sigma**2)*dt  # 漂移项
        diffusion = sigma * (correlated_brownians[:, i] - correlated_brownians[:, i-1])  # 扩散项
        S[:, i] = S[:, i-1] * np.exp(drift+diffusion)
    
    return S