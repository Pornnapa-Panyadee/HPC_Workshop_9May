#!/bin/bash
#SBATCH --gpus=1                # total number of GPUs
#SBATCH -w compute2
#SBATCH --job-name=qegpu     # create a short name for your job
#SBATCH -p gpu                  # specific partition (compute, memory, gpu)
#SBATCH -o qe.%j.out          # Name of stdout output file (%j expands to jobId)
#SBATCH --ntasks=1            # number of tasks per node
#SBATCH --time=05:00:00

singularity run --nv /opt/ohpc/pub/apps/singularity/quantum_espresso_qe-7.1.sif mpirun pw.x -inp input.in > output.out
