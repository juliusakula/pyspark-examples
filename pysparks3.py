# Usage: 
# for LOCAL spark to reach S3, some additional hadoop libraries are needed - download them from maven. 
# Not needed for cloud runs as amazon EMR has these already (omit --jars option for cloud runs)
# these do not install a new hadoop, only expands it's capabilities
# 1 https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws/2.7.2
# 2 https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk/1.7.4
# 3 https://mvnrepository.com/artifact/com.google.guava/guava/11.0.2
# Command:
# $SPARK_HOME/bin/spark-submit --jars /Users/jmurdock/Downloads/hadoop-aws-2.7.2.jar,/Users/jmurdock/Downloads/aws-java-sdk-1.7.4.jar,/Users/jmurdock/Downloads/guava-11.0.2.jar pysparks3.py s3n://<bucket>/<file> <aws_access_key> <aws_secret_key>

from __future__ import print_function

import sys
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: spark-submit pysparks3.py s3n://<bucket>/<prefix>/<file*> <ACCESS_KEY> <SECRET_KEY>", file=sys.stderr)
        # * -- if a specific file is left out it will read all files in that directory
        exit(-1)

    spark = SparkSession \
        .builder \
        .appName("PythonWordCount") \
        .getOrCreate()
    sc= spark.sparkContext
    hadoopConf = sc._jsc.hadoopConfiguration()
    hadoopConf.set("fs.s3n.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")

    hadoopConf.set("fs.s3n.awsAccessKeyId", sys.argv[2])
    hadoopConf.set("fs.s3n.awsSecretAccessKey",sys.argv[3])
    s3path = sys.argv[1]
    df = sc.textFile(s3path)
    print("====== Hello Spark user, First Line of your S3 file is '{}' =====".format(df.first()))
    print("====== Hello Spark user, Row Count for your S3 file is {} =====".format(df.count()))

    spark.stop()
