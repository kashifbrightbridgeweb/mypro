# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492570201.6630678
_enable_loop = True
_template_filename = 'C:/Users/matth/Desktop/seramomosite/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<html>\r\n  <head>\r\n  <title>Homepage</title>\r\n    <meta charset="utf-8">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1">\r\n    <script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>\r\n    <script type="text/javascript" src="http://netdna.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>\r\n    <link href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">\r\n    <link href="Seremomo Website.css" rel="stylesheet" type="text/css">\r\n  </head>\r\n  <body>\r\n    <div class="cover">\r\n      <div class="navbar">\r\n        <div class="container">\r\n          <div class="navbar-header">\r\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-ex-collapse">\r\n              <span class="sr-only">Toggle navigation</span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n            </button>\r\n            <img src="http://i.imgur.com/q1jHatA.png" class="navbar-brand" style="height: 300px">\r\n          </div>\r\n          <div class="collapse navbar-collapse" id="navbar-ex-collapse">\r\n            <ul class="nav navbar-nav navbar-right">\r\n              <li class="active">\r\n                <a style="color:black;" href="homepage">Home</a>\r\n              </li>\r\n              <li>\r\n                <a style="color:black;" href="/homepage/#ordernow">Order Now</a>\r\n              </li>\r\n              <li>\r\n             <a href="/Products" style="color:black">Products</a>\r\n            </li>\r\n            <li>\r\n             <a href="/Description" style="color:black">Description</a>\r\n            </li>\r\n            </ul>\r\n          </div>\r\n        </div>\r\n      </div>\r\n      <div class="cover-image" style="background-image: url(\'https://static.pexels.com/photos/66556/pexels-photo-66556.jpeg\');"></div>\r\n      <div class="container">\r\n        <div class="row">\r\n          <div class="col-md-12 text-center">\r\n            <h1 class="text-inverse">Sera MoMo</h1>\r\n            <p class="text-inverse">From the Himalayan cliffs to your kitchen.</p>\r\n            <br>\r\n\r\n            <video width="560" height="315" controls>\r\n  <source src="/static/homepage/media/SeraMoMoVid.mp4" type="video/mp4">\r\n\r\n</video>\r\n<!--             <video width="560" height="315" contorls="">\r\n              <source src="/static/homepage/media/SeraMoMoVid.mp4" type="video/mp4">\r\n              <iframe width="560" height="315" src="https://www.youtube.com/embed/ST8NC_titZo" frameborder="0" allowfullscreen></iframe>\r\n            </video> -->\r\n            <!-- <iframe class="headerVid" src="https://www.youtube.com/watch?v=bZr-L37nLiM"></iframe>-->\r\n          </div> \r\n        </div>\r\n      </div>\r\n    </div>\r\n    <div class="section">\r\n      <div class="container">\r\n        <div class="row">\r\n          <div class="col-md-6">\r\n            <img src="http://i.imgur.com/41z9Yfj.jpg" class="bordertime img-responsive" style="">\r\n          </div>\r\n          <div class="col-md-6">\r\n            <h1 class="text-primary">Sera MoMo</h1>\r\n            <h3>Our Story</h3>\r\n            <p>Sera MoMo brings you a taste of the Himalayas.   A recipe handed down from generation to generation in the shadow of Mt. Everest, Sera MoMo is a traditional Sherpa food, updated with farm fresh produce and grass fed meats.In 2015 "Great Quake" Sera\'s homeland was devastated and many family members home and livelihoods were destroyed. After the tragedy Sera founded Sera MoMo to bring awareness and raise money to help the rebuilding process in Nepal.  Sera handcrafts each dumpling, and offers a prayer, “Om Mane Padme Hung,” for the wellbeing of those who eat them, as well as those affected by the earthquake.  With every healthy, delicious bite, Sera MoMo brings you the authenticity of Sherpa food.</p>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n    <div class="section">\r\n      <div class="container">\r\n        <div class="row">\r\n          <div class="col-md-6">\r\n            <h1 class="text-primary" id="ordernow">Order Now</h1>\r\n            <h3>Sera MoMo</h3>\r\n            <p>Bring home the taste of authentic himalayan food with Sera MoMos. Sera MoMo\'s are a must bring to social gatherings, parties, family dinners and more. The brilliant zest and flavors are sure to make anyone\'s mouth water. Just the smell of these amazing treats will make people go running for just a little taste. The flavors and gusto of Sera MoMo\'s will leave anyone enchanted.\r\n            <br>\r\n            <br>\r\n<!-- <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top" class="buttonz"> \r\n<input type="hidden" name="cmd" value="_s-xclick">\r\n<input type="hidden" name="hosted_button_id" value="ETRY6KBJPEEYS">\r\n<table>\r\n<tr><td><input type="hidden" name="on0" value="Sera MoMo Menu">Sera MoMo Menu</td></tr><tr><td><select name="os0">\r\n  <option value="Sera MoMo (15 Meat)">Sera MoMo (15 Meat) $10.99 USD</option>\r\n  <option value="Sera MoMo (15 vegan/Veg)">Sera MoMo (15 vegan/Veg) $10.99 USD</option>\r\n  <option value="Sera MoMo Sauce">Sera MoMo Sauce $8.00 USD</option>\r\n  <option value="Sera MoMo Lunch Special">Sera MoMo Lunch Special $10.00 USD</option>\r\n  <option value="Sera MoMo Catering (per person)">Sera MoMo Catering (per person) $15.00 USD</option>\r\n</select> </td></tr>\r\n</table>\r\n<input type="hidden" name="currency_code" value="USD">\r\n<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_buynowCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">\r\n<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">\r\n</form>\r\n                <button type="submit" class="btn btn-primary btn-lg">\r\n                Order Now\r\n                </button>\r\n<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">\r\n</form>\r\n-->       <a href="/products">\r\n          <button type="submit" class="btn btn-primary btn-lg">\r\n                See our products\r\n                </button>\r\n                </a>  \r\n\r\n\r\n\r\n\r\n\r\n\r\n            <br>\r\n            </p>\r\n          </div>\r\n          <div class="col-md-6">\r\n            <img src="http://i.imgur.com/1ft9rxp.jpg" class="bordertime img-responsive">\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n    <div class="section">\r\n      <div class="container">\r\n        <div class="row">\r\n          <div class="col-md-6">\r\n            <img src="http://i.imgur.com/FFwKccA.jpg" class="bordertime package-image">\r\n          </div>\r\n          <div class="col-md-6">\r\n            <h1 class="text-primary">Additional Services</h1>\r\n            <h3>Catering</h3>\r\n            <p>Sera MoMo Caters! We cater for events for small events (50 people or less). Sera MoMo does many dishes including: Alu Dam(a potatoe dish), Dal Bhat(A traditional Napali dish that includes rice and lentils), Chicken and Curry and of course our classic seramomos. <a href="/contactus">contact us</a> to setup an event. </p>\r\n            <h3>Lunch Special Sera MoMo</h3>\r\n            <p>Local businesses of Boise can also order it for lunch, we deliver cooked sera MoMo for lunch in business office\'s with a minimum of 5 orders of Sera MoMo.\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n</body></html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <title>homepage</title>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "source_encoding": "utf-8", "filename": "C:/Users/matth/Desktop/seramomosite/homepage/templates/index.html", "line_map": {"64": 3, "52": 8, "37": 1, "70": 3, "76": 70, "42": 5, "28": 0, "58": 8}}
__M_END_METADATA
"""
