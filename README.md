# WeCylorsApp
#### 写在前面的话
* 本项目全名 Team WeCylors Web Application  
系 *LNPC - Team WeCylors* 内部开发的网络安全Web学习平台  
* 项目基于 <kbd>Python3-Django</kbd> + <kbd>SQLite3</kbd> 开发
* 目前项目开发中……  
  
#### 项目树 
```  
WeCylorsApp Project  
    ├ Blog APP
    |    ├ Experiences
    |    ├ Tutorials
    |    └ Writeup
    └ CTF / AWD APP
         ├ Challenge Module
         |     ├ Exercise Mode
         |     └ Competition Mode
         ├ Flag Module
         |     ├ Static Flag
         |     └ Dynamic Flag (for Web)
         └ Score Module
               ├ Exercise Score
               ├ Competition Score
               |       ├ Static Mode
               |       └ Blood Mode
               └ Check-in Score
```  

#### 环境准备
* Python 3 \(Python 3.8 推荐\)
* Django 3.0.6  

#### 环境启用
```shell
git clone https://github.com/Rayee200/WeCylorsApp.git
cd WeCylorsApp
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0:8000
```
