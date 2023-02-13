QUESTION: What are the key differences between Python2 and Python3?

ANSWER: 
Some of the key differences between Python 2 and Python 3 are:
  -In Python 2, the print statement is used to display output. In Python 3, the print function is used instead.
  -In Python 2, the division operator between two numbers returns an integer if both operands are integers. In Python 3, it returns a float if either operand is a float.
  -In Python 2, the / operator performs integer division if both operands are integers. In Python 3, the // operator performs integer division.
  -Python 3 has better support for Unicode, including more consistent handling of text encoding.
  -In Python 2, the range function returns a list. In Python 3, it returns an iterable range object.
  -In Python 2, the input function returns a string. In Python 3, it returns a value of the type specified by the input's syntax.
  -In Python 3, all text is stored as unicode, and binary data is stored in bytes.



QUESTION: What happens if you import the same library into the code twice?

ANSWER:
It won´t cause errors, when you import any library in your code, the library is imported once, this means that it´s loaded in memory once. So, for example, if you make any changes you make to the library during the second import will not take effect.
It´s considered a bad practice.



QUESTION: What is circular (cyclic) import and how can you avoid it?

ANSWER:
Circular or Cyclic import occurs when two or more modules depend on each other. ModuleZ imports ModuleX and vice versa. This causes an error.
This problem can be avoided using "Absolute Import" technique for example:

from packageX import functionZ
from packageY.subpackage1 import classW

In this case you´re importing strictly what you need from other module, specifying the full path.
With this technique you can avoid circular imports and make your much more readable and mantainable, which is a good practice.



QUESTION: What is a context manager?

ANSWER:
A context manager is an object that defines the methods __enter__ and __exit__ and is used to manage a context in which a certain set of operations are performed, such as file handling and DB connections for example.



QUESTION: Describe how a list data structure works.

ANSWER:
A list is a data structure that stores an ordered collection of elements. Each element in a list has an index, which is a unique integer that represents its position in the list. The first element in the list has an index of 0.
In Python, a list is implemented as a dynamic array, which means that it can grow dynamically to accommodate the number of elements it contains, when we add an element or decrease when we eliminate an element in the list.


QUESTION: Which data type in Python should I choose for the items container so that the operation of searching for an item is asymptotically the most efficient?

ANSWER:
You should choose a set.


QUESTION: Estimate the difficulty of quick sorting in the worst-case scenario.

ANSWER:
O(N^2)


QUESTION: Estimate the complexity of the operation of searching for an element in the search tree in the worst-case scenario.

ANSWER:
There are no correct answers.


QUESTION: What is a “heap data structure”?

ANSWER:
A heap is a type of data structure that is used to implement priority queues. A priority queue is a queue-like data structure that allows elements to be inserted in any order, but retrieves elements in order of priority.


QUESTION: What features should a binary tree have in order to be a search tree?

ANSWER:
The left child of a node must contain a value that is less than the parent node's value.
The right child of a node must contain a value that is greater than the parent node's value.
Each node's left and right subtrees must also be binary search trees.


QUESTION: How can I get the value of the username variable in the controller if it is passed from the page by the POST method?

ANSWER:
request.POST.get('username')


QUESTION: Which command runs the development web server in Django?

ANSWER:
python manage.py runserver


QUESTION: What arguments in this code are passed to the view function?
`path('/example/<int:id>/', example_view)`

ANSWER: 
Positioned id argument that has an int type.


QUESTION: You need to write a controller that returns data from the database in the form of an object. On the basis of which class would you create it?

ANSWER:
ListView


QUESTION: You have changed the models in a project. What commands do you need to run to commit changes and start migrations?

ANSWER:
commands for the commit changes:
git add .
git commit -m "commit message"

commans for the migration:
python manage.py makemigrations
python manage.py migrate


QUESTION: What is middleware?

ANSWER:
It's a component of the Django request-response handling process that allows you to modify or add to the request and response objects before they are passed to the view function or after they are returned from the view function.


QUESTION: What types of JOIN queries in SQL do you know? Describe them and specify the differences between them.

