#!/bin/bash

module load pre2019
module load stopos

NR_NODES=60
#NR_NODES=0
sbatch -a 0-$NR_NODES ./job.sh
