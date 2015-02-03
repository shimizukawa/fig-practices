FROM ubuntu:14.04
MAINTAINER Takayuki Shimizukawa shimizukawa@gmail.com

# environment
ENV DEBIAN_FRONTEND noninteractive

# update, curl
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install curl libcurl4-openssl-dev ruby ruby-dev make && apt-get clean

# install fluentd
RUN curl -L http://toolbelt.treasuredata.com/sh/install-ubuntu-trusty-td-agent2.sh | sh

# install fluentd plugins
RUN /opt/td-agent/embedded/bin/fluent-gem install --no-ri --no-rdoc \
    fluent-plugin-elasticsearch \
    fluent-plugin-record-modifier \
    fluent-plugin-exclude-filter


# add conf
ADD ./etc/fluentd /etc/fluentd

CMD /etc/init.d/td-agent stop && /opt/td-agent/embedded/bin/fluentd -c /etc/fluentd/fluent.conf
