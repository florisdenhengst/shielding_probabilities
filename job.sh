#!/bin/bash

module load pre2019
module load stopos
module load python/3.5.0

stopos_run="sim_run"
dirname="shielding_probabilities"

source ~/venvs/sim_probabilities/bin/activate

stopos next -p $stopos_run
rm -rf ${dirname}
cp ~/projects/${dirname} .
cd ${dirname}
python simulate.py $STOPOS_VALUE

