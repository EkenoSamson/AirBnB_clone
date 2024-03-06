## 0x00. AirBnB clone

The goal of this project is to deploy a simple copy of AirBnB website on server.
After 4 months, we will have a complete web application composed by:

+ A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
+ A website (the front-end) that shows the final product to everybody: static and dynamic
+ A database or files that store data (data = objects)
+ An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

### Console
+ We'll start by creating a data model
+ This model must have the CRUD ability
#C_ Create
#R_ Read
#U_ update
#D_ Delete
+ Must store and persist objects to a file (JSON file)

With the Console:
We"ll manipulate a powerful storage engine.
The storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.
Hence: from our console code (the command interpreter itself) and from the front-end and
RestAPI we will build later, we won’t have to pay attention (take care) of how our objects are stored.

This abstraction will also allow us to change the type of storage easily without updating all of our codebase.

The console will be a tool to validate this storage engine

// Add a console picture