ANSWER:
There are several types of JOIN in SQL, such as:
INNER JOIN: This type of join returns only the rows that have matching values in both tables. It's the most commonly used join and is used to combine rows from two or more tables based on a common column.
LEFT JOIN: This type of join returns all the rows from the left table (the first table in the join clause) and the matching rows from the right table (the second table in the join clause). If there's no match in the right table, the result will contain NULL values for the columns from the right table.
RIGHT JOIN: This type of join returns all the rows from the right table and the matching rows from the left table. If there's no match in the left table, the result will contain NULL values for the columns from the left table.
FULL OUTER JOIN: This type of join returns all the rows from both tables, and if there's no match in one of the tables, the result will contain NULL values for the columns from the non-matching table.
CROSS JOIN: This type of join returns the Cartesian product of the two tables, meaning every row from the first table is combined with every row from the second table.

The difference between the different join types lies in the way they handle non-matching rows between the two tables. Inner join only returns the matching rows, while outer joins (left, right, and full) return the matching rows as well as the non-matching rows from one of the tables. Cross join returns the Cartesian product of the two tables.


QUESTION: There are two tables: A and B. The first table has 4 columns and 10 records, and the second one has 5 columns and 8 records. How many rows and columns will be output with the select * from A,B query, and why?

ANSWER:
The output will have 4 columns from table A and 5 columns from table B, for a total of 9 columns. The number of rows in the output will be the product of the number of rows in tables A and B, which is 10 * 8 = 80 rows.
That´s beacause it´s cross join, where the number of rows in the output is equal to the product of the number of rows in each input table.


QUESTION: Indicate the main differences between SQL and NoSQL databases. Give examples of how both of them can be used and explain your choice.

ANSWER:
The main differences between SQL and NoSQL databases are:
Structure: SQL databases have a fixed schema, while NoSQL databases do not.
Scalability: NoSQL databases are often more scalable than SQL databases and are better suited to big data applications.
Query language: SQL databases use SQL as their query language, while NoSQL databases often use different query languages or APIs.
Performance: NoSQL databases are generally faster than SQL databases when it comes to handling large amounts of unstructured or semi-structured data.

When choosing between SQL and NoSQL databases, it depends on the specific use case and requirements of the project.
For example, if you need to build a database for a customer management system, an SQL database might be a better choice, as the data structure is well defined and you have strict data integrity requirements. But if you are building a database for a social media application that needs to handle large amounts of unstructured data, such as user-generated content, then a NoSQL database might be a better choice.


QUESTION: You need to write Python code that will send users' comments to a certain forum. Which request method would you choose for this — GET, POST, or PUT? Explain your choice.

ANSWER:
The POST request method is usually the most appropriate choice. This is because the POST method is used for submitting data to a resource to be processed


QUESTION: Explain which is better: inheritance or composition. Why?

ANSWER: 
In general, inheritance is best used when there is a clear hierarchy of objects with a shared set of attributes and behaviors. Composition is best used when you want to create complex objects from simpler objects, or when you want to manage the lifecycle of objects.


QUESTION: Explain how authentication differs from authorization.

ANSWER: 
Authentication refers to the process of verifying the identity of a user, system, or device.
Authorization is the process of granting or denying access to specific resources or actions based on the identity that has been established through authentication.


QUESTION: What is versioning used for when creating REST API services?

ANSWER:
Versioning is used in REST API services to ensure compatibility and stability of the API as it evolves over time. With versioning, multiple versions of the same API can be maintained and used by different clients, without breaking existing client implementations. This allows for incremental changes to be made to the API without disrupting its existing usage.


QUESTION: What HTTP methods do you know?

ANSWER:
There are several HTTP methods to implement, GET and POST are the most common, some of them are:
GET: This method is used to retrieve information from a server. It does not modify any data on the server.
POST: This method is used to submit information to the server for processing. It is often used when submitting form data.
PUT: This method is used to update information on the server. It replaces existing data with new data.
PATCH: This method is used to partially update information on the server. It updates only specific fields of an existing resource.
DELETE: This method is used to delete information from the server.
HEAD: This method is similar to GET, but it only returns the header information and not the actual response body.
OPTIONS: This method is used to retrieve the allowed methods for a resource on the server.
CONNECT: This method is used to establish a network connection to a resource, usually for the purpose of using a proxy.
TRACE: This method is used to retrieve a diagnostic trace of the request/response communication.
PROPFIND: This method is used to retrieve information about the properties of a resource, such as its size, type, and modification date.


