#!/bin/bash

# Set the duration for which you want to stress the CPU and memory (in seconds)
duration=60

# Get the number of CPU cores
num_cpus=$(nproc)

# Calculate the number of CPU-bound processes to run
num_cpu_processes=$((num_cpus * 2))

# Function to stress CPU
stress_cpu() {
  for ((i=0; i<$num_cpu_processes; i++)); do
    while true; do
      # This mathematical operation will stress the CPU
      result=$(echo "scale=10000; 4*a(1)" | bc -l)
    done &
  done
}

# Function to stress memory
stress_memory() {
  # Allocate memory in 100MB chunks until the duration ends
  end_time=$((SECONDS + duration))
  while [ $SECONDS -lt $end_time ]; do
    # Allocate 100MB
    data=$(dd if=/dev/urandom bs=100M count=1 | md5sum)
  done
}

# Start the CPU and memory stress functions in the background
stress_cpu
stress_memory

# Run for the specified duration
sleep $duration

# Kill all background processes
killall -9 stress
