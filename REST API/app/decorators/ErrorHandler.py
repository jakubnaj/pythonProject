def handle_error(func):
    def func_wrapper(self, *args, **kwds):
        try:
            return func(self, *args, **kwds)
        except Exception as e:
            return {'error': str(e)}
    return func_wrapper
