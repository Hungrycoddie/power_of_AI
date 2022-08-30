
import sys
import time
import logging
import argparse
import threading
import queue
import random

from pyads import adsPortOpen, adsPortClose, adsSyncReadWriteReq, \
    adsSyncReadDeviceInfoReq, adsSyncReadStateReq, adsSyncWriteControlReq, \
    adsSyncWriteReq, adsSyncReadReq, adsSyncReadWriteReqEx, \
    adsSyncReadReqEx, adsSyncWriteReqEx, adsSyncReadStateReqEx, \
    adsSyncReadDeviceInfoReqEx, adsSyncWriteControlReqEx, \
    adsSyncReadWriteReqEx2, adsSyncReadReqEx2, adsSyncWriteReqEx2, \
    adsSyncReadStateReqEx2, adsSyncReadDeviceInfoReqEx2, \
    adsSyncWriteControlReqEx2, adsSyncReadWriteReqEx3, adsSyncReadReqEx3, \
    adsSyncWriteReqEx3, adsSyncReadStateReqEx3, adsSyncReadDeviceInfoReqEx3, \
    adsSyncWriteControlReqEx3, adsSyncReadWriteReqEx4, adsSyncReadReqEx4, \
    adsSyncWriteReqEx4, adsSyncReadStateReqEx4, adsSyncReadDeviceInfoReqEx4, \
    adsSyncWriteControlReqEx4, adsSyncReadWriteReqEx5, adsSyncReadReqEx5, \
    adsSyncWriteReqEx5, adsSyncReadStateReqEx5, adsSyncReadDeviceInfoReqEx5, \
    adsSyncWriteControlReqEx5, adsSyncReadWriteReqEx6, adsSyncReadReqEx6, \
    adsSyncWriteReqEx6, adsSyncReadStateReqEx6, adsSyncReadDeviceInfoReqEx6, \
    adsSyncWriteControlReqEx6, adsSyncReadWriteReqEx7, adsSyncReadReqEx7, \
    adsSyncWriteReqEx7, adsSyncReadStateReqEx7, adsSyncReadDeviceInfoReqEx7, \
    adsSyncWriteControlReqEx7, adsSyncReadWriteReqEx8, adsSyncReadReqEx8, \
    adsSyncWriteReqEx8, adsSyncReadStateReqEx8, adsSyncReadDeviceInfoReqEx8, \
    adsSyncWriteControlReqEx8, adsSyncReadWriteReqEx9, adsSyncReadReqEx9, \
    adsSyncWriteReqEx9, adsSyncReadStateReqEx9, adsSyncReadDeviceInfoReqEx9, \
    adsSyncWriteControlReqEx9, adsSyncReadWriteReqEx10, adsSyncReadReqEx10, \
    adsSyncWriteReqEx10, adsSyncReadStateReqEx10, adsSyncReadDeviceInfoReqEx10, \
    adsSyncWriteControlReqEx10, adsSyncReadWriteReqEx11, adsSyncReadReqEx11, \
    adsSyncWriteReqEx11, adsSyncReadStateReqEx11, adsSyncReadDeviceInfoReqEx11, \
    adsSyncWriteControlReqEx11, adsSyncReadWriteReqEx12, adsSyncReadReqEx12, \
    adsSyncWriteReqEx12, adsSyncReadStateReqEx12, adsSyncReadDeviceInfoReqEx12, \
    adsSyncWriteControlReqEx12, adsSyncReadWriteReqEx13, adsSyncReadReqEx13, \
    adsSyncWriteReqEx13, adsSyncReadStateReqEx13, adsSyncReadDeviceInfoReqEx13, \
    adsSyncWriteControlReqEx13, adsSyncReadWriteReqEx14, adsSyncReadReqEx14, \
    adsSyncWriteReqEx14, adsSyncReadStateReqEx14, adsSyncReadDeviceInfoReqEx14, \
    adsSyncWriteControlReqEx14, adsSyncReadWriteReqEx15, adsSyncReadReqEx15, \
    adsSyncWriteReqEx15, adsSyncReadStateReqEx15, adsSyncReadDeviceInfoReqEx15, \
    adsSyncWriteControlReqEx15, adsSyncReadWriteReqEx16, adsSyncReadReqEx16, \
    adsSyncWriteReqEx16, adsSyncReadStateReqEx16, adsSyncReadDeviceInfoReqEx16, \
    adsSyncWriteControlReqEx16, adsSyncReadWriteReqEx17, adsSyncReadReqEx17, \
    adsSyncWriteReqEx17, adsSyncReadStateReqEx17, adsSyncReadDeviceInfoReqEx17, \
    adsSyncWriteControlReqEx17, adsSyncReadWriteReqEx18, adsSyncReadReqEx18, \
    adsSyncWriteReqEx18, adsSyncReadStateReqEx18, adsSyncReadDeviceInfoReqEx18, \
    adsSyncWriteControlReqEx18, adsSyncReadWriteReqEx19, adsSyncReadReqEx19, \
    adsSyncWriteReqEx19, adsSyncReadStateReqEx19, adsSyncReadDeviceInfoReqEx19, \
    adsSyncWriteControlReqEx19, adsSyncReadWriteReqEx20, adsSyncReadReqEx20, \
    adsSyncWriteReqEx20, adsSyncReadStateReqEx20, adsSyncReadDeviceInfoReqEx20, \
    adsSyncWriteControlReqEx20, adsSyncReadWriteReqEx21, adsSyncReadReqEx21, \
    adsSyncWriteReqEx21, adsSyncReadStateReqEx21, adsSyncReadDeviceInfoReqEx21, \
    adsSyncWriteControlReqEx21, adsSyncReadWriteReqEx22, adsSyncReadReqEx22, \
    adsSyncWriteReqEx22, adsSyncReadStateReqEx22, adsSyncReadDeviceInfoReqEx22, \
    adsSyncWriteControlReqEx22, adsSyncReadWriteReqEx23, adsSyncReadReqEx23, \
    adsSyncWriteReqEx23, adsSyncReadStateReqEx23, adsSyncReadDeviceInfoReqEx23, \
    adsSyncWriteControlReqEx23, adsSyncReadWriteReqEx24, adsSyncReadReqEx24, \
    adsSyncWriteReqEx24, adsSyncReadStateReqEx24, adsSyncReadDeviceInfoReqEx24, \
    adsSyncWriteControlReqEx24, adsSyncReadWriteReqEx25, adsSyncReadReqEx25, \
    adsSyncWriteReqEx25, adsSyncReadStateReqEx25, adsSyncReadDeviceInfoReqEx25, \
    adsSyncWriteControlReqEx25, adsSyncReadWriteReqEx26, adsSyncReadReqEx26, \
    adsSyncWriteReqEx26, adsSyncReadStateReqEx26, adsSyncReadDeviceInfoReqEx26, \
    adsSyncWriteControlReqEx26, adsSyncReadWriteReqEx27, adsSyncReadReqEx27, \
    adsSyncWriteReqEx27, adsSyncReadStateReqEx27, adsSyncReadDeviceInfoReqEx27, \
    adsSyncWriteControlReqEx27, adsSyncReadWriteReqEx28, adsSyncReadReqEx28, \
    adsSyncWriteReqEx28, adsSyncReadStateReqEx28, adsSyncReadDeviceInfoReqEx28, \
    adsSyncWriteControlReqEx28, adsSyncReadWriteReqEx29, adsSyncReadReqEx29, \
    adsSyncWriteReqEx29, adsSyncReadStateReqEx29, adsSyncReadDeviceInfoReqEx29, \
    adsSyncWriteControlReqEx29, adsSyncReadWriteReqEx30, adsSyncReadReqEx30, \
    adsSyncWriteReqEx30, adsSyncReadStateReqEx30, adsSyncReadDeviceInfoReqEx30, \
    adsSyncWriteControlReqEx30, adsSyncReadWriteReqEx31, adsSyncReadReqEx31, \
    adsSyncWriteReqEx31, adsSyncReadStateReqEx31, adsSyncReadDeviceInfoReqEx31, \
    adsSyncWriteControlReqEx31, adsSyncReadWriteReqEx32, adsSyncReadReqEx32, \
    adsSyncWriteReqEx32, adsSyncReadStateReqEx32, adsSyncReadDeviceInfoReqEx32, \
    adsSyncWriteControlReqEx32, adsSyncReadWriteReqEx33, adsSyncReadReqEx33, \
    adsSyncWriteReqEx33, adsSyncReadStateReqEx33, adsSyncReadDeviceInfoReqEx33, \
    adsSyncWriteControlReqEx33, adsSyncReadWriteReqEx34, adsSyncReadReqEx34, \
    adsSyncWriteReqEx34, adsSyncReadStateReqEx34, adsSyncReadDeviceInfoReqEx34, \
    adsSyncWriteControlReqEx34, adsSyncReadWriteReqEx35, adsSyncReadReqEx35, \
    adsSyncWriteReqEx35, adsSyncReadStateReqEx35, adsSyncReadDeviceInfoReqEx35, \
    adsSyncWriteControlReqEx35, adsSyncReadWriteReqEx36, adsSyncReadReqEx36, \
    adsSyncWriteReqEx36, adsSyncReadStateReqEx36, adsSyncReadDeviceInfoReqEx36, \
    adsSyncWriteControlReqEx36, adsSyncReadWriteReqEx37, adsSyncReadReqEx37, \
    adsSyncWriteReqEx37, adsSyncReadStateReqEx37, adsSyncReadDeviceInfoReqEx37, \
    adsSyncWriteControlReqEx37, adsSyncReadWriteReqEx38, adsSyncReadReqEx38, \
    adsSyncWriteReqEx38, adsSyncReadStateReqEx38, adsSyncReadDeviceInfoReqEx38, \
    adsSyncWriteControlReqEx38, adsSyncReadWriteReqEx39, adsSyncReadReqEx39, \
    adsSyncWriteReqEx39, adsSyncReadStateReqEx39, adsSyncReadDeviceInfoReqEx39, \
    adsSyncWriteControlReqEx39, adsSyncReadWriteReqEx40, adsSyncReadReqEx40, \
    adsSyncWriteReqEx40, adsSyncReadStateReqEx40, adsSyncReadDeviceInfoReqEx40, \
    adsSyncWriteControlReqEx40, adsSyncReadWriteReqEx41, adsSyncReadReqEx41, \
    adsSyncWriteReqEx41, adsSyncReadStateReqEx41, adsSyncReadDeviceInfoReqEx41, \
    adsSyncWriteControlReqEx41, adsSyncReadWriteReqEx42, adsSyncReadReqEx42, \
    adsSyncWriteReqEx42, adsSyncReadStateReqEx42, adsSyncReadDeviceInfoReqEx42, \
    adsSyncWriteControlReqEx42, adsSyncReadWriteReqEx43, adsSyncReadReqEx43, \
    adsSyncWriteReqEx43, adsSyncReadStateReqEx43, adsSyncReadDeviceInfoReqEx43, \
    adsSyncWriteControlReqEx43, adsSyncReadWriteReqEx44, adsSyncReadReqEx44, \
    adsSyncWriteReqEx44, adsSyncReadStateReqEx44, adsSyncReadDeviceInfoReqEx44, \
    adsSyncWriteControlReqEx44, adsSyncReadWriteReqEx45, adsSyncReadReqEx45, \
    adsSyncWriteReqEx45, adsSyncReadStateReqEx45, adsSyncReadDeviceInfoReqEx45, \
    adsSyncWriteControlReqEx45, adsSyncReadWriteReqEx46, adsSyncReadReqEx46, \
    adsSyncWriteReqEx46, adsSyncReadStateReqEx46, adsSyncReadDeviceInfoReqEx46, \
    adsSyncWriteControlReqEx46, adsSyncReadWriteReqEx47, adsSyncReadReqEx47, \
    adsSyncWriteReqEx47, adsSyncReadStateReqEx47, adsSyncReadDeviceInfoReqEx47, \
    adsSyncWriteControlReqEx47, adsSyncReadWriteReqEx48, adsSyncReadReqEx48, \
    adsSyncWriteReqEx48, adsSyncReadStateReqEx48, adsSyncReadDeviceInfoReqEx48, \
    adsSyncWriteControlReqEx48, adsSyncReadWriteReqEx49, adsSyncReadReqEx49, \
    adsSyncWriteReqEx49, adsSyncReadStateReqEx49, adsSyncReadDeviceInfoReqEx49, \
    adsSyncWriteControlReqEx49, adsSyncReadWriteReqEx50, adsSyncReadReqEx50, \
    adsSyncWriteReqEx50, adsSyncReadStateReqEx50, adsSyncReadDeviceInfoReqEx50, \
    adsSyncWriteControlReqEx50, adsSyncReadWriteReqEx51, adsSyncReadReqEx51, \
    adsSyncWriteReqEx51, adsSyncReadStateReqEx51, adsSyncReadDeviceInfoReqEx51, \
    adsSyncWriteControlReqEx51, adsSyncReadWriteReqEx52, adsSyncReadReqEx52, \
    adsSyncWriteReqEx52, adsSyncReadStateReqEx52, adsSyncReadDeviceInfoReqEx52, \
    adsSyncWriteControlReqEx52, adsSyncReadWriteReqEx53, adsSyncReadReqEx53, \
    adsSyncWriteReqEx53, adsSyncReadStateReqEx53, adsSyncReadDeviceInfoReqEx53, \
    adsSyncWriteControlReqEx53, adsSyncReadWriteReqEx54, adsSyncReadReqEx54, \
    adsSyncWriteReqEx54, adsSyncReadStateReqEx54, adsSyncReadDeviceInfoReqEx54, \
    adsSyncWriteControlReqEx54, adsSyncReadWriteReqEx55, adsSyncReadReqEx55, \
    adsSyncWriteRe