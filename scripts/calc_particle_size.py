import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_size_distribution_from_csv(file_path, size_column='Size(nm)', mof_name="ZIF-67"):
    """
    从 CSV 文件读取粒径数据并绘制分布图
    """
    try:
        # 读取包含粒径的 CSV (例如用 ImageJ 测量导出的数据)
        data = pd.read_csv(file_path)
        sizes = data[size_column].dropna() # 获取数据并去除空值
        
        plt.figure(figsize=(8, 6))
        
        # 绘制直方图
        counts, bins, patches = plt.hist(sizes, bins=20, density=True, alpha=0.6, color='royalblue', edgecolor='black')
        
        # 高斯曲线拟合
        mu, std = norm.fit(sizes)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        
        plt.plot(x, p, 'k', linewidth=2.5, label=f'Fit: $\mu$={mu:.1f} nm\n$\sigma$={std:.1f}')
        
        # 图表美化
        plt.xlabel('Particle Size (nm)', fontsize=14, fontweight='bold')
        plt.ylabel('Relative Frequency', fontsize=14, fontweight='bold')
        plt.title(f'Particle Size Distribution of {mof_name}', fontsize=16)
        plt.legend(frameon=False, fontsize=12)
        plt.tick_params(direction='in', right=True, top=True)
        
        plt.savefig(f'{mof_name}_Size_Distribution.png', dpi=300, bbox_inches='tight')
        print(f"粒径统计完成！平均粒径为 {mu:.1f} nm")
        plt.show()
        
    except Exception as e:
        print(f"数据读取失败，请检查 CSV 路径和列名 '{size_column}' 是否正确。错误信息: {e}")

if __name__ == "__main__":
    print("SEM 粒径分析脚本(CSV读取版)已就绪。")
