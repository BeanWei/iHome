#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from ihome.libs.yuntongxun.CCPRestSDK import REST
import ConfigParser

#���ʺ�
accountSid= '8a216da8627648690162843e217602d5'

#���ʺ�Token
accountToken= '6fef8fc8ef3b478b966c99db420c8a4a'

#Ӧ��Id
appId='8a216da8627648690162843e21d002db'

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com'

#����˿� 
serverPort='8883'

#REST�汾��
softVersion='2013-12-26'

class CCP(object):
    """�Զ��嵥���࣬���ڷ�����"""
    #���ڼ�¼ʵ��
    __instance=None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            #û��ʵ��������¼��һ��ʵ������
            cls.__instance=super(CCP, cls).__new__(cls,*args, **kwargs)

            # ��ʼ��REST SDK
            cls.__instance.rest = REST(serverIP, serverPort, softVersion)
            cls.__instance.rest.setAccount(accountSid, accountToken)
            cls.__instance.rest.setAppId(appId)
        return cls.__instance

    def send_sms(self,to, datas, tempId):
        """������Ϣ�ӿ�"""
        # ���÷�����Ϣ�ӿڷ��صģ�������Ϣ�Ľ��
        result = self.rest.sendTemplateSMS(to, datas, tempId)
        if result.get('statusCode') == '000000':   # ���ͳɹ����ص�״̬��
            return 1
        else:
            return 0

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id

# def sendTemplateSMS(to,datas,tempId):
#
#     #��ʼ��REST SDK
#     rest = REST(serverIP,serverPort,softVersion)
#     rest.setAccount(accountSid,accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to,datas,tempId)
#     for k,v in result.iteritems():
#
#         if k=='templateSMS' :
#                 for k,s in v.iteritems():
#                     print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)
#
   
#sendTemplateSMS(�ֻ�����,��������,ģ��Id)