# pythonNode

> In this series, I'm sharing python basic to advance and data-structure code, which I'm teaching my friends and brothers.

#### Features

- Python installation.
- How to write Python terminal or IDE.
- Function.
- Class (OOP).
- Python library and modules.
- Basic problem-solving.


###### How to install python Linux (ubuntu) OS

By default Linux and Mac OS install python 2.7. If you install python3 or more version you may follow this commands.

##### Optional PATH environment
Set up PATH environment variable, If you used HomeBrew to install Python3, then HomeBrew already added PATH. Do not 
Change PATH environment if you can launch python3 from the terminal.

Add the following line to your `~/.profile` file

`export PATH=/usr/local/bin:/usr/local/sbin:$PATH`
Usually, your Python installation directory looks like this; add it to your PATH

`PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"`

##### On Linux/Ubuntu
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
python ––version
```

```python
assert sum([1, 2, 3]) == 6, "Should be 6"
```

```python
li = [5, 7, 22, 96, 54, 62, 77, 23, 73, 61]
result = list(filter(lambda x: x % 2 == 0, li))
print(result)

```

```python

from extra import asyncio


async def say_hello():
    print('Hello there,')
    await asyncio.sleep(3)
    print(f'This is Sagor')


# asyncio.run(say_hello())


async def download():
    for i in range(0, 11):
        await asyncio.sleep(1)
        print(f"Download {i}% done")
    print("Thanks Sagor! Your download has been completed.")


asyncio.run(download())

```

> Simple inner function example:

```python
def select(num):
    def child():
        return "Hello, I'm Mbr Sagor"
    
    def child2():
        return "Hi, This is a Bozlur here."
    
    if num == 1:
        return child()
    else:
        return child2()


print(select(1))
print(select(2))

```

###### Decorators are one of the most common popular data structures in Python. Below is a simple example:
```python
def uppercase_decorator(function):
    def wrapper():
        content = function().upper()
        return content
    return wrapper


@uppercase_decorator
def say_hello():
    return "hello there, this is a bozlur rosid sagor"


print(say_hello())
```

###### Static method and class Method example:
```python
class User(object):

    @classmethod
    def get_full_name(cls, first_name, last_name):
        print(f"Full Name is: {first_name} {last_name}")

    @staticmethod
    def get_name(name):
        print(f"Hello {name}")


if __name__ == '__main__':
    User.get_full_name('mbr', 'sagor')
    User.get_name('sagor')
```

> About Me
```python
person = {
    'type': 'engineer',
    'skills': ['Python', 'JavaScript', 'Django', 'FastAPI', 'React.JS', 'Docker', 'AWS'],
    'keepLearning': True
}
```
