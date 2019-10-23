#!/bin/bash
#SBATCH -t 99:00:00
#SBATCH -N 1
#SBATCH --mail-user=florisdenhengst@gmail.com
#SBATCH --mail-type=ALL

module load pre2019
module load stopos
module load python/3.5.0

stopos_run="sim_run"
dirname="shielding_probabilities"

source ~/venvs/sim_probabilities/bin/activate

cd ${TMPDIR}

rm -rf ${dirname}
cp -r ~/projects/${dirname} .
cd ${dirname}

stopos next -p $stopos_run
python simulate.py $STOPOS_VALUE

