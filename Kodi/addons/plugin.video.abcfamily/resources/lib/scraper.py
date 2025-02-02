# -*- coding: utf-8 -*-
# ABCFamily Kodi Video Addon
#
from t1mlib import t1mAddon
import json
import re
import os
import urllib
import xbmc
import xbmcplugin
import xbmcgui
import HTMLParser
import sys

h = HTMLParser.HTMLParser()
qp  = urllib.quote_plus
uqp = urllib.unquote_plus
UTF8 = 'utf-8'


class myAddon(t1mAddon):

  def getAddonMenu(self,url,ilist):
      html = self.getRequest('http://freeform.go.com/shows')
      a = re.compile('<div class="col-xs-4 shows-grid">.+?href="(.+?)".+?img src="(.+?)".+?<h3>(.+?)<',re.DOTALL).findall(html)
      for url, thumb, name in a:
          fanart = thumb
          infoList ={}
          infoList['Title'] = name
          infoList['TVShowTitle'] = name
          infoList['mediatype'] = 'tvshow'
          contextMenu = [('Add To Library','XBMC.RunPlugin(%s?mode=DF&url=AL%s)' % (sys.argv[0], url))]
          ilist = self.addMenuItem(name,'GE', ilist, url, thumb, fanart, infoList, isFolder=True, cm=contextMenu)
      return(ilist)

  def getAddonEpisodes(self,url,ilist, getFileData=False):
      if not url.startswith('http'):
         url = 'http://freeform.go.com'+url
      html = self.getRequest(url)
      vids = re.compile('<hr />.+?href="(.+?)".+?requires-sign-in="(.+?)".+?src="(.+?)".+?m-y-0">.+?S(.+?) E(.+?) (.+?)<.+?"m-t-1">(.+?)<', re.DOTALL).findall(html)
      if vids == []:
          html = re.compile('<div class="swiper-container"(.+?)<div class="swiper-nav swiper-next', re.DOTALL).search(html)
          if html is None:
              return(ilist)
          html = html.group(1)
          vids = re.compile('<a href="(.+?)".+?url\((.+?)\).+?requires-sign-in="(.+?)".+?<span class="heavy">    <span class="heavy">.+?S(.+?) E(.+?) .+?class="card-title">(.+?)<', re.DOTALL).findall(html)
          vids1 = []
          for url, thumb, elock, season, episode, name in vids:
              thumb = thumb.strip("'")
              vids1.append([url, elock, thumb, season, episode, name, ''])
          vids = vids1
      for url, elock, thumb, season, episode, name,plot in vids:
          if elock != 'False':
              continue
          name = h.unescape(name.decode(UTF8))
          name = name.strip()
          plot = h.unescape(plot.decode(UTF8))
          plot = plot.strip()
          thumb = thumb.strip()
          fanart = thumb
          infoList = {}
          if len(season) > 0 and season.strip().isdigit():
              infoList['Season'] = int(season)
          if len(episode) > 0 and episode.strip().isdigit():
              infoList['Episode'] = int(episode)
          infoList['Title'] = name
          infoList['Plot'] = plot
          infoList['MPAA'] = 'TV-PG'
          infoList['TVShowTitle'] = xbmc.getInfoLabel('ListItem.TVShowTitle')
          infoList['Studio'] = 'ABC'
          infoList['mediatype'] = 'episode'
          if getFileData == False:
              ilist = self.addMenuItem(name,'GV', ilist, url, thumb, fanart, infoList, isFolder=False)
          else:
              ilist.append((infoList['Season'], infoList['Episode'], url))
      return(ilist)

  def doFunction(self, url):
      func = url[0:2]
      url  = url[2:]
      if func == 'AL':
        name  = xbmc.getInfoLabel('ListItem.Title')
        profile = self.addon.getAddonInfo('profile').decode(UTF8)
        moviesDir  = xbmc.translatePath(os.path.join(profile,'TV Shows'))
        movieDir  = xbmc.translatePath(os.path.join(moviesDir, name))
        if not os.path.isdir(movieDir):
            os.makedirs(movieDir)
        ilist = []
        ilist = self.getAddonEpisodes(url, ilist, getFileData = True)
        for season, episode, url in ilist:
            se = 'S%sE%s' % (str(season), str(episode))
            xurl = '%s?mode=GV&url=%s' % (sys.argv[0], url)
            strmFile = xbmc.translatePath(os.path.join(movieDir, se+'.strm'))
            with open(strmFile, 'w') as outfile:
               outfile.write(xurl)         
      json_cmd = '{"jsonrpc":"2.0","method":"VideoLibrary.Scan", "params": {"directory":"%s/"},"id":1}' % movieDir.replace('\\','/')
      jsonRespond = xbmc.executeJSONRPC(json_cmd)

  def getAddonVideo(self,url):
      if not url.startswith('http'):
          url = 'http://freeform.go.com'+url
      html = self.getRequest(url)
      vd = re.compile("VDKA(.+?)'").search(html).group(1)
      url = 'https://api.entitlement.watchabc.go.com/vp2/ws-secure/entitlement/2020/authorize.json'
      udata = 'video%5Fid=VDKA'+str(vd)+'&device=001&video%5Ftype=lf&brand=002'
      uheaders = self.defaultHeaders.copy()
      uheaders['Content-Type'] = 'application/x-www-form-urlencoded'
      uheaders['Accept'] = 'application/json'
      uheaders['X-Requested-With'] = 'ShockwaveFlash/24.0.0.194'
      uheaders['Origin'] = 'http://cdn1.edgedatg.com'
      uheaders['DNT'] = '1'
      uheaders['Referer'] = 'http://cdn1.edgedatg.com/aws/apps/datg/web-player-unity/1.0.6.13/swf/player_vod.swf'
      uheaders['Pragma'] = 'no-cache'
      uheaders['Connection'] = 'keep-alive'
      uheaders['Cache-Control'] = 'no-cache'
      html = self.getRequest(url, udata, uheaders)
      a = json.loads(html)
      if a.get('uplynkData', None) is None:
          xbmcgui.Dialog().notification(self.addonName, self.addon.getLocalizedString(30001), self.addonIcon)
          return

      sessionKey = a['uplynkData']['sessionKey']
      oid, eid = re.compile('&oid=(.+?)&eid=(.+?)&', re.DOTALL).search(sessionKey).groups()
      url = 'http://content.uplynk.com/ext/%s/%s.m3u8?%s' % (oid, eid, sessionKey)
      html = self.getRequest(url)
      url = re.compile('#UPLYNK-MEDIA0.+?http(.+?)\n',re.DOTALL).search(html).group(1)
      url = 'http'+url
      liz = xbmcgui.ListItem(path = url.strip())
# No need to process subtitles, all shows have closed captions
      infoList={}
      infoList['mediatype'] = xbmc.getInfoLabel('ListItem.DBTYPE')
      infoList['Title'] = xbmc.getInfoLabel('ListItem.Title')
      infoList['TVShowTitle'] = xbmc.getInfoLabel('ListItem.TVShowTitle')
      infoList['Year'] = xbmc.getInfoLabel('ListItem.Year')
      infoList['Premiered'] = xbmc.getInfoLabel('Premiered')
      infoList['Plot'] = xbmc.getInfoLabel('ListItem.Plot')
      infoList['Studio'] = xbmc.getInfoLabel('ListItem.Studio')
      infoList['Genre'] = xbmc.getInfoLabel('ListItem.Genre')
      infoList['Duration'] = xbmc.getInfoLabel('ListItem.Duration')
      infoList['MPAA'] = xbmc.getInfoLabel('ListItem.Mpaa')
      infoList['Aired'] = xbmc.getInfoLabel('ListItem.Aired')
      infoList['Season'] = xbmc.getInfoLabel('ListItem.Season')
      infoList['Episode'] = xbmc.getInfoLabel('ListItem.Episode')
      liz.setInfo('video', infoList)
      xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

