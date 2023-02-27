# Game AI - Avatars Generator

A repository for generating character portraits using StyleGan3.

![img](avatars/original.png)

## 0. Prerequisities
- Download and install cuda - [download link](https://developer.nvidia.com/cuda-11.1.0-download-archive)
- Download and install anaconda - [download link](https://www.anaconda.com/products/distribution/start-coding-immediately)
- Add anaconda to Path - [StackOverflow link](https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10)
- Install MSVC - [donwload link](https://visualstudio.microsoft.com/vs/), [YouTube tutorial](https://www.youtube.com/watch?v=UA99zPAIDmw)
- Download the model - [gdrive link](https://drive.google.com/file/d/1pMiujcIcl3jdpKrgNzXwburTQ0a5B1Xw/view?usp=sharing)

## 1. Setup

Open a command prompt/bash shell in the current directory and run the following commands
```
# create anaconda environment
conda env create -f environment.yml

# activate environment
conda activate ai-avatars
```

## 2. Creating avatars

Run the following comand in the activated environment to generate images
```
# generate a avatar
python stylegan3/gen_images.py --network ./models/fantasy.pkl --outdir ./avatars  --seeds=42 --trunc=0.5
```

## 3. FAQ

Q1. I get his error when installing the packages

```
CondaSSLError: OpenSSL appears to be unavailable on this machine. OpenSSL is required to download and install packages.
```

A1. Follow [this tutorial](https://www.youtube.com/watch?v=hfKAV6OYaKw) and copy the dll files to the conda folder.
