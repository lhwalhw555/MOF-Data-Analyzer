import xml.etree.ElementTree as ET
import pandas as pd
import re

def parse_endnote_xml(xml_path, output_csv="mof_literature_summary.csv"):
    """
    解析 EndNote 导出的 XML 文件，提取 MOF 相关文献的标题、年份、摘要，
    并尝试使用正则提取关键的合成参数或表征数据。
    """
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        records = []
        # 遍历所有文献记录
        for record in root.findall('.//record'):
            title = record.find('.//titles/title/style')
            year = record.find('.//dates/year/style')
            abstract = record.find('.//abstract/style')
            
            title_text = title.text if title is not None else ""
            year_text = year.text if year is not None else ""
            abstract_text = abstract.text if abstract is not None else ""
            
            # 简单的正则匹配：尝试从摘要中提取 BET 比表面积数值
            bet_match = re.search(r'BET\s+surface\s+area.*?(\d+[\.\d]*)\s*m2/g', abstract_text, re.IGNORECASE)
            bet_area = bet_match.group(1) if bet_match else "N/A"
            
            # 标记是否涉及特定的材料或工艺
            is_monolith = "Yes" if re.search(r'monolith|monolithic', abstract_text, re.IGNORECASE) else "No"
            
            records.append({
                "Year": year_text,
                "Title": title_text,
                "Is_Monolithic": is_monolith,
                "BET_Surface_Area_m2/g": bet_area,
                "Abstract_Snippet": abstract_text[:150] + "..." if abstract_text else ""
            })
            
        df = pd.DataFrame(records)
        df.to_csv(output_csv, index=False, encoding='utf-8-sig')
        print(f"✅ 成功解析 {len(df)} 篇文献，结果已保存至 {output_csv}")
        
    except Exception as e:
        print(f"❌ 解析失败，请检查 XML 文件路径和格式: {e}")

if __name__ == "__main__":
    # 使用说明：在 EndNote 中选择目标文献 -> 导出 -> 格式选择 XML
    # parse_endnote_xml("../data/My_MOF_Library.xml")
    print("EndNote XML 解析器已加载。")
