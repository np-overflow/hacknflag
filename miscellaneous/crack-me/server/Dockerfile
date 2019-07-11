FROM python:2-alpine
RUN apk --no-cache add socat

WORKDIR /usr/src/app

COPY crack-me.py ./

EXPOSE 8080

CMD ["socat", "TCP4-LISTEN:8080,fork", "EXEC:/usr/src/app/crack-me.py"]
