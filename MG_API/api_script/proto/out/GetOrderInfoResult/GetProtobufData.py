#coding=utf-8

import sys
sys.path.append('D:\\AUTOTEST\\MG_API\\PROTO\\out\\GetOrderInfoResult')
import GetOrderInfoResult_pb2

def GetProtoData(ReturnData):

	obj=GetOrderInfoResult_pb2.GetOrderInfoResult()
	obj.ParseFromString(ReturnData)
	return obj