from chilero import web


class Home(web.View):

    def get(self):
        return web.Response('Hello World!')


routes = [['/', Home]]


if __name__ == '__main__':
    web.run(web.Application, routes)
