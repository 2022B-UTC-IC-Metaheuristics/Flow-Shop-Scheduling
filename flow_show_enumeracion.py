import numpy as np
from itertools import permutations

def flow_shop_scheduling(n_jobs, n_machines, processing_times):
    # Initialize completion times and order of jobs for each machine
    completion_times = np.zeros((n_jobs, n_machines))
    job_order = np.zeros((n_jobs, n_machines), dtype=np.int32)

    # Initialize the starting time for the first job on each machine
    start_times = np.zeros(n_machines)

    # Loop through each job
    for i in range(n_jobs):
        # Loop through each machine
        for j in range(n_machines):
            # If it's the first machine, start the job at time 0
            if j == 0:
                start_times[j] = completion_times[i-1,j] if i > 0 else 0
            else:
                start_times[j] = max(completion_times[i,j-1], completion_times[i-1,j])
            # Update completion time and job order for the job on the current machine
            completion_times[i,j] = start_times[j] + processing_times[i,j]
            job_order[i,j] = i

    # Get the order of jobs by sorting them based on their completion time on the last machine
    last_machine_times = completion_times[:, -1]
    job_order = job_order[np.argsort(last_machine_times)]

    # Return the completion time of the last job on the last machine and the order of jobs
    return completion_times[-1,-1], job_order.tolist()

# Example usage
n_jobs = 5
n_machines = 4
#processing_times = np.array([[5,10,6,8], [8,15,5,7], [8,5,7,9]])
processing_times = np.array([[5,4,4,3],[5,4,4,6],[3,2,3,3],[6,4,4,2], [3,4,1,5]])

# Generate all possible permutations of job order
job_orders = permutations(range(n_jobs))

# Initialize minimum completion time and optimal job order
min_completion_time = np.inf
print(min_completion_time)
optimal_job_order = None

# Test each permutation of job order and update optimal solution if a better one is found
for job_order in job_orders:
    processing_times_perm = processing_times[job_order,:]
    completion_time, _ = flow_shop_scheduling(n_jobs, n_machines, processing_times_perm)
    if completion_time < min_completion_time:
        min_completion_time = completion_time
        optimal_job_order = list(job_order)

# Print the optimal completion time and job order
print("Optimal completion time:", min_completion_time)
print("Optimal job order:", optimal_job_order)
