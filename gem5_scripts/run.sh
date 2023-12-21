#!/bin/bash

GEM5_DIR=~/gem5-rvv

$GEM5_DIR/build/RISCV/gem5.opt $GEM5_DIR/configs/deprecated/example/se.py --cpu-type=RiscvO3CPU --caches --cmd ~/riscv-vector-tests/out/v256x64user/bin/stage2/vle8.v-0
