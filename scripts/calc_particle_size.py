import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_size_distribution(sizes, mof_name="ZIF-67"):
    """
    根据 SEM 测量的纳米颗粒直径列表，绘制粒径分布直方图及拟合曲线
    """
    plt.figure(figsize=(8, 6))
    
    # 绘制直方图
    counts, bins, patches = plt.hist(sizes, bins=15, density=True, alpha=0.6, color='seagreen', edgecolor='black')
    
    # 高斯曲线拟合
    mu, std = norm.fit(sizes)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2, label=f'Fit: $\mu$={mu:.1f} nm, $\sigma$={std:.1f}')
    
    # 图表美化
    plt.xlabel('Particle Size (nm)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.title(f'Particle Size Distribution of {mof_name}', fontsize=16)
    plt.legend()
    
    plt.savefig(f'{mof_name}_Size_Distribution.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    # 模拟一组溶剂热合成的 ZIF-67 粒径数据 (单位: nm)
    mock_sizes = np.random.normal(loc=450.0, scale=30.0, size=100)
    plot_size_distribution(mock_sizes)
