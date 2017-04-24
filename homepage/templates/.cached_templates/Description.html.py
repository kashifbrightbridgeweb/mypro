# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492729282.33183
_enable_loop = True
_template_filename = '/Users/anderswood/Desktop/SeraMomo_Git/homepage/templates/Description.html'
_template_uri = 'Description.html'
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
        __M_writer('\n<html>\n  <title>Description</title>\n<div style="background-color:#E92380;" class="navbar navbar-default navbar-static-top">\n      <div class="container">\n        <div class="navbar-header">\n          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-ex-collapse">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n          </button>\n          <a class="navbar-brand" href="homepage"><span style="color:white;">SeraMoMo</span></a>\n        </div>\n        <div class="collapse navbar-collapse" id="navbar-ex-collapse">\n          <div style="margin-top: -10px; margin-right:80px;">\n            <center>\n            <h3 style="color:white;">Description </h3>\n            </center>\n          </div>\n          <ul style="margin-top:-50px;" class="nav navbar-nav navbar-right">\n            <li style="color:black;">\n              <a href="homepage" style="color:white;">Home</a>\n            </li>\n            <li>\n              <a href="/homepage/#ordernow" style="color:white;">Order Now</a>\n            </li>\n            <li>\n             <a href="/Products" style="color:white">Products</a>\n            </li>\n            <li>\n             <a href="/Description" style="color:white">Description</a>\n            </li>\n          </ul>\n        </div>\n      </div>\n    </div>\n    <meta charset="utf-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>\n    <script type="text/javascript" src="http://netdna.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>\n    <link href="http://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">\n    <link href="Seremomo Website.css" rel="stylesheet" type="text/css">\n  </head><body>\n\n<div class="section">\n\t<div class="container">\n\t\t<div class="row">\n\t\t\t<div class="col-md-6">\n\n\t\t\t\t<img src="http://i.imgur.com/1ft9rxp.jpg" class="img-responsive"/>\n\t\t\t</div>\n\t\t\t<div class="col-md-6">\n\t\t\t\t<h1 class="text-primary">Sera\'s Meat MoMo</h1>\n\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. </p>\n\t\t\t<div class="col-md-3">\n\t\t\t\t<button type="button" class="btn btn-primary">Buy Now</button>\n\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div>\n\n<div class="section">\n\t<div class="container">\n\t\t<div class="row">\n\t\t\t<div class="col-md-6">\n\t\t\t\t<img src="http://i.imgur.com/1ft9rxp.jpg" class="img-responsive"/>\n\t\t\t</div>\n\t\t\t<div class="col-md-6">\n\t\t\t\t<h1 class="text-primary">Sera\'s Vegetarian MoMo</h1>\n\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. </p>\n\t\t\t<div class="col-md-3">\n\t\t\t\t<button type="button" class="btn btn-primary">Buy Now</button>\n\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div>\n\n<div class="section">\n\t<div class="container">\n\t\t<div class="row">\n\t\t\t<div class="col-md-6">\n\t\t\t\t<img src="https://upload.wikimedia.org/wikipedia/commons/b/b7/Babi_panggang_sauce.JPG" class="img-responsive"/>\n\t\t\t</div>\n\t\t\t<div class="col-md-6">\n\t\t\t\t<h1 class="text-primary" id="MoMo1">Sera\'s MoMo sauce</h1>\n\t\t\t\t<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. </p>\n\t\t\t<div class="col-md-3">\n\t\t\t\t<a href="/Products"><button type="button" class="btn btn-primary">Buy Now</button></a>\n\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n</div>\n\n\n\n\n</body></html>\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"51": 4, "35": 1, "28": 0, "45": 4, "57": 51}, "filename": "/Users/anderswood/Desktop/SeraMomo_Git/homepage/templates/Description.html", "uri": "Description.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
