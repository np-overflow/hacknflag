FROM alpine
RUN apk add --no-cache gcc
RUN apk add --no-cache socat
RUN apk add libc-dev

WORKDIR /app
COPY . .

RUN gcc -o echo echo.c

EXPOSE 8080

CMD ["socat", "TCP4-LISTEN:8080,fork", "EXEC:/app/echo"]
