from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

filter_fn = lambda x: x % 2 == 0

if rank == 0:
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Split up data into consecutive workloads for each process
    len_data = len(data)
    workloads = [[] for _ in range(size)]
    num_items_per_workload = len_data // size
    if len_data % size:
        num_items_per_workload += 1
    i = 0
    for workload in workloads:
        num_in_workload = 0
        while num_in_workload < num_items_per_workload and i < len_data:
            workload.append(data[i])
            num_in_workload += 1
            i += 1
else:
    workloads = []

#Scatter
workload = comm.scatter(workloads, root=0)
print("rank", rank, "received", workload)
workload = [item for item in workload if filter_fn(item)]

#Gather
workloads = comm.gather(workload, root=0)

comm.Barrier()

if rank == 0:
    filtered_data = []
    for workload in workloads:
        filtered_data += workload
    print(filtered_data)
