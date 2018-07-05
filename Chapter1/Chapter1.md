# The Python Data Model

One of the best qualities of Python is its consistency. after working with Python for a while, you are able to start making informed见多识广的, correct guesses about features that are new to you.

However, if you learned another object-oriented language before Python, you may have found it strange to use len(collection) instead of collection.len(). This apparent oddity is the tip of an iceberg that, when properly understood, is the key to everything we called Pythonic. The iceberg is called the Python data model, and it describes the API that you can use to make your own objects play well with the most idiomatic 符合语言习惯的 language features.

You can think of the data model as a description of Python as a framework. It formalizes the interfaces of the building blocks of the language itself, such as sequences, iterators, functions, classes, contex managers, and so on.

While coding with any framework, you spend a lot of time implementing methods that are called by the framework. The same happens when you leverage the Python data model. The Python interpreter invokes special methods to perform basic object operations, often triggered by special syntax. The special method names are always written with leading and trailing double underscores (i.e., \__getitem\__). For example, the syntax obj\[key\] is supported by the \__getitem\__ special method. In order to evaluate my_collection\[key\], the interpreter calls my_collection.\_\_getitem\_\_(key).




## A Pythonic Card Deck

The first thing to note is the use of collections.namedtuple to construct a simple class to represent individual cards. Since Python2.6, namedtuple can be used to build classes of objects that are just bundles of attributes with no custom methods, like a database record. In the example, we use it to protive a nice representation for the cards in the deck, as shown in the console session:
