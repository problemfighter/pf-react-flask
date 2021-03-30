#!/bin/bash

GIT_PATH="$(which git)"
export git_path="$GIT_PATH"
source venv/Scripts/activate
python zscript/clone-pull.py