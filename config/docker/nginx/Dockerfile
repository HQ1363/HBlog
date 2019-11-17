FROM nginx

EXPOSE 80

RUN rm /etc/nginx/conf.d/default.conf
ADD blog.conf  /etc/nginx/conf.d/
RUN mkdir -p /usr/share/nginx/html/static
