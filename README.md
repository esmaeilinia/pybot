# pybot

Research tools for autonomous systems using Python<br>
**Author: [Sudeep Pillai](http://people.csail.mit.edu/spillai)** ([spillai@csail.mit.edu](mailto:spillai@csail.mit.edu))<br>
**License: MIT**<br>

Modules
---
**geometry** is Python package that provides general-purpose tools for fast
prototyping of robotics applications (such as Visual Odometry, SLAM) that
require computing rigid-body transformations. This is a preliminary version that
currently deals mostly with **SE(3)** or 6-DOF (3-DoF Rotational + 3-DoF
translation) and some support for **Sim(3)** motions.

**vision** Computer vision package with several tools including
  camera, tracking, 2d features, 3d features, optical flow,
  recognition, object proposals, caffe, classifier training,
  bag-of-words training, geometry, stereo, drawing etc

**utils** Basic tooling that includes attribute dictionaries,
database-utils including incremental hdf5 tables, dataset readers
[ImageDatasets, StereoDatasets, VelodyneDatasets etc], dataset helpers
[KITTI, NYU-RGBD, SUN3D, Tsukuba Stereo, UW-RGBD, caltech101],
itertools recipes, timing/profiling tools, io utils
[video/image writing, mkdirs, find_files, config parsers, joblib utils, stdout tee-ing, json],
other misc tools including pretty prints, progressbars, colored
prints, counters, accumulators (indexed deques), accumulators with
periodic callbacks etc.

**externals** ROS/LCM drawing tools, ROS/LCM log readers, Google
  Project Tango log reader

Installation
---
Most of the installation assumes you have a clean python virtual
environment to work with. I prefer conda for my development
environment, but you're free to use any alternative (as long as you do
not globally install, in which case I can not provide much support).

1. Install miniconda and setup path in `~/.bashrc`
```sh
wget --no-check-certificate https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
bash Miniconda2-latest-Linux-x86_64.sh -b -p $HOME/anaconda
```

2. Install dependencies into a new conda environment
```sh
conda config --add channels menpo
conda create --name pybot --file conda_requirements.txt
```
Alternatively, if you'd like to add pybot to an already existing
environment,
```sh
conda config --add channels menpo
conda install --name pybot --file conda_requirements.txt
```

3. (Optional) ROS dependencies (reading bag files etc) into the same
environment. First ensure that you are within the pybot virtual
environment.
```sh
source activate pybot
pip install catkin_pkg rospkg
```

Dependencies
---
[bot_geometry](https://github.com/spillai/pybot_geometry), [NumPy](https://github.com/numpy/numpy), [lcm](https://github.com/lcm-proj/lcm), [collections viewer](https://github.mit.edu/mrg/visualization-pod), [libbot](https://github.com/RobotLocomotion/libbot)

All the dependencies need to be available in the `PYTHONPATH`. 


Examples
---
All the 3D visualization demos for the works below were created using the above set of tools. <br>
[Monocular SLAM-Supported Object Recognition](https://www.youtube.com/watch?v=m6sStUk3UVk), 
[High-speed Stereo Reconstruction](http://people.csail.mit.edu/spillai/projects/fast-stereo-reconstruction/pillai_fast_stereo16.mp4)


Tensorflow (Linux 64-bit)
---

Ubuntu/Linux 64-bit, CPU only, Python 2.7
```sh
$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
```

Ubuntu/Linux 64-bit, GPU enabled, Python 2.7
Requires CUDA toolkit 7.5 and CuDNN v5. For other versions, see
"Install from sources" below.
```sh
$ export
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
```

Tensorflow (Mac 64-bit)
---

Mac OS X, CPU only, Python 2.7:
```sh
$ export
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.10.0-py2-none-any.whl
```

Mac OS X, GPU enabled, Python 2.7:
---
```sh
$ export
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow-0.10.0-py2-none-any.whl
```

OpenCV
---
Install OpenCV 2.4.11 from menpo
```sh
conda install -c https://conda.anaconda.org/menpo opencv=2.4.11 -y
```
