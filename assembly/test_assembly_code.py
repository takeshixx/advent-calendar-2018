from keystone import *
from keystone import KsError
import sys

CODE = sys.argv[1]

ks = Ks(KS_ARCH_X86, KS_MODE_32)
encoding, count = ks.asm(CODE)
print("%s = %s (number of statements: %u)" %(CODE, encoding, count))
