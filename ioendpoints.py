from protorpc import remote
from protorpc import messages
import endpoints


class RequestExampleSchema(messages.Message):
    attr1 = messages.StringField(1)
    attr2 = messages.StringField(2)

class ResponseExampleSchema(messages.Message):
    result1 = messages.StringField(1)
    result2 = messages.StringField(2)

@endpoints.api(
               name='yourapiname',
               version='v1',
               description='yourapidescription'
               )
class YourApiClassName(remote.Service):
    
    @endpoints.method(RequestExampleSchema,ResponseExampleSchema,
                      path='example/dosomething', http_method='POST',
                      name='example.dosomething')
    def dosomething_method(self, request):
        # get request attributes
        attr1 = request.attr1
        # do something here
        response_schema = ResponseExampleSchema(
                                            result1 = 'something',
                                            result2 = 'something 2'
                                            )

        return response_schema

        