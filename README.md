# pyspark-examples
[pyspark](http://spark.apache.org/docs/0.9.0/python-programming-guide.html) (python spark api) [examples](http://spark.apache.org/examples.html)

## Usage

###### Step Zero: [download pyspark](http://spark.apache.org/downloads.html) (the examples ship with it)

### Unpack spark and view examples

    cd <Downloads folder or otherwise same directory as spark-*.tar>
    tar xvf spark-2.1.0-bin-hadoop2.7.tar
    cd spark-2.1.0-bin-hadoop2.7
    ls examples/src/main/python/

### list ML, SQL examples

    ls examples/src/main/python/ml/

### Execute examples

    ./bin/spark-submit examples/src/main/python/<example>.py 

### Alternative execute examples (from pyspark shell)

     $ ./bin/pyspark
     ...
     Welcome to
       ____              __
      / __/__  ___ _____/ /__
     _\ \/ _ \/ _ `/ __/  '_/
    /__ / .__/\_,_/_/ /_/\_\   version 2.1.0
       /_/
     ...
     >>> execfile("examples/src/main/python/ml/sql_transformer.py")
