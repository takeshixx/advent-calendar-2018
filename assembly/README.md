# Assembly Service

A simple ([Assembly](assembly)) Service which requires to solve some arithmetic operations on bytecode basis. To solve the challenge, you can either do it by pushing the bytecode to a dissassembler or simply forwarding it to the unicorn engine to solve it automagic.

## Building & Running

```bash
docker build -t day16_assembly .
docker run -d --restart=always -p 16:16 --name=day16 day16_assembly
```
