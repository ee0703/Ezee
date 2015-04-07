#! /usr/bin/env python
#-*- coding:utf-8 -*-

'''ezee web framework
    http://ezee.pqx.ee/
'''

from __future__ import print_function
from string import Template
from wsgiref import simple_server
from pprint import pformat 
import sys,re,traceback

__version__ = '0.1'
__all__ = ['ezee_app', 'render_html']
err_types = ['404', '500',  'render_html_err', 'template_not_found']

class ezee_app(object):
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 8000
        self.wsgi_server = simple_server.make_server
        self.url_map = {}
        self.err_handlers = {err:getattr(self, 'handle_'+err) if hasattr(self, 'handle_'+err) else None 
                                for err in err_types}

    def url(self, *url_list, **params):
        def url_decorator(func):
            methods = params['method'] if 'method' in params else ['GET']
            for url in url_list:
                self.url_map[url] = {'func':func.__name__, 'method':methods }
            def func_ret(env):
                ret = func()
                return ret
            return func_ret
        return url_decorator

    def __url_dispatch(self, env):
        path_info = env['PATH_INFO']
        if path_info in self.url_map:
            return self.url_map[path_info]['func']

    def __response(self, start_response,(status, content_type, content)):
        start_response(status, [('content-type', content_type)])
        return content

    def __entry(self, env, start_response):
        action = self.__url_dispatch(env)
        if(action):
            try:
                ret = action(env)
                if type(ret) is str:
                    return self.__response(start_response, ('200 OK', 'text/plain', ret))
                else:
                    return self.__response(start_response, ('200 OK', ret['type'], ret['content']))
            except:
                return self.__response(start_response, self.handle_err(type = '500', env = env))
        else:
            return self.__response(start_response, self.handle_err(type = '404', env = env))

    def run(self):
        httpd = self.wsgi_server(self.host, self.port, self.__entry)
        try:
            print('start server at %s:%s\npress [Ctrl+C] to stop' % (self.host, self.port))
            httpd.serve_forever()
        except KeyboardInterrupt: 
            print('||server exit')
    
    def handle_404(self, type, env):
        ret = render_html(dict(err_type = '404 page not found', urls=pformat(self.url_map), env = pformat(env)), 'err.tpl')
        return '404 Not Found',ret['type'],ret['content']

    def handle_500(self, type, env):
        ret = render_html(dict(err_type = '500 Interner server error', urls=pformat(self.url_map), env = pformat(env)), 'err.tpl')
        return '404 Not Found',ret['type'],ret['content']

    def handle_err(self, **kw):
        err_type = kw['type'] if 'type' in kw else ''
        err_msg = kw['msg'] if 'msg' in kw else ''
        env =  kw['env'] if 'env' in kw else None
        if err_type and err_type in self.err_handlers:
            return self.err_handlers[err_type](type = err_type, env = env)

class ezee_template(Template):
    delimiter = '$$'

def render_html(data, template, str_template = None):
    if not str_template:
        with open(template) as tpl_file:
            str_template = ezee_template(tpl_file.read())
            tpl_file.close()
    else: str_template = ezee_template(str_template)
    return {'type':'text/html', 'content':str_template.substitute(data)}

if __name__ == '__main__':
    run_test()

