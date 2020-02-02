FROM nginx:1.13
VOLUME /data

# Install ced
RUN apt update
RUN apt install -y python-pip
RUN pip install ced

COPY ./config/conf.templ /etc/nginx/conf.d/conf.templ
RUN ced -o /etc/nginx/conf.d/conf -d £ /etc/nginx/conf.d/conf.templ

