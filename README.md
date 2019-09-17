#Treinamento DevOps

#Docker the "hard" way

##Docker build

Para construir a imagem do app do Chuck Norris

```docker build --no-cache --tag sciensa-chuck-app:latest -f Dockerfile-chuck -t chuck-app .```

Para construir a imagem do Nginx 

```docker build --no-cache --tag sciensa-nginx:latest -f Dockerfile-nginx -t nginx .```

##Docker setup

Para criar a rede

``` docker network create sciensa-trainees```

##Docker run

 - Nginx:

``` docker run -d --name nginx --network sciensa-trainees -p 80:80 sciensa-nginx:latest ```

 - Chuck Norris app:

``` docker run -d --name chuck-app --network sciensa-trainees --expose 9667 sciensa-chuck-app:latest ```

#Docker nutella aka compose

Build:

``` docker-compose -p sciensa_tr build --no-cache --force-rm ```

Up:

``` docker-compose -p sciensa_tr up --detach --force-recreate --remove-orphans ```