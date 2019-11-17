## HBlog
> 旨在提供开箱即用的个人博客系统，深度定制化，敬请期待。

## 技术栈
- `Python`
- `Django`
- `Django Rest Framework`

## 开发规范
- `添加文件和更新内容时, 注意项目结构, 相同概念的东西放到一起, DRY`
- `请严格遵循pep8代码规范`

## 贡献代码

1、本地安装好`Redis`和`Mysql`
```
   yum install mysql -y
```
2、安装隔离的虚拟环境和代码规约
```
  virtualenv .venv
  source .venv/bin/activate
  make setup-pre-commit-hook
  make install
```
3、创建数据库和表
```
  make mysql
```
4、启动服务
```
  python manage.py runserver 0.0.0.0:8000
  python manage.py celeryd -l info
  python manage.py celery beat
```
5、提交代码
```
  fork一份代码至自己的仓库   
  从远程origin仓库git clone一份至本地   
  git remote add <your-repository-name> <your-address>   
  git checkout -b develop   
  每次要提交代码时, 请git pull || git fetch origin master && git rebase origin/master   
  没有冲突或解决好冲突后, 提交代码至远程自己的分支，确认无误后从自己仓库合并到lightmerge分支   
  lightmerge在dev环境测试验收通过后，提合master的MR   
```
