#coding=utf-8

#import sys
#sys.path.append('D:\\AUTOTEST\\MG_API\\PROTO\\out\\GetGoodsCategoryResult')
import GetGoodsCategoryResult_pb2

def GetProtoData(ReturnData):

	obj=GetGoodsCategoryResult_pb2.GetGoodsCategoryResult()
	obj.ParseFromString(ReturnData)
	return obj