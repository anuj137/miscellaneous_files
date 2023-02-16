#!/usr/bin/python

### Program to check the usage of MPI in multiple nodes.
# To run on multiple nodes, the program will have to be submitted in accordance with the cluster. 
# Code returns Size, Rank and Node name for each processor. Also, returns total number of cores requested, which should be equal to #nodes x #cores_per_node.

import numpy as np

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
nodename = MPI.Get_processor_name() 

print('(rank, size, nodename): ({}, {}, {})'.format(rank, size, nodename))

comm.Barrier()

x=1
sum_all_xs = comm.reduce(x)
if rank==0:
	print('\nTotal cpu requested (machine_count x request_cpus): ', sum_all_xs)

