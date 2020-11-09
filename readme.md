# pythonNode3.7
Study in python latest code and node series

> In this series I'm sharing python basic to advance label nothing else.

#### Features

- Python installation.
- How to write python terminal or IDE.
- Function.
- Class (OOP).
- Python library and modules.
- Basic problem solving.


###### How to install python Linux (ubuntu) OS

By default Linux and Mac OS install python 2.7. If you install python3 or more version you may follow this commands.

##### On Mac OS
- Launch Terminal
- Go to Launchpad – Other – Terminal
- Install HomeBrew
```
(brew --prefix)/opt/python/libexec/bin
brew install python3
```

##### Optional, PATH environment
Set up PATH environment variable, if you used HomeBrew to install Python3, then HomeBrew already added PATH. Do not 
change PATH environment if you can launch python3 from terminal.

Add the following line to your `~/.profile` file

`export PATH=/usr/local/bin:/usr/local/sbin:$PATH`
Usually your Python installation directory looks like this, add it to your PATH

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
import asyncio


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