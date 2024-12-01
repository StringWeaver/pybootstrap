import os
import venv
import subprocess
def create_activate_venv(venv_dir):
    """ 创建虚拟环境 """
    if not os.path.exists(venv_dir):
        print(f"创建虚拟环境: {venv_dir}")
        venv.create(venv_dir, with_pip=True)
    else:
        print(f"虚拟环境已经存在: {venv_dir}")
def install(python_bin,requirement_file_path):
    print('在虚拟环境中安装依赖...')
    process = subprocess.Popen([python_bin,'-m','pip','install','-r', requirement_file_path])
    process.wait()
if __name__ == "__main__":
    workdir = os.path.dirname(os.path.abspath(__file__))
    venv_dir = os.path.join(workdir,'pyvenv') 
    create_activate_venv(venv_dir)
    venv_python_bin = os.path.join(venv_dir, 'bin','python')
    requirement_file_path = os.path.join(workdir,'requirements.txt')
    install(venv_python_bin,requirement_file_path)
    main_path = os.path.join(workdir,'main.py') 
    process = subprocess.Popen([venv_python_bin,main_path])
    process.wait()