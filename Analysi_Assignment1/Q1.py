import time
import matplotlib.pyplot as plt

def power (a,n):
    r=1
    for _ in range(n):
        r*=a

    return r    


def power_div(a,n):
    if n==0:
      return 1
    elif n%2==0:
        half_p=power_div(a,n//2)
        return half_p*half_p
    else:
        half_p=power_div(a,(n-1)//2)
        return a*half_p*half_p
    

start_time = time.time()
power(2,3)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time of power: {elapsed_time} seconds")

start_time = time.time()
power_div(2,3)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time of power_div: {elapsed_time} seconds")


n_values = [1,100,1000,10000,100000,1000000]

power_times = []
power_div_times= []

for n in range(len(n_values)):
    start_time = time.time()*(10**9)
    power(2,n_values[n])
    end_time = time.time()*(10**9)
    power_times.append(end_time - start_time)

    start_time = time.monotonic()*(10**9)
    power_div(2,n_values[n])
    end_time = time.monotonic()*(10**9)
    power_div_times.append(end_time - start_time)



plt.plot(n_values, power_times, label='power(a, n)')
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()