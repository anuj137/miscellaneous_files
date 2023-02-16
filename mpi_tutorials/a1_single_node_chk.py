#!/usr/bin/python

### Program to check the usage of MPI in a single node.
# Run on terminal using: mpiexec -n N python -m mpi4py test_mpi_1.py;
# where N is the total number of processors to use.
# Code returns Size and Rank for each processor. Size=N, whereas rank is an integer varying from (0, N-1).

import numpy as np

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print('(rank, size): ({}, {})'.format(rank, size))
