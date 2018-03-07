#! /usr/bin/env python
import os
import sys
import json
import feature_extraction

'''
extract feature array from audio file,
save them to file
arg 1: audio folder
arg 2: feature filename
'''
if __name__ == "__main__":
    ff = []
    try:
        if os.path.isdir(sys.argv[1]):
            # ff = [os.path.join(sys.argv[1], f) for f in os.listdir(sys.argv[1]) if f.split('.')[1]=='mp3']
            ff = [os.path.join(sys.argv[1], f) for f in os.listdir(sys.argv[1])]
        feature_file = '../feature_data/' + sys.argv[2]
    except Exception as e:
        print(e)

    feat = {}
    with open(feature_file, 'w') as f_file:
        for f in ff:
            print('processing: {}'.format(f))
            feat['feature'] = list(feature_extraction.feature(f))
            feat_json = json.dumps(feat)
            f_file.write(feat_json+'\n')
    print('saved feature array to ' + feature_file)
