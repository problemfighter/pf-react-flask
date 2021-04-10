#!/bin/bash

echo "Updating npm";
npm install -g npm

echo "Installing yarn";
npm install -g yarn

echo "Installing Lerna";
npm i -D lerna

echo "Installing Dependency";
yarn install