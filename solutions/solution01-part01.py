# SOLUTION
def read_data(filename):
    '''
        Reads data from hdf5 file of data.

    '''
    # this is the way to open an hdf5 file for reading
    f = h5py.File(filename, "r")
    # accessing a data set is just like accessing as a dictionary
    mask = f['mask'].value
    img = f['img'].value
    # for groups (which are groups of data sets, we can access them the same
    # way)
    attributes = f['attributes']
    # we can grab all the keys from the attributes as so
    keys = attributes.keys()
    # note that this is an iterator, call list(keys) to see the keys
    # we'll do it here just to be explicit (but this step is not necessary)
    keys = list(keys)

    md = dict()
    # iterate over the keys
    for key in keys:
        # access the attribute like a dictionary
        # alternately, this also works: f['attributes/beam_center_x'] etc
        # (but the current implementation is simpler)
        md[key] = attributes[key].value

    return img, mask, md

# if running from the notebooks directory:
img, mask, md = read_data("../data/00000000.hd5")
