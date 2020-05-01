from webargs.falconparser import parser


class SchemaValidation(object):
    def __init__(self, schema, req):
        self.schema = schema
        self.req = req

    def validate(self):
        return parser.parse(self.schema, self.req)
