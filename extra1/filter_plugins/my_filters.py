# filter_plugins/my_filters.py

class FilterModule(object):
    def filters(self):
        return {
            'upper': self.to_uppercase
        }

    def to_uppercase(self, a_string):
        return str(a_string).upper() 