# Web Based Home Security

**List of Topics**:

- [Web Based Home Security](#web-based-home-security)
  - [Datasets](#datasets)
  - [Model Benchmark Reports](#model-benchmark-reports)
  - [Web Application](#web-application)
  - [Results and Dicussions](#results-and-dicussions)
  - [Web Application](#web-application-1)

## Datasets

For this project we use 5 real environment images using Nikon DSLR camera. For each subject we take ~10000 images. 

![images](./dataset-freq-count.png)

## Model Benchmark Reports

Here we use three top convolutional neural network based model, `Inception V3`, `Vgg16` and my `custom cnn model`. In the `./Notebooks/` you can find the three seperate models that we use our training data.

## Web Application

Here we create a simple django based web application to present how the deep learning secure you works, home environment over the internet. 

## Results and Dicussions

## Web Application

To run web application clone the repo and install the required packages.

```bash
$ pip3 install django Pillow tensorflow numpy pandas opencv-desktop all-auth2 scikit-leran matplotlib 
$ python manage.py makemigrations objrecog
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
