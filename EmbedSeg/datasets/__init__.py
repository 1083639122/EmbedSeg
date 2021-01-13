from EmbedSeg.datasets.TwoDimensionalDataset import TwoDimensionalDataset
#from EmbedSeg.datasets.ThreeDimensionalDataset import ThreeDimensionalDataset

def get_dataset(name, dataset_opts):
    if name == "2d": 
        return TwoDimensionalDataset(**dataset_opts)
    elif name=="3d":
        pass
        #return ThreeDimensionalDataset(**dataset_opts)
    else:
        raise RuntimeError("Dataset {} not available".format(name))
