#!/bin/sh

# install fig
echo installing fig
curl --progress-bar -q https://bootstrap.pypa.io/get-pip.py | sudo python
sudo pip install -q -U fig

