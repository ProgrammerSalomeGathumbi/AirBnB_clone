0x00. AirBnB clone - The console

The goal of the project is to deploy on our server a simple copy of the AirBnB website.
We will have a complete web application composed by:

1. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
2. A website (the front-end) that shows the final product to everybody: static and dynamic
3. A database or files that store data (data = objects)
4. An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
  
First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

What’s a command interpreter?
It’s exactly the sameas the Shell but limited to a specific use-case.We want to be able to manage the objects of our project:

1. Create a new object (ex: a new User or a new Place)
# Create a new user
user1 = User("John", 30, "john@example.com")
print(user1)  # User(name='John', age=30, email='john@example.com')

2. Retrieve an object from a file, a database etc…
3. Do operations on objects (count, compute stats, etc…)
# Do operations on objects
# For example, count the number of users
users = [user1, User("Jane", 25, "jane@example.com"), User("Bob", 40, "bob@example.com")]
print(len(users))  # 3

4. Update attributes of an object
# Update attributes of an object
user1.update_age(31)
print(user1)  # User(name='John', age=31, email='john@example.com')

5. Destroy an object
# Destroy an object
# For example, remove a user from a list
users.remove(user1)
print(users)  # [User(name='Jane', age=25, email='jane@example.com'), User(name='Bob', age=40, email='bob@example.com')]

