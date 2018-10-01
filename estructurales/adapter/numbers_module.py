class Numbers(object):

    def get_even_numbers(self, limit):
        return [
            x
            for x in range(limit)
            if x % 2 == 0
        ]

    def get_odd_numbers(self, limit):
        return [
            x
            for x in range(limit)
            if x % 2 != 0
        ]
