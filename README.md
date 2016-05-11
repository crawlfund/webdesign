1.如果你使用 Mac OS X 或 Linux ，那么可以使用下面两条命令中任意一条:
  
  $ sudo easy_install virtualenv
  
  或更高级的:
  
  $ sudo pip install virtualenv

2.上述命令中的任意一条就可以安装好 virtualenv 。也可以使用软件包管理器，在 Ubuntu 系统中可以试试:

  $ sudo apt-get install python-virtualenv
3.进入webpage文件夹,现在，每次需要使用项目时，必须先激活相应的环境。在 OS X 和 Linux 系统中运行:
  
  $ . venv/bin/activate
4.现在可以开始在你的 virtualenv 中安装 Flask 了:

  $ pip install Flask

5.进入pages文件夹,运行helloworld
  
  $ python index.py
  
