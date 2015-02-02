FROM shimizukawa/td-agent
MAINTAINER Takayuki Shimizukawa shimizukawa@gmail.com

RUN apt-key adv --keyserver pgp.mit.edu --recv-keys ABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >> /etc/apt/sources.list.d/nginx.list
RUN echo "deb-src http://nginx.org/packages/ubuntu/ trusty nginx" >> /etc/apt/sources.list.d/nginx.list

ENV NGINX_VERSION 1.6.2-1~trusty

RUN apt-get update && \
    apt-get install -y nginx=${NGINX_VERSION} && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME ["/var/cache/nginx"]

EXPOSE 80 443

CMD nginx && /etc/init.d/td-agent stop && /opt/td-agent/embedded/bin/fluentd -c /etc/fluentd/fluent.conf

