class Angle(object):
    """ An angle between three Atom objects.

        Currently, there is no reference to the actual Atom objects but instead
        they are indexed in the parent molecule class.
    """
    def __init__(self, id1, id2, id3):
        self._id1 = id1
        self._id2 = id2
        self._id3 = id3

    def __repr__(self):
        return("Angle({0:d},{1:d},{2:d})".format(self._id1, self._id2, self._id3))
