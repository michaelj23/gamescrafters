from pyspark import SparkContext
from random import uniform

# Approximate PI using Monte Carlo integration
sc = SparkContext("local", "pi")
N = 1e7
radius = 1
square_area = 4 * radius
num_partitions = 4 # N should be divisible by num_partitions

# Hacky? way to generate N random points in parallel
montecarlo_rdd = sc.parallelize([None]*num_partitions, num_partitions)
def gen_rand_points(iter):
    start_bound = -1 * radius
    end_bound = radius
    num_pts = int(N // num_partitions)
    for _ in range(num_pts):
        x = uniform(start_bound, end_bound)
        y = uniform(start_bound, end_bound)
        yield (x, y)
montecarlo_rdd = montecarlo_rdd.mapPartitions(gen_rand_points)

in_circle = lambda point: point[0]**2 + point[1]**2 <= 1
fraction_in_circle = montecarlo_rdd.filter(in_circle).count()

print("PI IS: " + str(square_area * fraction_in_circle / N))
