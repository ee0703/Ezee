from ezee import * 

app = ezee_app()

@app.url('/')
def helloWorld(env):
    return 'hello world!'

@app.url('/welcom')
def welcom(env):
    name =  env['QUERY_STRING'] if env['QUERY_STRING'] else 'World'
    return render_html(dict(name=name), 'index.tpl')

@app.url('/err')
def err(env):
    num = 100 / 0 # Should be Error
    return 'There is an Error'

if __name__ == '__main__':
    app.run()
