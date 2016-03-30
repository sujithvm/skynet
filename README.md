# skynet
Network Analysis: finding infected nodes and seeding of a network 

[![Build Status](https://travis-ci.org/sujithvm/skynet.svg?branch=master)](https://travis-ci.org/sujithvm/skynet)



### Build instructions (Linux)

Dependencies :

```
$ sudo apt-get install python-pip
$ sudo pip install networkx
$ sudo pip install matplotlib

```

Navigate to `skynet/code`

```
$ python seeding.py
```


### Build instructions (Windows)

Making sure Python is added to build path. Pip is present in `/Scripts/pip.exe`

Dependencies :

```
> pip install networkx
> pip install matplotlib

```

Navigate to `skynet/code`

```
> python seeding.py
```


for pygraphviz :
```
sudo apt-get install -y graphviz libgraphviz-dev pkg-config python-pip
sudo pip install pygraphviz --install-option="--include-path=/usr/include/graphviz" --install-option="--library-path=/usr/lib/graphviz/"

Read : https://github.com/pygraphviz/pygraphviz/issues/71
```