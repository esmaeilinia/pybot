# Author: Sudeep Pillai <spillai@csail.mit.edu>
# License: MIT

import cv2
import sys
import time
import numpy as np

from pybot import IMSHOW_FLAG
from pybot.utils.plot_utils import plt
from collections import OrderedDict

global figures, trackbars
figures = OrderedDict()
trackbars = dict()

class WindowManager(object): 
    """
    Basic window manager
    """
    def __init__(self): 
        pass
        self.trackbars_ = dict()
        self.figures_ = OrderedDict()
        self.has_moved_ = set()

    def imshow(self, label, im): 
        cv2.imshow(label, im)
        if label not in self.has_moved_:
            cv2.moveWindow(label, 0, 0)
            self.has_moved_.add(label)

global window_manager
window_manager = WindowManager()

def imshow_plt(label, im, block=True):
    global figures
    if label not in figures: 
        figures[label] = plt.imshow(im, interpolation=None, animated=True, label=label)
        plt.tight_layout()
        plt.axis('off')
        
    figures[label].set_data(im)
    # figures[label].canvas.draw()
    # plt.draw()
    plt.show(block=block)

def bar_plt(label, ys, block=False):
    global figures
    if label not in figures:
        figures[label] = plt.bar(np.arange(len(ys)), ys, align='center')
        plt.title(label)
        # plt.tight_layout()
        # plt.axis('off')

    inds, = np.where([key == label for key in figures.keys()])
    for rect, y in zip(figures[label], ys): 
        rect.set_height(y)

    plt.draw()
    plt.show(block=block)

def print_status(vis, text=None): 
    if text is not None:
        cv2.rectangle(vis, (0, vis.shape[0]-18), (len(text) * 8, vis.shape[0]), (50, 50, 50), -1)
        cv2.putText(vis, '%s' % text, (2, vis.shape[0] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, 
                    (240, 240, 240), thickness = 1)
    return vis

def draw_border(vis, value=128):
    vis[:,0], vis[0,:], vis[:,-1], vis[-1,:] = value, value, value, value
    return vis

if IMSHOW_FLAG: 
    def imshow_cv(label, im, block=False, text=None, wait=2): 
        vis = im.copy()
        print_status(vis, text=text)
        window_manager.imshow(label, vis)
        ch = cv2.waitKey(0 if block else wait) & 0xFF
        if ch == ord(' '):
            cv2.waitKey(0)
        if ch == ord('v'):
            print('Entering debug mode, image callbacks active')
            while True: 
                ch = cv2.waitKey(10) & 0xFF
                if ch == ord('q'): 
                    print('Exiting debug mode!')
                    break
        if ch == ord('s'):
            fn = 'img-%s.png' % time.strftime("%Y-%m-%d-%H-%M-%S")
            print('Saving %s' % fn)
            cv2.imwrite(fn, vis)
        elif ch == 27 or ch == ord('q'):
            sys.exit(1)
else:
    def imshow_cv(*args, **kwargs):
        pass
            
            
def trackbar_update(_=None): 
    global trackbars
    for k,v in trackbars.items(): 
        trackbars[k]['value'] = cv2.getTrackbarPos(v['label'], v['win_name'])    

def trackbar_create(label, win_name, v, maxv, scale=1.0): 
    global trackbars
    if label in trackbars:     
        raise RuntimeError('Duplicate key. %s already created' % label)
    trackbars[label] = dict(label=label, win_name=win_name, value=v, scale=scale)

    cv2.namedWindow(win_name)
    cv2.createTrackbar(label, win_name, v, maxv, trackbar_update)

def trackbar_value(key=None): 
    global trackbars
    if key not in trackbars: 
        raise KeyError('%s not in trackbars' % key)
    return trackbars[key]['value'] * trackbars[key]['scale']

def mouse_event_create(win_name, cb): 
    cv2.namedWindow(win_name)
    cv2.setMouseCallback(win_name, cb)

