"""
created by: Wangshujing
"""

from __future__ import print_function
import os
import argparse
import numpy as np
import pandas as pd
import time
import shutil
from PIL import Image
from tqdm import tqdm

import torch
from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
import torchvision.models as models

from .util import ProtestDatasetEvalFile, modified_resnet50


def eval_one_file(img_path, model):
        """
        return model output of a images
        """
        model.eval()
        batch_size = 1
        workers = 0
        cuda = False
        # make dataloader
        dataset = ProtestDatasetEvalFile(img_path = img_path)
        data_loader = DataLoader(dataset,
                                num_workers = workers,
                                batch_size = batch_size)
        # load model

        outputs = []
        imgpaths = []

        n_imgs = 1
        with tqdm(total=n_imgs) as pbar:
            for i, sample in enumerate(data_loader):
                imgpath, input = sample['imgpath'], sample['image']
                if cuda:
                    input = input.cuda()

                input_var = Variable(input)
                output = model(input_var)
                outputs.append(output.cpu().data.numpy())
                imgpaths = imgpath
                if i < n_imgs / batch_size:
                    pbar.update(batch_size)
                else:
                    pbar.update(n_imgs%batch_size)

        array = np.concatenate(outputs)
        return {
            'protest': array[0][0],
            'violence': array[0][1], 
            'sign': array[0][2], 
            'photo': array[0][3], 
            'fire': array[0][4],
            'police': array[0][5], 
            'children': array[0][6], 
            'group_20': array[0][7], 
            'group_100': array[0][8], 
            'flag': array[0][9],
            'night': array[0][10], 
            'shouting': array[0][11]
        }

def check_violence(img_file):
# load trained model
    path = os.getcwd()
    model_path = 'model_best.pth.tar'
    cuda = False
    print("*** loading model from {model}".format(model = model_path))
    model = modified_resnet50()
    if cuda:
        model = model.cuda()
    
    with open(os.path.join(path, 'backend' ,'api', model_path), 'rb') as f:
        model.load_state_dict(torch.load(f ,map_location='cpu')['state_dict'])
        # calculate output
    df = eval_one_file(img_file, model)
    return df