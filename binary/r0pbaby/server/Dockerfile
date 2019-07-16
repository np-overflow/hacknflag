FROM alpine
RUN apk add --no-cache gcc
RUN apk add --no-cache socat
RUN apk add --no-cache libc-dev
RUN apk add --no-cache util-linux

WORKDIR /app
COPY . .

RUN gcc -no-pie -m32 -fno-stack-protector -z execstack -o r0pbaby r0pbaby.c

EXPOSE 8080

CMD ["socat", "TCP4-LISTEN:8080,fork", "EXEC:/app/exec.sh"]
