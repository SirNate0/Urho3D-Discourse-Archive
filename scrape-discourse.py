#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup, Tag
from collections import namedtuple
import json
from urlpath import URL
from pprint import pprint,pformat
from time import sleep
from numpy.random import rand
from dateutil import parser as dateparser
import os
import math
import pypandoc
#from urllib.request import urlretrieve # Fails with 403 on https://cdn.discordapp.com/attachments/1011222168958418954/1042120445912158248/Animation12.gif

#ProductLink = namedtuple('ProductLink','name page img')

DISABLE_JSON_CACHE = 0 #True # True to force it to re-download the list of topics and the json

def urlretrieve(url,fn):
    if url.startswith('//'):
        url = 'http:' + url
    for i in range(2):
        if i:
            print('Retrying',i)
        try:
            r = requests.get(url)
            sleep(0.1 + 0.042523*rand())
            if r.status_code == 200:
                os.makedirs(os.path.split(fn)[0],exist_ok=True)
                with open(fn,'wb') as f:
                    f.write(r.content)
                return
            else:
                raise Exception(f'Recieved response {r}')
        except Exception as e:
            print('Failed to get url',url,'->',fn,type(e),e)


def mergejson(v1,v2,*args,path=tuple()):
    if len(args):
        return mergejson(mergejson(v1,v2,path=path),*args,path=path)
            
    assert(type(v1) == type(v2))
    if isinstance(v1,dict):
        out = {}
        for k in v1:
            if k in v2:
                out[k] = mergejson(v1[k],v2[k],path=path+(k,))
            else:
                out[k] = v1[k]
        for k in v2:
            if k not in v1:
                out[k] = v2[k]
        return out
    elif isinstance(v1,list):
        if v1 != v2:
            return v1 + v2
        else:
            return v1
    else:
        if not (v1 == v2):
            if path not in [('views',)]:
                print(path,v1,v2)
                raise ValueError(f'Mismatched Json {v1} {v2}')
        return v1
        

if 0:
    p1 = requests.get('https://discourse.urho3d.io/t/3d-rich-text-view/2969.json?page=1').json()
    p2 = requests.get('https://discourse.urho3d.io/t/3d-rich-text-view/2969.json?page=2').json()
    p3 = requests.get('https://discourse.urho3d.io/t/3d-rich-text-view/2969.json?page=3').json()
    p = mergejson(p1,p2,p3)
    stream = p['post_stream']['stream']
    actual = [p['id'] for p in p['post_stream']['posts']]
    print(stream == actual)
    print(len(p))
    pprint(p.keys())
    exit()

        
    
base = URL('https://discourse.urho3d.io')


def users():
    pass
    
    
