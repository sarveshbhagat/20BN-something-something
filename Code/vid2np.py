import cv2
import numpy as np


def webm2arr(video, stride=1):
    """

    :param video: Required path to a video file, relative or absolute
    :param stride: Allows every nth frame to be returned. Default is all frames. All frames are always read in.
    :return: Returns np array of video, with dimensions [Frame, H, W, Channel]
    """
    cap = cv2.VideoCapture(video)
    nframes = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    wframe = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    hframe = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    buf = np.empty((nframes, hframe, wframe, 3), np.dtype('uint8'))

    fc = 0
    ret = True

    while fc < nframes and ret:
        ret, buf[fc] = cap.read()
        fc += 1 + (stride - 1)

    cap.release()
    if stride != 1:
        buf = buf[0:buf.shape[2]:stride, :, :, :]

    return buf
