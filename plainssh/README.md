# Plain SSH

A patched OpenSSH v6.8 server that supports (forces) the none cipher a.k.a. plaintext transmission.

# Building

OpenSSH does not support OpenSSL v1.1.1 yet, so we need some older version:

```bash
git clone git@github.com:openssl/openssl.git
cd openssl
git checkout OpenSSL_1_0_2-stable
./config
make -j4
```

After this we can build OpenSSH v6.8 with our own OpenSSL version (path for `--with-ssl-dir` has to be adjusted):

```bash
git clone git@github.com:openssh/openssh-portable.git
cd openssh-portable
git checkput V_6_8
git apply openssh_v6.8_none_cipher.patch
./configure --with-ssl-engine --with-ssl-dir=git/openssl
make -j4
```

# Running

Force the none cipher with sshd:

```bash
./sshd -o Ciphers=none
```