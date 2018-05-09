import sys, os, json

# Change to darknet directory and add the python module
os.chdir('darknet')
sys.path.append(os.path.join(os.getcwd(),'python/'))
import darknet as dn

# Configure Darknet
dn.set_gpu(0)
net = dn.load_net('cfg/yolov3.cfg', 'yolov3.weights', 0)
meta = dn.load_meta('cfg/coco.data')

# Create data folder if necessary
if not os.path.exists('../data'):
    os.makedirs('../data')

for subdir, dirs, files in os.walk('../photos/listing-photos'):
    for file in files:
        if (file.endswith('.jpg')):
            listingId = subdir.split('/')[-1]
            print('Processing listing ' + listingId + ' - ' + file)

            r = dn.detect(net, meta, os.path.join(subdir, file))

            if not os.path.exists('../data/' + listingId):
                os.makedirs('../data/' + listingId)
            
            with open('../data/' + listingId + '/' + file.split('.')[0] + '.json', 'w') as outfile:
                json.dump(r, outfile)
