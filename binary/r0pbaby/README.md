# r0pbaby

Very simple ROP :D Have fun!

## Difficulty

⭐️⭐️⭐️⭐️

## Compilation

`gcc -no-pie -m32 -fno-stack-protector -z execstack -o r0pbaby r0pbaby.c`

## Writeup

See `solve.py`. It constructs and submits the malicious payload. The payload overrides the return pointer to call the `get_flag` function.

## Flag

`HNF{r0p_to_v1ct0ry}`

