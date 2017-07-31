#!/bin/bash

# This command uses `srun` and is probably best for smaller numbers of jobs (thousands or less?)
# You may also want to include "--keep-going" to make snakemake continue with as many independent tasks as possible even if some of the current jobs fail
snakemake --cluster-config cluster.yaml --cluster-sync "srun --time {cluster.time} --mem {cluster.mem} --cpus-per-task {cluster.cpus}" -j 99 --keep-going

# This might be better for larger numbers of jobs (it submits them using sbatch)
# But unfortunately it will not cancel your jobs if you hit CTRL+C, or know that your job failed if SLURM cancels it due to time limit, etc. 
snakemake --cluster-config cluster.yaml --cluster "sbatch --time {cluster.time} --mem {cluster.mem} --cpus-per-task {cluster.cpus}" -j 99
