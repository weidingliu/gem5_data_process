#!/bin/bash

GEM5_DIR=~/gem5-rvv
OUTPUT_DIR=./m5out
TEST_DIR=~/riscv-vector-tests/out/v256x64user/bin/stage2
MAX_THREADS=8

BOOM_FLAGS="--cpu-type=RiscvO3CPU \
--bp-type=BiModeBP \
--caches \
--l2cache \
--cacheline=64 \
--num-l2cache=1 \
--l1i_size=16kB \
--l1i_assoc=4 \
--l1d_size=16kB \
--l1d_assoc=4 \
--l2_size=256kB \
--l2_assoc=4 \
--mem-size=8192MB \
--warmup-insts=10000000 \
-I 300000000"

if [ ! -e "./generates/fd_hyc" ]; then 
    mkfifo ./generates/fd_hyc 
fi 
if [ ! -e "./generates/filelist" ]; then 
    find $TEST_DIR/ -name 'vl*' -o -name 'vs*' -printf '%f\n' \
    | grep -v 'vslid*' | grep -v 'vssra*' | grep -v 'vset*' |    grep -v 'vsll*' | grep -v 'vsrl*' \
    | grep -v 'vssub*' | grep -v 'vsadd*' | grep -v 'vsub*' | grep -v 'vsbc*' | grep -v 'vsmul*' > ./generates/filelist
fi

exec 3<>./generates/fd_hyc

rm -rf ./generates/fd_hyc

for ((i=1;i<$MAX_THREADS;i++))
do 
    echo >&3
done

for file in $(cat generates/filelist)
do 
    read -u3
    (
    mkdir -p $OUTPUT_DIR/$file
    $GEM5_DIR/build/RISCV/gem5.opt --outdir=$OUTPUT_DIR/$file \
     $GEM5_DIR/configs/deprecated/example/se.py \
     $BOOM_FLAGS \
     --cmd $TEST_DIR/$file
    echo >&3
    )&
done
wait
exec 3>&-