files = []
def posts():
    url = base / 'latest.json?ascending=false&no_definitions=true'
    filename ='all-topics.json'
    if os.path.exists(filename) and not DISABLE_JSON_CACHE:
        with open(filename,'rb') as f:
            print('Loading',flush=True)
            topics = json.load(f)
            print('Loaded',flush=True)
    else:
        topics = []
        users = []
        primary_groups = []
        flair_groups = []
        extra = []
        def doadd(f,p,u,t,x):
            topics.extend(t)
            users.extend(u)
            primary_groups.extend(p)
            flair_groups.extend(f)
            extra.extend(x)
            
        def add(flair_groups,primary_groups,users,topic_list):
            """ Adds the groups and returns the next url """ 
            tl = dict(**topic_list)
            del tl['topics']
            doadd(flair_groups,primary_groups,users,topic_list['topics'],tl)
            return base / topic_list['more_topics_url'].replace('?','.json?')
        while url:
        #for i in range(2):
            try:
                print('Loading topics list:',url,end=' ')
                r = requests.get(url)
                content = json.loads(r.content)
                print(r,flush=True)
                #s = pformat(content)
                #print(s[:1000])
            
                #print(*content.keys())
                url = add(**content)
                sleep(0.1 + 0.042523*rand())
            except Exception as e:
                print(type(e),e)
                #print(r.content)
                break
            
        with open(filename,'w') as f:
            json.dump(topics,f)
            
        with open('all-topics-extra.json','w') as f:
            json.dump({'users':users,'primary_groups':primary_groups,'flair_groups':flair_groups,'extra':extra},f)
            
        print(f'Scraped {len(topics)} topics')
    
    os.makedirs('posts/json',exist_ok=True)
    os.makedirs('posts/raw',exist_ok=True)
    os.makedirs('posts/md',exist_ok=True)
    
    # fix filenames, as the slugs can be duplicates, it seems
    for idx,t in enumerate(topics):
        slug = t['slug']
        count = t['posts_count']
        id = t['id']
        
        
        old = f'posts/json/{slug}.json'
        new = f'posts/json/{slug}.{id}.json'
        if os.path.exists(old):
            with open(old,'rb') as f:
                topic = json.load(f)
            if topic['id'] == id and len(topic['post_stream']['posts']) == count:
                print(f'Moving {old} -> {new}')
                os.rename(old,new)
                os.rename(old+'.response',new+'.response')
            
        
    
    for idx,t in enumerate(topics):
        # Unlike the above, there seems to be no more_topics_url, but we can still compare the stream size (listing topic id) with the actual list of posts.
        # If we add ?page=2 we get the second page (page=1 is silently the first page)
        # If we instead specify a post index ../id/post_index.json then we actually get about 5 before that post as well.
        slug = t['slug']
        count = t['posts_count']
        id = t['id']
        
        fn = f'posts/json/{slug}.{id}.json'
        files.append(fn)
        
        if not os.path.exists(f'posts/raw/{slug}.{id}.md'):
            urlretrieve(str(base/f'raw/{id}'),f'posts/raw/{slug}.{id}.md')
            print(idx,"Fetched raw",id,slug,flush=True)
        
        
        if os.path.exists(fn) and not DISABLE_JSON_CACHE:
            # Since the all_topics list is also cached, it will always have the same number of posts here, in theory. So skip the json loading.
                #"""
            with open(fn,'rb') as f:
                topic = json.load(f)
            if topic['id'] == id and len(topic['post_stream']['posts']) == count:
                #"""
                print(idx,'Using cached',slug,id,count,flush=True)
                continue
            
        
        print(idx,'Processing',slug,id,count,flush=True)
            
        page_json = []
        responses = []
        for page in range(math.ceil(count/20)):
            print('\tPage',page+1)
            url = base / 't' / slug / f'{id}.json?page={page+1}'
            r = requests.get(url)
            sleep(0.1 + 0.042523*rand())
            
            # if we have only 1 page we just directly write the content
            if count <= 20:
                with open(f'posts/json/{slug}.json','wb') as f:
                    f.write(r.content)
                with open(f'posts/json/{slug}.json.response','w') as f:
                    f.write(f'Status = {r.status_code}\n{r.headers}')
            else:
                page_json.append(r.json())
                responses.append(f'Status = {r.status_code}\n{r.headers}')
        
        if page_json: # 2+ pages
            combined = mergejson(*page_json)
            with open(fn,'w') as f:
                json.dump(combined,f)
            with open(fn+'.response','w') as f:
                f.write('\n\n------\n\n'.join(responses))
            
                
        #topic2md(slug)
        
        """
        # if count < 20
        url = base / 't' / slug / f'{id}.json'
        r = requests.get(url)
        with open(f'posts/json/{slug}.json','wb') as f:
            f.write(r.content)
            with open(f'posts/json/{slug}.json.response','w') as f:
                f.write(f'Status = {r.status_code}\n{r.headers}')
        topic2md(slug)
        """
              

imagemap = {
    'https://global.discourse-cdn.com/standard17/uploads/urho3d/':'images/uploads/',
    'https://sjc6.discourse-cdn.com/standard17/user_avatar/discourse.urho3d.io/' : 'images/avatars/', #u3d/40/3868_2.png'
    'https://avatars.discourse-cdn.com/' : 'images/avatars/', #v4/letter/g/9e8a1a/40.png'
    'https://emoji.discourse-cdn.com/' : 'images/emoji/',
    'https://cdn.discordapp.com/attachments/' : 'attachments/', # 1011222168958418954/1042120445912158248/Animation12.gif'
    'https://img.youtube.com/':'images/youtube/',
    'https://i.ytimg.com/':'images/youtube/',
    'https://s14.postimg.org/':'images/postimg/', # d6vfc7w3l/Capture_du_2016_12_02_20_17_50.png
    'https://s20.postimg.org/':'images/postimg/', # d6vfc7w3l/Capture_du_2016_12_02_20_17_50.png
    'https://s28.postimg.org/':'images/postimg/', # d6vfc7w3l/Capture_du_2016_12_02_20_17_50.png
    'https://s28.postimg.org/':'images/postimg/', # d6vfc7w3l/Capture_du_2016_12_02_20_17_50.png
    'https://cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/':'images/uploads/aws/',
    'https://i.imgur.com/':'images/imgur/',
    'https://povareshkino.ru/':'images/povareshkino/',#files/userarticles/19527_1cdbe1bd.jpg
    'https://www.indianetzone.com/':'images/indianetzone/'
}

unmapped = []
all_images = []

