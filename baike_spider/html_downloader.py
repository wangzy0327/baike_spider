# coding:utf8
'''
Created on 2016年7月11日

@author: Wangziyang
'''
import urllib2


class HtmlDownloader(object):
    

    
    def download(self,url):
        if url is None:
            return None
        
        response=urllib2.urlopen(url)
        
        if response.getcode()!=200:
            return None
        
        return response.read()
        
    
    
    
    



