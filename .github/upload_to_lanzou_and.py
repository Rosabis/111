import os
import glob
from lanzou.api import LanZouCloud

def main():
    # 初始化蓝奏云客户端
    lz = LanZouCloud()
    
    # 登录方式一：使用 Cookie（推荐，更稳定）
    cookie = os.getenv('LANZOU_COOKIE')
    if cookie:
        print("使用 Cookie 登录...")
        # 注意：根据 lanzou-api 版本，可能需要调整 Cookie 格式
        lz.login_by_cookie(cookie)
    else:
        # 登录方式二：使用用户名密码（可能不稳定）
        username = os.getenv('LANZOU_USERNAME')
        password = os.getenv('LANZOU_PASSWORD')
        if username and password:
            print("使用用户名密码登录...")
            login_success = lz.login(username, password)
            if not login_success:
                print("登录失败！")
                return
        else:
            print("未设置登录凭据！")
            return
    
    # 查找所有 APK 文件
    apk_files = glob.glob("**/*.apk", recursive=True)
    
    if not apk_files:
        print("未找到 APK 文件")
        return
    
    print(f"找到 {len(apk_files)} 个 APK 文件:")
    for apk in apk_files:
        print(f"  - {apk} ({os.path.getsize(apk) / (1024*1024):.2f} MB)")
    
    # 上传每个 APK 文件
    success_count = 0
    for apk_file in apk_files:
        print(f"\n正在上传 {apk_file}...")
        
        try:
            # 上传到蓝奏云根目录
            # folder_id=-1 表示根目录
            code = lz.upload_file(apk_file, folder_id=-1)
            
            if code == 0:  # 上传成功
                print(f"✓ 成功上传: {apk_file}")
                success_count += 1
            else:
                print(f"✗ 上传失败 {apk_file}, 错误码: {code}")
                
        except Exception as e:
            print(f"✗ 上传异常 {apk_file}: {str(e)}")
    
    print(f"\n上传完成: {success_count}/{len(apk_files)} 个文件上传成功")

if __name__ == '__main__':
    main()