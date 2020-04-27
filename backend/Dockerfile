FROM python:3.6.2

#for bjoern
#RUN apt-get update && apt-get install -y libev-dev

COPY start.sh /scripts/start.sh
EXPOSE 8001

WORKDIR /app
ENTRYPOINT ["/scripts/start.sh"]