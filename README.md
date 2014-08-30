Simple contact form processing
----------------------------------

You have a static website (e.g. Jekyll), and wanna give your visitors the ability to reach you, huh?
No problem!

All we need is [Mandrill](http://mandrillapp.com) and [Heroku](http://heroku.com) accounts, and a bit of python to get it work.


0. Assumptions
--------------------

You have:

* Heroku toolbelt installed
* Active Mandrill account and API KEY

1. Create a heroku web  app
---------------------


```bash
    $ git clone https://github.com/ousenko/simple-contact-form.git
    $ heroku create <YOUR_HEROKU_APP>
    $ heroku config:set MANDRILL_API_KEY=<KEY>
    $ heroku config:set USER_EMAIL=<YOUR EMAIL>
    $ heroku config:set USER_SITE=<YOUR SITE>
    $ heroku config:set SUCCESS_PAGE=<A SUCCESS PAGE TO REDIRECT USER TO AFTER THE MESSAGE IS SENT>
```

2. Front-end setup
-------------------

In your form html code specify the following:

```html
<form action="https://<YOUR_HEROKU_APP>.herokuapp.com/send">
  Email: <input type="text" name="name"><br>
  Name: <input type="text" name="email"><br>
  Subject: <input type="text" name="subject"><br>
  Message: <textarea name="message" cols="40" rows="5"></textarea>
  <input type="submit" value="Send Message">
</form> 
```


3. Enjoy
----------

Don't forget to star this repo! ;)
