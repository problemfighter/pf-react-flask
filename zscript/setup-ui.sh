#!/bin/bash

echo "Installing yarn";
npm install -g yarn

echo "Installing Lerna";
npm i -D lerna

lerna clean

echo "Installing Dependency";
yarn install