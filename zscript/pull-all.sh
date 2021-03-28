#!/bin/bash

cd /home/v-host/api-goods-mama.problemfighter.com/application
source venv/bin/activate
python zscript/clone-pull.py
systemctl restart httpd