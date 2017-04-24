# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492728550.575956
_enable_loop = True
_template_filename = '/Users/anderswood/Desktop/SeraMomo_Git/homepage/templates/Products.html'
_template_uri = 'Products.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


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
        __M_writer = context.writer()
        __M_writer('\n\n\n')
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
        __M_writer('\n<html>\n  <title>Products</title>\n<div style="background-color:#E92380;" class="navbar navbar-default navbar-static-top">\n      <div class="container">\n        <div class="navbar-header">\n          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-ex-collapse">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n          </button>\n          <a class="navbar-brand" href="homepage"><span style="color:white;">SeraMoMo</span></a>\n        </div>\n        <div class="collapse navbar-collapse" id="navbar-ex-collapse">\n          <div style="margin-top: -10px; margin-right:80px;">\n            <center>\n            <h3 style="color:white;">Products </h3>\n            </center>\n          </div>\n          <ul style="margin-top:-50px;" class="nav navbar-nav navbar-right">\n            <li style="color:black;">\n              <a href="homepage" style="color:white;">Home</a>\n            </li>\n            <li>\n              <a href="/homepage/#ordernow" style="color:white;">Order Now</a>\n            </li>\n            <li>\n             <a href="/Products" style="color:white">Products</a>\n            </li>\n            <li>\n             <a href="/Description" style="color:white">Description</a>\n            </li>\n          </ul>\n        </div>\n      </div>\n    </div>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>\n    <script type="text/javascript" src="http://netdna.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>\n    <link href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">\n    <link href="Seremomo Website.css" rel="stylesheet" type="text/css">\n  </head><body>\n<div class="section">\n\t<div class="container">\n\t\t<div class="row">\n\t\t\t<div class="col-md-6">\n\t\t\t\t<img src="http://i.imgur.com/1ft9rxp.jpg" class="img-responsive"/>\n\t\t\t</div>\n\t\t\t<div class="col-md-6">\n\t\t\t\t<h1 class="text-primary">Sera\'s Vegetarian Momo</h1>\n\t\t\t\t<p> Made with fresh, organic produce, and delicious IDAHO potatoes.  Vegetarian, and Vegan, friendly, Sera’s Veggie MoMos bring an updated taste to a Himalayan classic. </p>\n\t\t\t<div class="col-md-3">\n\t\t\t\t<a href="/Description#MoMo1" id="MoMo1"><button type="button" class="btn btn-primary">Find Out More</button></a>\n\t\t\t</div>\n\t\t\t<div class="col-md-3">\n\t\t\t\t<button type="button" class="btn btn-primary">Pre-Order</button>\n\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div>\n<div class="section">\n\t<div class="container">\n\t\t<div class="row">\n\t\t\t<div class="col-md-6">\n\t\t\t\t<img src="http://i.imgur.com/1ft9rxp.jpg" class="img-responsive"/>\n\t\t\t</div>\n\t\t\t<div class="col-md-6">\n\t\t\t\t<h1 class="text-primary">Sera\'s Meat MoMo</h1>\n\n\t\t\t\t<p>handcrafted with a mixture of grass-fed pork and turkey from Melheur River Meats (Boise, Idaho), and organic produce (cabbage, cilantro, red/green onions), combined with traditional Himalayan spices (cumin, turmeric, and Sera’s spice blend).  With every bite you will Taste the Himalayas.</p>\n \n\t\t\t\t<div class="col-md-3">\n\t\t\t\t<a href="/Description#MoMo2" id="MoMo2"><button type="button" class="btn btn-primary">Find Out More</button></a>\n\t\t\t</div>\n\t\t\t<div class="col-md-3">\n\t\t\t\t<button type="button" class="btn btn-primary">Pre-Order</button>\n\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div>\n<div class="section">\n  <div class="container">\n    <div class="row">\n      <div class="col-md-6">\n        <img src="https://upload.wikimedia.org/wikipedia/commons/b/b7/Babi_panggang_sauce.JPG" class="img-responsive"/>\n      </div>\n      <div class="col-md-6">\n        <h1 class="text-primary">Sera\'s MoMo Sauce</h1>\n\n        <p>Not just for MoMo!  A versatile sauce made with fresh tomatoes, and sesame seeds, it goes well with anything!  Available for pre-orders only.</p>\n \n        <div class="col-md-3">\n        <a href="/Description#MoMo2" id="MoMo2"><button type="button" class="btn btn-primary">Find Out More</button></a>\n      </div>\n      <div class="col-md-3">\n        <button type="button" class="btn btn-primary">Pre-Order</button>\n      </div>\n      </div>\n    </div>\n  </div>\n</div>\n\n</body></html>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"51": 4, "35": 1, "28": 0, "45": 4, "57": 51}, "filename": "/Users/anderswood/Desktop/SeraMomo_Git/homepage/templates/Products.html", "uri": "Products.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
