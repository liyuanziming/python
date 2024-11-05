本地目录里初始化一个仓库：
git init

本地目录的文件添加到仓库中：
git add *.c
git add LICENSE

git commit -m "Initial project version"

#上段代码将本地目录里的文件提交至本地仓库Git里。

克隆已经存在的仓库:
git clone url

查看本地git状态：
git status
文件没有变更，并且已经被add后，处于tracked状态,需要被提交:

