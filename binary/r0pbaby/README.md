# r0pbaby

Very simple ROP :D Have fun!

## Difficulty

⭐️⭐️⭐️⭐️

## Compilation

`gcc r0pbaby.c -o r0pbaby -fno-stack-protector`

## Writeup

See `solve.py`. It constructs and submits the malicious payload. The payload overrides the return pointer to call the `get_flag` function.

## Flag

`HNF{r0p_to_v1ct0ry}`

