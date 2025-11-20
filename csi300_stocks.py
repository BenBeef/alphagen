import akshare as ak
import pandas as pd

def get_csi300_stocks():
    """
    获取沪深300成分股数据
    返回: DataFrame包含股票代码、名称和纳入日期
    """
    try:
        # 获取沪深300成分股
        csi300_constituents = ak.index_stock_cons(symbol="000300")
        
        # 处理股票代码
        stock_codes = csi300_constituents["品种代码"].tolist()
        processed_codes = []
        
        for code in stock_codes:
            if code.startswith('6'):
                processed_codes.append(f"sh{code}")
            elif code.startswith(('0', '3')):
                processed_codes.append(f"sz{code}")
            else:
                processed_codes.append(code)
        
        print(f"沪深300成分股数量: {len(csi300_constituents)}")
        print("\n成分股列表:")
        # 设置显示选项
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', None)
        print(processed_codes)
            
        return processed_codes
        
    except Exception as e:
        print(f"获取数据时发生错误: {e}")
        return None

if __name__ == "__main__":
    get_csi300_stocks() 