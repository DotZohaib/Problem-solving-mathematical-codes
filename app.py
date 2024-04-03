# Question:1

def calculate_max_io_wait(total_ram_gb, os_ram_mb, process_ram_mb, num_processes, cpu_utilization):
    # Convert RAM sizes to MB
    total_ram_mb = total_ram_gb * 1024
    total_ram_for_processes_mb = total_ram_mb - os_ram_mb
    
    # Calculate total time for one process to complete
    total_time_for_one_process = (0.99 / cpu_utilization) * ((num_processes * process_ram_mb) / total_ram_for_processes_mb)
    
    
    max_io_wait = (12 * total_time_for_one_process) / 13
    
    return max_io_wait

total_ram_gb = 4
os_ram_mb = 512
process_ram_mb = 256
num_processes = 13
cpu_utilization = 0.99


max_io_wait = calculate_max_io_wait(total_ram_gb, os_ram_mb, process_ram_mb, num_processes, cpu_utilization)
print("Maximum I/O wait time that can be tolerated:", max_io_wait, "seconds")




# Question:2

def calculate_sequential_time(cpu_time, io_wait_time):
    # Total time for sequential execution
    total_time = (2 * cpu_time) + (2 * io_wait_time)
    return total_time

def calculate_parallel_time(cpu_time, io_wait_time):
    # Total time for parallel execution
    total_time = cpu_time + io_wait_time
    return total_time

cpu_time = 20  # in minutes
io_wait_time = 0.5 * cpu_time  

# Calculate time for sequential execution
sequential_time = calculate_sequential_time(cpu_time, io_wait_time)
print("Time for sequential execution:", sequential_time, "minutes")

# Calculate time for parallel execution
parallel_time = calculate_parallel_time(cpu_time, io_wait_time)
print("Time for parallel execution:", parallel_time, "minutes")



# Question:3

class KernelStack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            print("Kernel stack overflow")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.top == -1:
            print("Kernel stack underflow")
            return None
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

kernel_stack = KernelStack(10)

kernel_stack.push("Function 1")
kernel_stack.push("Function 2")

popped_item = kernel_stack.pop()
print("Popped item from kernel stack:", popped_item)
