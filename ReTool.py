import pandas as pd
import os

def read_csv_data(file_path):
    """
    读取CSV文件并返回包含name和GitHubid的字典列表
    """
    try:
        df = pd.read_csv(file_path)
        return df[['Name', 'GitHubID']].to_dict(orient='records')
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

def rename_md_files(csv_data):
    """
    根据CSV数据重命名.md文件
    """
    if not csv_data:
        print("No CSV data available for renaming files.")
        return

    for item in csv_data:
        old_filename = f"{item['Name']}.md"
        new_filename = f"{item['GitHubID']}.md"
        
        if os.path.exists(old_filename):
            try:
                os.rename(old_filename, new_filename)
                print(f"Renamed {old_filename} to {new_filename}")
            except Exception as e:
                print(f"Error renaming {old_filename}: {e}")
        else:
            print(f"File not found: {old_filename}")

def main():
    # CSV文件路径
    csv_file_path = 'DeFi.csv'  # 请确保这是正确的CSV文件路径

    # 读取CSV文件
    csv_data = read_csv_data(csv_file_path)

    # 重命名文件
    if csv_data:
        rename_md_files(csv_data)
    else:
        print("Failed to read CSV data. File renaming process aborted.")

if __name__ == "__main__":
    main()