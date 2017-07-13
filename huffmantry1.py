import cv2
import numpy as np
from collections import Counter
import heapq
import time

class Node(object):
    def __init__(self, pairs, frequency):
        self.pairs = pairs
        self.frequency = frequency

    def merge(self, other):
        total_frequency = self.frequency + other.frequency
        for p in self.pairs:
            p[1] = "1" + p[1]
25        for p in other.pairs:
            p[1] = "0" + p[1]
        new_pairs = self.pairs + other.pairs
        return Node(new_pairs, total_frequency)

    def __lt__(self, other):
        return self.frequency < other.frequency

def huffman_codes(s):
    table = [Node([[ch, '']], freq) for ch, freq in Counter(s).items()]
    heapq.heapify(table)
    while len(table) > 1:
        first_node = heapq.heappop(table)
        second_node = heapq.heappop(table)
        new_node = first_node.merge(second_node)
        heapq.heappush(table, new_node)
    return dict(table[0].pairs)

def frequency(str):
    freqs={}
    for ch, freq in Counter(str).items():
        freqs[ch]=freq
    return freqs
     

'''img=cv2.imread('100.png',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
arr=np.array([67,90,12,67,90,90,90,12])
set1=arr.ravel()
dict1=frequency(set1)
print ("***********************")
"""##############For printing the frequency of pixels#################"""
print "Frequency values of every pixel"
##for key,values in dict1.items():
  ##  print str(key)+" occurs: "+str(values)

print ("***********************")
dict2=huffman_codes(set1)

"""##################For printing the CODE of pixels###################"""
##for key,values in dict2.items():
  ##  print str(key)+" code: "+str(values)

no_of_pixels_in_original=0
no_of_pixels_in_compressed=0
compression_ratio=0.0
"""######################################################################"""
for key,value in dict1.items():
    no_of_pixels_in_original+=value*8
print "Total number of bits in the original image: "+str(no_of_pixels_in_original)
print ("***********************")
"""######################################################################"""
for key,value in dict2.items():
    for key1,value1 in dict1.items():
        if(key==key1):
            no_of_pixels_in_compressed=no_of_pixels_in_compressed+value1*len(value)
            break;
print "Total number of bits in the compressed image: "+str(no_of_pixels_in_compressed)

compression_ratio=float(no_of_pixels_in_original)/float(no_of_pixels_in_compressed)
print "Compession Ratio: "+str(compression_ratio)

"""for i in set1:
    key=dict2[i]
    time.sleep(.3)
    print str(i)+ " : "+str(key)"""
