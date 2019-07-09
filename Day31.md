# Day 31 
*   Google BigTable is the world's first NoSql database.
## Distributed Database systems.
*   To store data we use the most traditional and common way of using Databases.
*   We process raw data and process it and save to the database
*   In a SQL database we use tables which contains rigid rows and columns.
*   Static schema on write and read means we have fixed the schema when we planned to design the schema of a table.
*   If we want to add a column in a table we have to edit the schema in real time due to which while adding a new column all the users will be disconnected for a second or such.
*   To solve this issue of editing schema in real time we need a new type of system for this.
*   In Large systems we have the following infrastructure.
    *   Users generate queries then goes to multiple Database Engines.
    *   Those engines will then pass your query for processing to CPU and RAM's to thousands of systems.
    *   Then these queries are stored in multiple Hardrives and clusturs for backup and reduce load to a single server.
## NoSql Database Engines
*   It is divided in 4 big categories.
*   Document Oriented Database.
    *   We use this generally for developing a documentation type of websites which contains most of the text.
    *   Example : Wikipedia
    *   Links, Docks, Text, Few Images
    *   MongoDB, CouchDB
*   Columns oriented Database
    *   When we need to print results of a particular column then we use this.
    *   When we want to print a specific column database it will read by rows wize.
    *   Usecase find average salary of all the employees as such it will read all the rows.
    *   Examples: Google BigTable, DynamoDB, Hbase, Cassendra.
    *   DynamoDB is developed by Amazon
    *   Hbase and Cassendra are open sourced.
*   Key value type Database
    *   When we have a lot of attributes of a product or such we use key value system.
    *   Example Redis, Memcached.
    *   This database is generally used to make cache servers.
*   Graph Database
    *   The technology Blockchain uses Graph Database.
    *   When we need linked list pattern for storage or token management we use GraphDB
    *   Example: Neo4j
## Dynamo DB and AWS Lambda
*   This service of Amazon is more expensive then RDS
*   Use Boto3 for using DynamoDB at AWS.
*   AWS Lambda is responsible for allocating resources to DynamoDB.
*   Lambda is an on demand platform independent product.
*   Lambda will allocate resources in real time as per your current needs.
*   The use case of not management of any servers or backend stuff it is called Serverless architecture, Here everything is measured and controlled by AWS Lambda.
## Neural Network
*   First we have a lot of data with lot of attributes.
*   The data we store as a variable is a neuron.
*   The input pins of a neuron are called as dendrites.
*   The ouput pins of a neuron are called as axon.
*   Dendrites are input nodes, every node can be a GPU or CPU
*   ANN (Artificial Neural Networks) 
*   Every hidden layer contains an information which is called as activation function.
*   The 1st layer of neaural network is always input layer and the last is the output layer.
*   All the middle layers are hidden layers which contains neurons.
*   We can and cannot connect every neuron with each other.
*   Number of neurons in hidden layer is average of input neurons.
*   When we connect a neuron with another neuron we are connecting one cpu/gpu/tpu with another cpu/gpu/tpu.
*   Every hidden layer process its mathematical equation is activation function.
*   We can run more then one activation function on one layer but then we need to create a program for this.
*   There are a lot of activtation functions but commonly we use 4 types of functions.
*   More then 2 hidden layers means deep neural networks.
*   Cost Function work is to find errors.
*   Use Cases of Neural Network
    *   Performance Search
    *   Voice Processing
    *   Self Driving Car
    *   Computer Games
*   Geoffren Hinton is God Father of Deep Learning.
### Activation Function
*   Threshold
*   Sigmoid
*   Rectifier
*   Hyperbolic Tangent (tanh)
### Weights in Activation Function.
```
y = m1x1 + m2x2 + m3x3 + b
```
*   Here x1,x2,x3 are the inputs from the dataset and m1,m2,m3 are called as weights.
*   We multiply the data with weights to modify the information, The range of weight comes in between 0 and 1.
*   When we get the wrong output the neural network changes the wights.
*   Cost function calculates difference from current result with the dataset output.
*   Backpropogation it checks that the output is correct or not and if wrong then it sends back to the previous layers for processing.
### Gradient Descent
*   It is used to change the weights in the neurons as per the error.
*   Gradient Descent uses bruiteforce method to generate a random number and adjust the weight.
### EPOC
*   EPOC is the count the number of times the process executed.
*   We can change the number of EPOC
*   Batch size is to pick some size of data or attribute in a batch for processing.


## Task
*   Who changes the difference/compare between the actual output and predicted output.   