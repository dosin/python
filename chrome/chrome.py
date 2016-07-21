
import sys
import re
import os
import urllib

def get_url(platform, version):
  chrome = {
    # win32
    'win32_stable' : 'https://dl.google.com/tag/s/appguid={8A69D345-D564-463C-AFF1-A69D9E530F96}&iid={E38B1B95-BC8B-F8A0-4E5A-1927D46D37A9}&lang=zh-CN&needsadmin=prefers/update2/installers/ChromeStandaloneSetup.exe',
    'win32_beta' : 'https://dl.google.com/tag/s/appguid={8A69D345-D564-463C-AFF1-A69D9E530F96}&iid={E38B1B95-BC8B-F8A0-4E5A-1927D46D37A9}&lang=zh-CN&needsadmin=prefers&ap=1.1-beta/update2/installers/ChromeStandaloneSetup.exe',
    'win32_dev' : 'https://dl.google.com/tag/s/appguid={8A69D345-D564-463C-AFF1-A69D9E530F96}&iid={E38B1B95-BC8B-F8A0-4E5A-1927D46D37A9}&lang=zh-CN&needsadmin=prefers&ap=2.0-dev/update2/installers/ChromeStandaloneSetup.exe',
    'win32_canary' : 'https://dl.google.com/tag/s/appguid={4ea16ac7-fd5a-47c3-875b-dbf4a2008c20}&iid={E38B1B95-BC8B-F8A0-4E5A-1927D46D37A9}&lang=zh-CN&needsadmin=prefers/update2/installers/ChromeSetup.exe',
    # win64
    'win64_stable' : 'https://dl.google.com/tag/s/appguid={8A69D345-D564-463C-AFF1-A69D9E530F96}&iid={E38B1B95-BC8B-F8A0-4E5A-1927D46D37A9}&lang=zh-CN&needsadmin=prefers&ap=x64-stable/update2/installers/ChromeStandaloneSetup64.exe',
    'win64_beta' : 'https://dl.google.com/tag/s/appguid={8A69D345-D564-463C-AFF1-A69D9E530F96}&iid={E38B1B95-BC8B-F8A0-4E5A-1927D46D37A9}&lang=zh-CN&needsadmin=prefers&ap=x64-beta/update2/installers/ChromeStandaloneSetup64.exe',
    'win64_dev' : 'https://dl.google.com/tag/s/appguid={8A69D345-D564-463C-AFF1-A69D9E530F96}&iid={E38B1B95-BC8B-F8A0-4E5A-1927D46D37A9}&lang=zh-CN&needsadmin=prefers&ap=x64-dev/update2/installers/ChromeStandaloneSetup64.exe',
    'win64_canary' : 'https://dl.google.com/tag/s/appguid={4ea16ac7-fd5a-47c3-875b-dbf4a2008c20}&iid={E38B1B95-BC8B-F8A0-4E5A-1927D46D37A9}&lang=zh-CN Canary&needsadmin=prefers&ap=x64-canary/update2/installers/ChromeSetup.exe',
    # mac
    'mac_stable' : 'https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg',
    'mac_beta' : 'https://dl.google.com/chrome/mac/beta/GoogleChrome.dmg',
    'mac_dev' : 'https://dl.google.com/chrome/mac/dev/GoogleChrome.dmg',
    'mac_canary' : 'https://dl.google.com/release2/q/canary/googlechrome.dmg'
  }
  return chrome['%s _ %s' % (platform, version)]

def report(a, b, c):
  percent = 100.0 * a * b / c
  if percent > 100:
    percent = 100
  sys.stdout.write('\r%.2f%%' % percent)
  sys.stdout.flush()


def download(platform, version, path):
  url = get_url(platform, version)
  filename = re.findall(r'\/(\w+\.\w+)', url).pop()
  if not os.path.exists(path):
    os.makedirs(path)
  print '\nFetching: %s' % filename
  urllib.urlretrieve(url, os.path.join(path, filename), report)
  print '\nComplete'

def main():
  args = sys.argv[1:]
  if not args or len(args) != 2:
    print '\n   usage : chrome.py platform version [path]'
    print 'platform : win32/win64/mac'
    print ' version : stable/beta/dev/canary'
    sys.exit(1)
  if args[0] not in 'win32/win64/mac':
    print 'only support win32/win64/mac platform'
    sys.exit(1)
  platform = args[0]
  args = args[1:]
  if args[0] not in 'stable/beta/dev/canary':
    print 'only support stable/beta/dev/canary version'
    sys.exit(1)
  version = args[0]
  args = args[1:]
  if not args:
    path = '.'
  else:
    path = args[0]
  download(platform, version, path)

if __name__ == '__main__':
  main()