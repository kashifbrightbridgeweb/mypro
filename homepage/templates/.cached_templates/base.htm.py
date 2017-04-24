# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492570201.7361765
_enable_loop = True
_template_filename = 'C:/Users/matth/Desktop/seramomosite/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content', 'title']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n    \r\n\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n   <footer class="section section-primary">\r\n      <div class="container">\r\n        <div class="row">\r\n          <div class="col-sm-6">\r\n            <h1><a href="/ordernow" style="color:white">Order Now</a></h1>\r\n            <p>Order now to be amazed by the delicious flavor of Sera MoMo!\r\n              <br>\r\n              </p>\r\n          </div>\r\n          \r\n           <div class="col-sm-6">\r\n            <p class="text-info text-right" contenteditable="False">\r\n              <a href="homepage" style="color:white">Home</a>&nbsp; - &nbsp;\r\n              <a href="/aboutus" style="color:white">AboutUs</a>&nbsp; - &nbsp;\r\n              <a href="/privacypolicy" style="color:white">Privacy Policy</a>&nbsp; - &nbsp;\r\n              <a href="/termsandconditions" style="color:white">Terms\r\n              and Conditions</a>&nbsp; - &nbsp;\r\n              <a href="/contactus" style="color:white">Contact Us</a>&nbsp; - &nbsp;\r\n              <a href="/Products" style="color:white">Products</a>&nbsp; - &nbsp;\r\n              <a href="/Description" style="color:white">Description</a>\r\n            </p>\r\n\r\n          <div class="col-sm-6">\r\n            <p class="text-info text-right">\r\n              <br>\r\n              <br>\r\n            </p>\r\n            <div class="row">\r\n              <div class="col-md-12 hidden-lg hidden-md hidden-sm text-left">\r\n                <a href="https://www.instagram.com/seramomollc/"><i class="fa fa-3x fa-fw fa-instagram text-inverse"></i></a>\r\n                <a href="https://twitter.com/search?f=tweets&q=seramomo144&src=typd"><i class="fa fa-3x fa-fw fa-twitter text-inverse"></i></a>\r\n                <a href="https://www.facebook.com/people/Sera-MoMo/100009670604927"><i class="fa fa-3x fa-fw fa-facebook text-inverse"></i></a>\r\n                <a href="#"><i class="fa fa-3x fa-fw fa-github text-inverse"></i></a>\r\n              </div>\r\n            </div>\r\n            <div class="row">\r\n              <div class="col-md-12 hidden-xs text-right">\r\n                <a href="https://www.instagram.com/seramomollc/"><i class="fa fa-3x fa-fw fa-instagram text-inverse"></i></a>\r\n                <a href="https://twitter.com/search?f=tweets&q=seramomo144&src=typd"><i class="fa fa-3x fa-fw fa-twitter text-inverse"></i></a>\r\n                <a href="https://www.facebook.com/people/Sera-MoMo/100009670604927"><i class="fa fa-3x fa-fw fa-facebook text-inverse"></i></a>\r\n                <a href="#"><i class="fa fa-3x fa-fw fa-github text-inverse"></i></a>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </footer>\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n      Site content goes here in sub-templates.\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n  \r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "source_encoding": "utf-8", "filename": "C:/Users/matth/Desktop/seramomosite/homepage/templates/base.htm", "line_map": {"66": 11, "36": 13, "37": 17, "38": 20, "39": 20, "40": 20, "45": 29, "46": 81, "47": 81, "48": 81, "17": 4, "19": 0, "78": 72, "54": 27, "72": 11, "60": 27, "30": 2, "31": 4}}
__M_END_METADATA
"""
