## flash - sale - bot
It's a flash sale bot for shopee-commerce in indonesia, you can try to use it, but i don't guarantee it will works properly, and yes.

### How to Use
Just clone the repository or download it, and follow the next step.

#### 1. Downloading Webdriver
Install a chromedriver that correspond on your browser, if you're using chrome you can install chromedriver, and if you're using firefox you can install it too. In this repository i'll be using chrome instead.
* [Chromedriver](https://chromedriver.chromium.org/)
* [Firefox](https://github.com/mozilla/geckodriver/releases)

#### 2. Installing Python and Moduls
This bot only use few of lines that executing every single lines from start until ends. The first you musn't forget is of course installing python, here i use Python 3.8.3 you can install python from [here](https://www.python.org/downloads/release/python-383/) 

You only need one moduls that is Selenium, just install it by typing these words on CMD or on your bash command
```
pip install selenium
```

wait till it done and it's all set, you're ready to start!!

### Getting Started
This is how it started
* First open up your ```flash_sale_bot.py``` using any IDE, you're free to use any IDE you have in your PC (VS Code etc)
* Change the email and password, change it into your credentials
* Input your product link in ```product_link``` in that syntax line 17..
* After you finish those steps you can just execute the code, RUN it (VS Code) or Build it (Sublime Text) or anything.
* The webdriver will do their task properly

### How the BOT works
here's how the BOT actually works
* It's actually loads you into a login page on that Shopee Commerce
* It's going to login automatically using your email and password
* Loads you into the product and click the buy out button for you, yeah you like a king huh
* It's not including clicking on checkout button, coz you wouldn't need that, i mean you should do it manually
* and you finish all the rest 
(dev suggestions: you should turn off OTP login things to get this BOT works smoothly, but you can set the ```time.sleep()``` in line 41 into the time you need to input and then it loads back, yeah just like that.

### Pros and Cons
the pros is:
* You just like a king you don't have to input your password, emails or clicking product and it can be done in few seconds using this code
* You can make this BOT works faster by changing ```time.sleep()```

the cons is:
* Yeah, it depends on your internet
* You must estimate the time left until the product open, or you just can execute at the times the flash sale open

### Further Development
Maybe i'm just going to add GUI to make it nicer for every USER, yeah but someday, somehow.
<br>
Maybe i'm going to add try and except method to make it easier to use too, yeah someday

```
Muhammad Ario Bagus Prakusa
Newbie Python Programmer
```
