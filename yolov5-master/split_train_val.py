import os
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--xml_path', default='D:/NUAACourse/aiDesignData/aiDesignData/xml', type=str, help="input xml label path")
parser.add_argument('--txt_path', default='D:/NUAACourse/aiDesignData/aiDesignData/dataSet', type=str, help="output txt label path")
opt = parser.parse_args()

train_val_percent = 0.8
train_percent = 0.75
xml_filepath = opt.xml_path
txt_savepath = opt.txt_path
total_xml = os.listdir(xml_filepath)
print(total_xml)
if not os.path.exists(txt_savepath):
    os.makedirs(txt_savepath)
num = len(total_xml)
list_index = range(num)
tv = int(num * train_val_percent)
tr = int(tv * train_percent)
train_val = random.sample(list_index, tv)
train = random.sample(train_val, tr)

file_train_val = open(txt_savepath + "/train_val.txt", 'w')
file_test = open(txt_savepath + '/test.txt', 'w')
file_train = open(txt_savepath + '/train.txt', 'w')
file_val = open(txt_savepath + '/val.txt', 'w')

for i in list_index:
    name = total_xml[i][:-4]
    name = 'D:/NUAACourse/aiDesignData/aiDesignData/image/' + name + '.jpg\n'
    if i in train_val:
        file_train_val.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
    else:
        file_test.write(name)
file_train_val.close()
file_train.close()
file_val.close()
file_test.close()
