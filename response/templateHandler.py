from response.requestHandler import RequestHandler


class TemplateHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.contentType = 'text/html'

    def find(self, routeData):
        try:
            template_file = open('templates/{}'.format(routeData['template']))
            self.contents = template_file
            self.setStatus(200)
            return True
        except FileNotFoundError:
            self.setStatus(404)
            return False
