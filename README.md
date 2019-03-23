# iot-fault-detection

## Sub Tasks
* Create python script to merge faulty and baseline data with/without labels. Script should be able to take a merge window parameter. MW 
will be number of samples in a slot. Final data will be merged dataset with having MW samples from each dataset file. It should be 
shuffles around MW as well. Output should be two files: with label and without label - **chandhya**
* Setup tsdb(influxdb) - **Raja**
* Create python script to write data to tsdb - **Ujjawal**
* Create python script to read data without/with labels and store in influxdb - **Raja**
* Create python script to read a sequence of data in random TW chunks from influxdb.
* Create a python script which takes some data read form influxdb and feed to a selected classifier. This is prediction.
* Create python script which takes some part of labeled data and feed it to a neural network classifier. It should be parameterized with
percent of data to read. This is training
* Create python script which prepared data for the classifier
* Setup tensor flow with a neural network classifier - **Jeremy**
* Create python script to store detection results to influxdb by classifier
* Create python script to train new classifiers by new data from labeled dataset
