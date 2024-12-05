# 功能：Png圖片轉io.BytesIO(二進制)
# 轉換關鍵字：
## 檔案名稱
## PngToBytesIO
import io

def png_to_bytes_string(png_file_path):
    """將 PNG 文件轉換為字符串形式的字節數據，用於生成相同格式的輸出"""
    with open(png_file_path, "rb") as f:
        data = f.read()
    
    # 將字節數據轉換為字符串格式
    byte_string = ''.join(f'\\x{byte:02x}' for byte in data)
    return f"data = b'{byte_string}'"

def GetPngToBytesIOStream():
    # 替換為您的 PNG 文件路徑
    png_file_path = 'NekoNeko.png'  # 檔案名稱（放在和此程式同個資料夾內即可）
    byte_string = png_to_bytes_string(png_file_path)
    
    # Python 字符串過濾
    stream_code = f"""
def GetPngToBytesIOStream():
    {byte_string}
    stream = io.BytesIO(data)
    return stream
"""

    # 將生成的代碼寫入到一個文本文件
    with open('png代碼.py', 'w') as f:
        f.write(stream_code.strip())  # 移除前後的換行符

    print("生成的代碼已經寫入到 'png代碼.py' 文件中。")

# 測試函數
if __name__ == "__main__":
    GetPngToBytesIOStream()

# 執行程式碼：python PngToBytesIO