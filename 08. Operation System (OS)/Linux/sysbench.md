```bash
# CPU
sysbench cpu run

# RAM
sysbench memory run

# File IO
sysbench fileio --threads=16 --file-total-size=2G --file-test-mode=rndrw prepare

# Threads
sysbench threads --threads=16 --thread-yields=1000 --thread-locks=8 run
```