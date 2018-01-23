class QueryConverter:
    regex = '\w+'

    def to_python(self, value):
        return str(value.replace('%20', ' '))

    def to_url(self, value):
        return str(value.replace(' ', '%20'))