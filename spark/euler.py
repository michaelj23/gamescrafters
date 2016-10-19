from pyspark import SparkContext
from math import ceil

# Solve Project Euler question 1 with Spark. https://projecteuler.net/problem=1
sc = SparkContext("local", "euler1")
nums_rdd = sc.parallelize([3, 5])
limit = 1000

print(nums_rdd.flatMap(lambda num: [num * i for i in range(1, int(ceil(limit / num)))]) \
                .reduce(lambda a, b: a + b))
