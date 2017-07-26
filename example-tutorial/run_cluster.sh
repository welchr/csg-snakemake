#!/bin/bash
snakemake --cluster-config cluster.yaml --cluster "sbatch --time {cluster.time} --mem {cluster.mem} --cpus-per-task {cluster.cpus}" -j 99
