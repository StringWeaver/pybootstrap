import os
import venv
import subprocess
def activate_venv(venv_dir,python_bin):
    """ 创建虚拟环境 """
    if not os.path.exists(venv_dir):
        print(f"创建虚拟环境: {venv_dir}")
        venv.create(venv_dir, with_pip=True)
    else:
        print(f"虚拟环境已经存在: {venv_dir}")
        subprocess.run([python_bin,'-m','ensurepip'])
def install_deps(python_bin):
    print('在虚拟环境中安装依赖...')
    subprocess.run([python_bin,'-m','pip','install','-r', 'requirements.txt', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'])
if __name__ == "__main__":
    workdir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(workdir)
    python_bin = os.path.join(workdir,'pyvenv','bin','python')
    activate_venv('pyvenv',python_bin)
    install_deps(python_bin)
    subprocess.run([python_bin,'main.py'])
    subprocess.run([python_bin, 'app.py'])