QUESTION: Suggest several options for scaling your service.

ANSWER:
There are several ways to increase the server scalability, here I list some examples:
Horizontal Scaling: Increasing the number of servers to handle the increased traffic, so that each server handles a smaller workload.
Vertical Scaling: Increasing the capacity of an existing server by adding more resources such as RAM, CPU, or storage.
Load balancing: Distributing incoming requests across multiple servers to balance the workload and improve performance.
Content Delivery Network (CDN): Storing static files on a network of servers located around the world, so that they can be served to users from the server closest to them.
Caching: Storing frequently used data in a cache to reduce the need to retrieve it from the main database, improving performance.
Database sharding: Splitting a large database into smaller, more manageable parts, so that each part can be managed and optimized separately.
Microservices: Breaking down a large monolithic application into smaller, independently deployable services, so that each service can be scaled and managed separately.


QUESTION: What ways do you know for changing file access rights in Linux?

ANSWER:
The most common way in Linux for changing file access rights is CHMOD. For example "CHMOD 777 myFile" gives full permision for read, write and execute.
Other way is he CHOWN command, that allows you to change the owner and group ownership of a file or directory. For example, "CHOWN user:group myFile" changes the owner of the file "myFile" to "user" and the group ownership to "group".
Other way the UMASK mask, is a default file permission mask that is applied whenever a new file is created. You can change the umask value to alter the default permissions applied to new files. For example if we put "UMASK 777" in the console, each every new file that´s created will have full permissions in this case.


QUESTION: List the key differences between processes and threads.

ANSWER:
There are several differences between processes and threads, for example, each process runs in a separate memory space and has its own system resources. Threads, share the same memory space and system resources with other threads.
Context switching between threads is faster and more efficient compared to context switching between processes.
Processes are typically allocated more resources such as memory and file descriptors. Threads have to compete for these resources with other threads in the same process.
Processes communicate with each other through inter-process communication mechanisms such as pipes or sockets. Threads can communicate directly with each other through shared memory.
Processes can have different priority levels, and the operating system can prioritize their execution. Threads within a process can have different priority levels, but they all have the same priority level as the process itself.
If a thread crashes, it only affects the performance of the process that contains it. If a process crashes, it will affect the performance of the entire system.
Processes are typically more portable across different operating systems, while threads may have different implementations across different platforms.


QUESTION: What ways of interaction between processes do you know?

ANSWER:
I know and used several techniques of proccess communication such as:
Shared Memory, Pipes, Message Queues, Sockets, Semaphores, Signals.


QUESTION: You typed a 6-character command in the terminal and received the name of the current directory in response. Is this possible?

ANSWER:
Yes, it´s possible using the PWD command, for example, PWD /C will print the full C directory.


QUESTION: What types of DNS records do you know?

ANSWER:
There are several types of DNS records such as:
Address record: associates a domain name with an IP address.
Mail Exchange record: specifies the mail server responsible for handling email for a domain.
Pointer record: associates an IP address with a host name.
Service record: specifies the hostname and port number for a specific service for a domain.
Canonical Name record: allows you to associate a domain name with another domain name.
Name Server record: specifies the authoritative name servers for a domain.


QUESTION: 0 STDIN, 1 STDOUT, 2 STDERR — what does it mean?

ANSWER:
STDIN (Standard Input) is typically used for taking input from the user, either through the keyboard or through a pipe or redirection from another command.
STDOUT (Standard Output) is used to display normal program output. By default, it is usually the terminal window.
STDERR (Standard Error) is used to display error messages and diagnostic information. It is also usually the terminal window, but it can be redirected separately from STDOUT.


QUESTION: What is the name of the DNS record for IPv6?

ANSWER: 
"AAAA" record associates a domain name with an IPv6 address.
