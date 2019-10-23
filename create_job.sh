#!/bin/bash

module load pre2019
module load stopos

sim_run="sim_run"

stopos purge -p $sim_run
stopos create -p $sim_run
stopos add parmset -p $sim_run
