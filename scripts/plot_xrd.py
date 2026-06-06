import pandas as pd
import matplotlib.pyplot as plt

def plot_xrd(file_path, mof_name="MonoZIF-8"):
    """
    绘制 MOF 材料的 XRD 衍射图谱
    要求输入 CSV 包含两列: 2Theta (角度), Intensity (强度)
    """
    try:
        data = pd.read_csv(file_path)
        
        plt.figure(figsize=(8, 5))
        # 绘制 XRD 曲线
        plt.plot(data['2Theta'], data['Intensity'], color='black', linewidth=1.2)
        
        # 学术图表美化
        plt.xlabel('2$\\theta$ (degree)', fontsize=14, fontweight='bold')
        plt.ylabel('Intensity (a.u.)', fontsize=14, fontweight='bold')
        plt.title(f'XRD Pattern of {mof_name}', fontsize=16)
        
        # XRD 通常不需要显示 Y 轴的具体数值，隐藏 Y 轴刻度
        plt.yticks([])
        plt.xlim(data['2Theta'].min(), data['2Theta'].max())
        plt.tick_params(direction='in', bottom=True, top=True)
        
        # 保存图片
        output_filename = f'{mof_name}_XRD_Pattern.png'
        plt.savefig(output_filename, dpi=300, bbox_inches='tight')
        print(f"XRD 绘图完成，已保存为 {output_filename}！")
        plt.show()
        
    except Exception as e:
        print(f"读取或绘图出错: {e}")

if __name__ == "__main__":
    # 测试代码
    # plot_xrd("your_xrd_data.csv", "ZIF-8")
    print("XRD 分析脚本已就绪。")
