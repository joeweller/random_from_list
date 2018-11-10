from random import choice


class Rfl:

    def __init__(self, obj_list):
        if not type(obj_list) == type(list()):
            raise ValueError('obj_list is not a list')
        else:
            self.obj_list = obj_list

    def __next__(self):
        """Return random value
        """
        #  choose random value from obj_list
        try:
            c = choice(self.obj_list)
        except IndexError:
            raise StopIteration()

        # remove random value from obj_list
        self.obj_list.remove(c)

        return c

    def __iter__(self):
        """Iter
        """
        return self

    def remaining(self):
        """Return current obj_list
        """
        return self.obj_list
