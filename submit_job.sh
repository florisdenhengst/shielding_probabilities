#!/bin/bash

module load pre2019
module load stopos

#SBATCH -e slurm-%j.err
#SBATCH -o slurm-%j.out

NR_NODES=0
sbatch -a 0-$NR_NODES ./job.sh
