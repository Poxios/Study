```bash
# CPU
sysbench cpu run

# RAM
sysbench memory run

# File IO
sysbench fileio --threads=16 --file-total-size=2G --file-test-mode=rndrw prepare
```