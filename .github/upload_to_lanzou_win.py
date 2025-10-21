import os
from lanzou.api import LanZouCloud

def main():
    # 初始化蓝奏云客户端
    lz = LanZouCloud()

    # 方式一：使用 Cookie 登录（推荐，因为用户名密码登录可能已失效:cite[1]）
    cookie = os.getenv('LANZOU_COOKIE')
    if cookie:
        # 注意：lanzou-api 库的 Cookie 登录方式可能需要你将 Cookie 字符串解析为字典
        # 请根据 lanzou-api 的实际文档调整
        lz.login_by_cookie(cookie)
    else:
        # 方式二：使用用户名和密码登录（可能不稳定）
        username = os.getenv('LANZOU_USERNAME')
        password = os.getenv('LANZOU_PASSWORD')
        lz.login(username, password)

    # 设置要上传的文件路径和目标文件夹ID
    file_path = "111/artifacts/*.zip"  # 根据你实际的打包路径修改
    folder_id = -1  # -1 表示上传到根目录，也可以指定其他文件夹ID

    # 执行上传
    for file in [f for f in os.listdir("111/artifacts") if f.endswith('.zip')]:
        print(f"Uploading {file} to LanZouCloud...")
        code = lz.upload_file(file, folder_id)
        if code == 0:  # 上传成功
            print(f"Successfully uploaded {file} to LanZouCloud!")
        else:
            print(f"Upload {file} failed, error code: {code}")

if __name__ == '__main__':
    main()