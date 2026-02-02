#!/bin/bash

mkdir tempdir
mkdir tempdir/node_modules
mkdir tempdir/public
mkdir tempdir/views
cp app.js tempdir/.
cp -r node_modules/* tempdir/node_modules/.
cp -r public/* tempdir/public/.
cp -r views/* tempdir/views/.
echo "FROM node:18" > tempdir/Dockerfile
echo "WORKDIR /home/veera/DevopsCa2/PhoenixRoyale" >> tempdir/Dockerfile
echo "COPY ./node_modules ./node_modules" >> tempdir/Dockerfile
echo "COPY ./public ./public" >> tempdir/Dockerfile
echo "COPY ./views ./views" >> tempdir/Dockerfile
echo "COPY app.js ./app.js" >> tempdir/Dockerfile
echo "EXPOSE 3000" >> tempdir/Dockerfile
echo 'CMD ["node","app.js"]' >> tempdir/Dockerfile
cd tempdir
docker build -t phoenixroyaledocker .
docker run -t -d -p 8080:3000 \
  -v /home/veera/DevopsCa2/PhoenixRoyale/public/images:/home/veera/DevopsCa2/PhoenixRoyale/public/images \
  --name phoenixroyalerunning phoenixroyaledocker
docker ps -a
