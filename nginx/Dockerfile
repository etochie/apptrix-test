FROM python:3.7-slim AS server

RUN mkdir /main
WORKDIR /main

COPY ./main/requirements.txt /main
RUN pip install -r requirements.txt

COPY ./main /main

RUN python ./manage.py collectstatic --noinput

#########################################

FROM nginx:1.13

RUN rm -v /etc/nginx/nginx.conf
COPY ./nginx/nginx.conf /etc/nginx/

RUN mkdir /nginx
COPY --from=server /main/staticfiles /nginx/static
