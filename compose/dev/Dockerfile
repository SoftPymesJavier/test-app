FROM python:3.5-alpine

LABEL maintainer="lmosquera@softpymes.com.co"

RUN apk update \ 
    && apk add tzdata git \
    && mkdir -p /app/

COPY ./requirements.txt /app/requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps build-base \
    && easy_install distribute \
    && pip install --upgrade pip \
    && pip install -U pip \
    && pip install -r /app/requirements.txt \
    && apk del .build-deps \
    && rm -fr /app/requirements.txt

COPY ./compose/dev/entrypoint /
RUN chmod +x /entrypoint

COPY ./compose/dev/start /
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]

CMD ["/start"]