if __name__ == "__main__":
    try:
        # 尝试导入 ，检查是否安装成功
        import panel
        print(f"panel 库已安装！")
    except ImportError:
        print("panel 库未安装！")