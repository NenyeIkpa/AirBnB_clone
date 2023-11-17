# AirBnB clone - The Console

***HOW TO START THE APPLICATION?***

Run `./console.py` on your shell prompt - To start the application

NOTE: - A prompt will be given by the console where you type in the various commands.

e.g `(HNBN) <command> <argument(s)>`

***HOW TO USE IT?***

### Interactive Mode

```cmd
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-Interactive Mode

```cmd
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

Type `help` + `<Enter>` on the console prompt - This will provide the information about
the general commands of the console application.

Type `help` `<command>` + `<Enter>` on the console prompt - This will provide the information
of the specific command of the console application.

### Command List
----------------

`./console.py` - to run the application.
Command | Description
--- | ---
`quit` | Exits the program
`EOF` | Exits the program
`create <class>` | Creates an instance of a class
`show <class> <id>` | Prints the string representation of an instance of a class based on class name and id
`destroy <class> <id>` | Deletes instance of a class based on class name and id
`all` | Prints all string representations of all instances
`all <class>` | Prints all string representations of all instances based on class name
`update <class> <id> <attribute name> "<attribute value>"` | Updates an attribute of an instance based on class name and id
`<class>.all()` | Retrieves all instances of a class
`<class>.count()` | Retrieves the number of instances of a class
`<class>.show(<id>)` | Retrieves an instance based on its id
`<class>.destroy(<id>)` | Destroys an instance based on its id

### Classes

Class   |   Description
--- | ---
`BaseModel` | Defines all common attributes/methods for other classes: `id`, `created_at`, `updated_at`.
`FileStorage` | Serializes instances to a JSON file and deserializes JSON file to instances. Methods like `reload()` recreates instances saved to a JSON file.
`User` | Defines User's details with public class attributes: `Email`, `password`, `first_name`, `last_name`.
`State` | Defines State with `name` as public class attribute.
`City` | Defines City with `state_id` and `name`.
`Amenity` | Defines Amenity with `name` attribute.
`Place` | Defines Place with attributes: `city_id`, `user_id`, `Name`, `description`, `number_rooms`, etc.
`Review` | Review is defined by `place_id`, `user_id`, `text`.
