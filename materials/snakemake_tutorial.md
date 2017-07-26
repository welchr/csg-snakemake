## Tutorial notes

These notes use the Snakefile under `example-tutorial`. 

1. Walk through the Snakefile components

2. How do we see what snakemake is going to do?

  ```bash
  # -p for show commands
  # -n for don't do anything (dry run)
  snakemake -pn
  ```

  Alternatively:

  ```bash
  alias snakemake-summary="snakemake --summary | column -t -s $'\t'"
  snakemake-summary
  ```

  Graphically:

  ```bash
  snakemake --dag | dot -Tpdf > dag.pdf
  open dag.pdf # on MacOS
  ```

3. Show running a single rule

  ```bash
  snakemake create_data
  snakemake-summary
  ls -l
  ```

4. Show running the entire snakefile

  ```bash
  snakemake -p
  ```

5. Show cleaning

  ```bash
  alias snakemake-clean="rm -f $(snakemake --summary | tail -n+2 | cut -f1)"
  snakemake-clean
  ```

6. What happens if an input file is modified?

  1. Modify `gene_data_normalized_chr1.tab`
  2. Re-run `snakemake -pn` to show what will change
  3. Re-run `snakemake-summary` to show what files will change

7. Show what happens if you cancel in the middle of a computation

  ```bash
  # Modify cov.py to include sleep command to make jobs wait
  snakemake -p
  # wait until covariance
  # then CTRL+C
  # covar_chrom*tab files will be deleted by Snakemake
  ```

8. Some of the tasks could actually be run in parallel

  ```bash
  snakemake -j 5 -p
  ```

9. What if we want to run tasks in parallel but on the cluster?

  1. Show the cluster.yaml file
  2. Show the `--cluster` method of running snakemake

    ```bash
    snakemake --cluster-config cluster.yaml --cluster "sbatch --time {cluster.time} --mem {cluster.mem} --cpus-per-task {cluster.cpus}" -j 99
    ```

10. What if we only want to run some rules on the cluster, others locally?

  ```
  # Add this to Snakefile
  localrules: split
  ```

  Now execute `run_cluster.sh`
