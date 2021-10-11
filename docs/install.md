## Installation

#### Download models

###### Option 1:

Directly download the full-packed released package [ROMP.zip](https://github.com/Arthur151/ROMP/releases/download/v1.0/ROMP_v1.0.zip) from github, latest version v1.0.

###### Option 2:

Clone the repo:
```bash
git clone -b master --single-branch https://github.com/Arthur151/ROMP
```

Then download the ROMP data from [Github release](https://github.com/Arthur151/ROMP/releases/download/v1.0/ROMP_data.zip), [Google drive](https://drive.google.com/file/d/1EZYEeLft5C2TkugaqsTP_wIsHVlWCyO8/view?usp=sharing).

Unzip the downloaded ROMP_data.zip under the same path of ROMP.
```bash
unzip ROMP_data.zip
```

The layout would be
```bash
ROMP
  - demo
  - models
  - src
  - trained_models
```

#### Set up environments

Please intall the Pytorch 1.6 from [the official website](https://pytorch.org/). We have tested the code on Ubuntu 18.04 and Centos 7.

Install packages:
```bash
cd ROMP/src
pip install -r requirements.txt
```

#### Proper pyrender setup

Please check the overall installation process from the [pyrender installation guide](https://pyrender.readthedocs.io/en/latest/install/index.html).
You need to install correct version of OSMesa and pyopengl.

Installing OSMesa from Debian package:
```
sudo apt update
sudo wget https://github.com/mmatl/travis_debs/raw/master/xenial/mesa_18.3.3-0.deb
sudo dpkg -i ./mesa_18.3.3-0.deb || true
sudo apt install -f
```

Installing a compatible fork of pyopengl:
```
git clone https://github.com/mmatl/pyopengl.git
pip install ./pyopengl
```
