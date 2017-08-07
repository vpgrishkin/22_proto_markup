from livereload import Server

server = Server()

# run a shell command
server.watch('templates/*.html', 'python render_templates.py')


server.serve()