def img2local(url):
    """ Returns local filename """
    if not url.startswith('http'):
        #print('!!!',url)
        url = 'http:' + url
    for k,v in imagemap.items():
        if url.startswith(k):
            url = v + url[len(k):]

        k = k.replace('https://','http://')
        if url.startswith(k):
            url = v + url[len(k):]
    
    if '://' in url:
        #raise KeyError('Could not map url ' + url)
        # Pray for Leon Hecks
        unmapped.append(url)
        url = url.replace('https://','images/').replace('http://','images/')
        
            
    return url
    

def process_images(htmlstring):
    soup = BeautifulSoup(htmlstring, features='lxml')
    
    # replace all oneboxes before images are done
    obs = soup.find_all(class_="onebox")
    for ob in obs:
        try:
            if ob.find_parents(class_="onebox"):
                continue # let the outer handle it
            elif ob.name == 'a':
                url = ob['href']
            elif "data-onebox-src" in ob:
                url = ob["data-onebox-src"]
            elif ob.find('header') and ob.header.find("a"):
                url = ob.header.a['href']
            elif ob.find('a'):
                url = ob.a['href']
            else:
                raise ValueError("Cannot extract onebox url from %s"%ob)
            
            title = None
            if ob.name == 'a':
                title = ob.get_text().strip()
            #elif "data-onebox-src" in ob:
                #url = ob["data-onebox-src"]
            #elif ob.find('header') and ob.header.find("a"):
                #raise 
            elif ob.find('a'):
                title = ob.select("[title]")
                if title:
                    title = title[0]["title"]
                #else:
                    #raise ValueError("Cannot extract onebox title from %s"%ob)
            
            #else:
                #raise ValueError("Cannot extract onebox title from %s"%ob)
            if not title:
                title = url
                
            
        #try:
            #try:
                #url = ob["data-onebox-src"]
            #except KeyError:
                #try:
                    #url = ob.header.a['href']
                #except:
                    #try:
                        #url = ob.a['href']
                    #except:
                        #print(ob)
                        #raise Exception(str(ob))
                
            a = soup.new_tag('a',href=url,)
            a.string = title
            ob.replaceWith(a)
        except:
            print(f'Failed in {ob}')
            print(soup)
            raise
        
    
    imgs = soup.find_all('img')
    for img in imgs:
        try:
            imgUrl = URL(img['src'])
            fn = imgUrl.parent / imgUrl.query.replace('&',' ') / imgUrl.name
            fn = img2local(str(fn))
            #fn = str(fn).replace('/',' - ')
            print(imgUrl,'->',fn)
            img['src'] = '../../' + fn
        except Exception as e:
            print(type(e),e)
            print(img)
            raise
        
        all_images.append((str(imgUrl), fn))
    #print(soup)
    if soup.body:
        #print(soup.body)
        return soup.body.decode_contents()
    else:
        #print(htmlstring)
        #print(soup)
        return str(soup)
        
    


def topic2md(fname,show=False):
    
    def quote(name,date,textstr):
        textstr = process_images(textstr)
        if 0:
            text = textstr.replace('\n','\n> ')
        else:
            textstr = '<blockquote>%s</blockquote>'%textstr
            #print(textstr)
            text = pypandoc.convert_text(textstr,'markdown','html')
            
        
        date = dateparser.parse(date).strftime('%I:%M:%S%p on %b %d, %Y')
        return f'''
> ---
> 
> ::: **{name}**        *at {date}* :::
> 
> ---
> {text}
'''
    
    """ Parsed json from the topic to markdown """
    with open(fname,'rb') as f:
        topic = json.load(f)
        
    posts = topic['post_stream']['posts']
    quotes ='\n'.join([quote(p['username'],p['created_at'],p['cooked']) for p in posts])
    
        
    val = f'''
# {topic['fancy_title']}

{quotes}
'''

    outname = fname.replace('json','md')
    if not outname.endswith('.md'):
        outname += '.md'
    with open(outname,'w') as f:
        f.write(val)
    
    if show:
        print(val)
    
    
    
    
    
    
#topic2md('random-projects-shots',show=True)
#exit()
posts()

print('Fetched all the JSON')
pprint(files)

print('Converting to markdown and fetching images')

for i,f in enumerate(files):
    try:
        print(i,f,len(files),flush=True)
        topic2md(f)
    except Exception as e:
        print(f,'failed:',type(e),e)
    except requests.exceptions.SSLError as e:
        print(f,'failed:',type(e),e)

for imgUrl,fn in all_images:
    if not os.path.exists(fn):
        try:
            urlretrieve(imgUrl, fn)
            sleep(0.1 + 0.042523*rand())
        except:
            print('Failed on',imgUrl)
            raise
    
print('Unmapped URLs')
pprint(unmapped)
