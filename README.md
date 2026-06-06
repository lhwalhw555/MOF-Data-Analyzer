# MOF-Data-Analyzer
开源的材料科学数据处理脚本库。提供 Python 脚本用于快速解析、批量处理及可视化 BET 氮气吸脱附曲线、SEM 粒径分布等表征数据（以 ZIF-8 / ZIF-67 为例）
# MOF数据分析仪 (MOF Data Analyzer) 🔬

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

开源的材料科学数据处理脚本库。提供 Python 脚本用于快速解析、批量处理及可视化 BET 氮气吸脱附曲线、SEM 粒径分布等表征数据。本项目以整体式 ZIF-8 及 ZIF-67 的溶剂热合成体系为例进行演示。

## ✨ 核心功能

*   **BET 数据可视化**: 自动解析物理吸附仪导出的 CSV 数据，绘制标准的氮气吸脱附等温线，支持多组分（如不同合成时间的 ZIF-8 批次）对比。
*   **SEM 粒径统计**: 辅助处理 SEM 图像测量数据，生成粒径分布直方图并自动拟合高斯分布曲线。
*   **格式化输出**: 一键导出符合学术期刊排版要求的高分辨率（300 dpi）图片。

## 📂 目录说明

*   `scripts/` : 存放核心 Python 脚本
*   `examples/` : 存放脱敏的演示数据（如 `.csv` 格式的孔径数据）
*   `results/` : 脚本自动生成的高清图表输出目录

## 🚀 使用方法

```bash
# 运行 BET 绘图脚本示例
python scripts/plot_bet.py --input examples/zif8_isotherm.csv
