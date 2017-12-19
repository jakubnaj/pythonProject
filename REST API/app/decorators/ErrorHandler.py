def handle_error(func):
    def func_wrapper(self):
        try:
            return func(self)
        except Exception as e:
            return {'error': str(e)}
    return func_wrapper