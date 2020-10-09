# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:53:01 2020

@author: SAMSUNG
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import struct
import pandas as pd
import numpy as np
import os


#file = open("C:/Users/spyder/DvsGesture/user01_fluorescent.aedat",'rb')

def aedat_to_events(filename):
    label_filename = filename[:-6] +'_labels.csv'
    labels = np.loadtxt(label_filename, skiprows=1, delimiter=',',dtype='uint32')
    events=[]
    with open(filename, 'rb') as file:
        print (file.read(105))
        events = []
        header=file.read(28)
        while len(header) > 0:
            eventtype = struct.unpack('H', header[0:2])[0]
            eventsize = struct.unpack('I', header[4:8])[0]
            eventoffset = struct.unpack('I', header[8:12])[0]
            eventtsoverflow = struct.unpack('I', header[12:16])[0]
            eventcapacity = struct.unpack('I', header[16:20])[0]
            eventnumber = struct.unpack('I', header[20:24])[0]
            eventvalid = struct.unpack('I', header[24:28])[0]
                                                
            for n in range(eventnumber):
                (data, timestamp)=struct.unpack("II",file.read(8))
                x=(data>>17)&0x00001FFF
                y=(data>>2)&0x00001FFF
                p=(data>>1)&0x00000001
                events.append([x,y,timestamp,p])
            header = file.read(28)

#user aedat파일 list형태로
def gather_aedat(directory, start_id, end_id, filename_prefix = 'user'):
    if not os.path.isdir(directory):
        raise FileNotFoundError("DVS Gestures Dataset not found, looked at: {}".format(directory))
    import glob
    fns = []
    for i in range(start_id,end_id):
        search_mask = directory+'/'+filename_prefix+"{0:02d}".format(i)+"_lab"+'*.aedat'
        glob_out = glob.glob(search_mask)
        if len(glob_out)>0:
            fns+=glob_out
    return fns
    print(fns)
    
    
'''
while len(header)>0:
    (eventsource,eventsize,eventoffset,overflow,capacity,number,valid)=struct.unpack("iiiiiii",header)
    for n in range(number):
        (data,time)=struct.unpack("ii",file.read(8))
        x=(data>>17)&0x00001FFF
        y=(data>>2)&0x00001FFF
        p=(data>>1)&0x00000001
        events.append([x,y,time,p])
    header=file.read(28)
print (events[0:100])

file2 = pd.read_csv("C:/Users/spyder/DvsGesture/user01_fluorescent_labels.csv")     # reading the csv file
#asdf.head()      # printing first five rows of the file
for __, row in file2.iterrows():
    print(row['class'],row['startTime_usec'],row['endTime_usec'])
    '''
'''
def aedat_to_events(filename):
    label_filename = filename[:-6] +'_labels.csv'
    labels = np.loadtxt(label_filename, skiprows=1, delimiter=',',dtype='uint32')
    events=[]
    with open(filename, 'rb') as f:
        for i in range(5):
            f.readline()
        while True:
            data_ev_head = f.read(28)
            if len(data_ev_head)==0: break

            eventtype = struct.unpack('H', data_ev_head[0:2])[0]
            eventsource = struct.unpack('H', data_ev_head[2:4])[0]
            eventsize = struct.unpack('I', data_ev_head[4:8])[0]
            eventoffset = struct.unpack('I', data_ev_head[8:12])[0]
            eventtsoverflow = struct.unpack('I', data_ev_head[12:16])[0]
            eventcapacity = struct.unpack('I', data_ev_head[16:20])[0]
            eventnumber = struct.unpack('I', data_ev_head[20:24])[0]
            eventvalid = struct.unpack('I', data_ev_head[24:28])[0]

            if(eventtype == 1):
                event_bytes = np.frombuffer(f.read(eventnumber*eventsize), 'uint32')
                event_bytes = event_bytes.reshape(-1,2)

                x = (event_bytes[:,0] >> 17) & 0x00001FFF
                y = (event_bytes[:,0] >> 2 ) & 0x00001FFF
                p = (event_bytes[:,0] >> 1 ) & 0x00000001
                t = event_bytes[:,1]
                events.append([t,x,y,p])

            else:
                f.read(eventnumber*eventsize)
    events = np.column_stack(events)
    events = events.astype('uint32')
    clipped_events = np.zeros([4,0],'uint32')
    for l in labels:
        start = np.searchsorted(events[0,:], l[1])
        end = np.searchsorted(events[0,:], l[2])
        clipped_events = np.column_stack([clipped_events,events[:,start:end]])
    return clipped_events.T, labels
'''