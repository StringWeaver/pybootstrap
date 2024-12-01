if __name__ == "__main__":
    try:
        # 尝试导入 requests，检查是否安装成功
        import requests
        print(f"requests 库已安装！版本：{requests.__version__}")
    except ImportError:
        print("requests 库未安装！")