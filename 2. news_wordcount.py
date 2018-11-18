from __future__ import print_function
import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
         spark = SparkSession\
                 .builder\
                 .appName("NewsWordCount")\
                 .getOrCreate()

         naver_news = "/.../naver_news.txt"

         lines = spark.read.text(naver_news).rdd.map(lambda r: r[0])
         counts = lines.flatMap(lambda line: line.strip().split()) \
                         .map(lambda word: (word, 1)) \
                         .reduceByKey(lambda a, b: a + b) \
                         .map(lambda a: (a[1], a[0])) \
                         .sortByKey(0)

         counts.saveAsTextFile("/.../wordcount_result")
         spark.stop()
