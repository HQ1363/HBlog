# use base python image with python 2.7
FROM python:2.7

# statement the author about image
MAINTAINER HQ huangqiang1363@outlook.com

# settings label
LABEL version=1.0 description="blog web server"

# statement the timezone
ENV TZ "Asia/Shanghai"

# new add user
RUN useradd devops -m -d /home/devops -s /sbin/nologin && mkdir -p /data/HBlog

# add project to the image
ADD . /data/HBlog/

# change the owner
RUN chown -R devops.devops /data/HBlog

# install python dependencies
RUN cd /data/HBlog && pip install -i http://pypi.douban.com/simple -r requirements/dev.txt --trusted-host pypi.douban.com

# direct the docker container user
USER devops

# set working directory to /data/polestar
WORKDIR /data/HBlog

# db migrate
RUN python manage.py makemigrations && python manage.py migrate

# direct the mount volume
VOLUME ["/data/logs/blog"]

# listen port
EXPOSE 8000

# execute command
CMD ["/bin/bash", "-c", "cd /data/HBlog && python manage.py runserver 0.0.0.0:8000"]
