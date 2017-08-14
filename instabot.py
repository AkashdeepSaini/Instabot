import requests,urllib
import numpy as np
import matplotlib.pyplot as plt


global APP_ACCESS_TOKEN,BASE_URL

BASE_URL='https://api.instagram.com/v1/'


#function to fetch user's details

def self_info():
  request_url=BASE_URL+'users/self/?access_token=%s' % (APP_ACCESS_TOKEN)

  user_info = requests.get(request_url).json()

  if user_info['meta']['code']==200:
    if len(user_info['data']):
      print 'Username = %s' %(user_info['data']['username'])
      print 'Full Name =%s' %(user_info['data']['full_name'])
      print 'Bio =%s' % (user_info['data']['bio'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
    else:
      print 'User does not exist'

  else:
      print 'Status code other than 200 received'

# function to get user id from username

def get_user_id(username):
  request_url=BASE_URL+'users/search?q=%s&access_token=%s' % (username,APP_ACCESS_TOKEN)
  user_info = requests.get(request_url).json()
  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      return user_info['data'][0]['id'] # to fetch the details of first user with given username
    else:
      return None
  else:
    print 'Status code other than 200 received!'
    exit()


#function to fetch details of another user

def another_user_detail(username):
  if username==None:
    print "Entered username is invalid"
  else:
    user_id=get_user_id(username)
    if user_id == None:
      print "Username not found"
    else:
      request_url = BASE_URL + 'users/%s/?access_token=%s' % (user_id,APP_ACCESS_TOKEN)

      user_info = requests.get(request_url).json()
      if user_info['meta']['code'] == 200:
        if len(user_info['data']):
          print 'Username = %s' % (user_info['data']['username'])
          print 'Full Name =%s' % (user_info['data']['full_name'])
          print 'Bio =%s' % (user_info['data']['bio'])
          print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
          print 'No. of people %s is following : %s' % ((user_info['data']['full_name']),user_info['data']['counts']['follows'])
          print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
          print 'No data is available for the searched user'

      else:
        print 'Status code other than 200 received'



#function to download user recent post

def user_recent_post():
  request_url=BASE_URL+'users/self/media/recent/?access_token=%s' %(APP_ACCESS_TOKEN)

  user_media = requests.get(request_url).json()
  if user_media['meta']['code'] == 200:
    if len(user_media['data']):
      image_name = user_media['data'][0]['id'] + '.jpeg'
      image_url = user_media['data'][0]['images']['standard_resolution']['url']
      urllib.urlretrieve(image_url, image_name)
      print 'Your image has been downloaded! and image id is %s' %(user_media['data'][0]['id'])
    else:
      print 'Post does not exist!'
  else:
    print 'Status code other than 200 received!'

# function to get media id from username
def get_media_id(username):
  user_id=get_user_id(username)
  if user_id==None:
      print 'no such user exists'
      exit()
  else:
     request_url=BASE_URL+'users/%s/media/recent/?access_token=%s'%(user_id,APP_ACCESS_TOKEN)
     user_media = requests.get(request_url).json()
     if user_media['meta']['code'] == 200:
         if len(user_media['data']):
           return user_media['data'][0]['id']
         else:
           print 'No recent post'
           exit()
     else:
       print 'Status code other than 200 received!'
       exit()

#downloads recent media of a user (self)
def user_recent_media(username):
  user_id=get_user_id(username)
  if user_id==None:
    print "No such user exists"
  else:
    request_url = BASE_URL + 'users/%s/media/recent/?access_token=%s' % (user_id, APP_ACCESS_TOKEN)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
      if len(user_media['data']):
        image_name = user_media['data'][0]['id'] + '.jpeg'
        image_url = user_media['data'][0]['images']['standard_resolution']['url']
        urllib.urlretrieve(image_url, image_name)
        print 'Your image has been downloaded! and image id is %s' % (user_media['data'][0]['id'])
      else:
        print 'Post does not exist!'
    else:
      print 'Status code other than 200 received!'


# downloads recent media liked by a user
def recent_media_liked():
  request_url = BASE_URL + 'users/self/media/liked/?access_token=%s' % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_media = requests.get(request_url).json()
  if user_media['meta']['code'] == 200:
    if len(user_media['data']):
      image_name = user_media['data'][0]['id'] + '.jpeg'
      image_url = user_media['data'][0]['images']['standard_resolution']['url']
      urllib.urlretrieve(image_url, image_name)
      print 'Your image has been downloaded! and image id is %s' % (user_media['data'][0]['id'])
    else:
      print 'Post does not exist!'
  else:
    print 'Status code other than 200 received!'


def like_a_post(username):
    media_id = get_media_id(username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}

    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
      print 'Your like was unsuccessful. Try again!'



#generates list of comments
def get_comments_list(username):
  media_id=get_media_id(username)
  if media_id==None:
    print "Post does not exist"
    exit()
  else:
    request_url=BASE_URL+'media/%s/comments?access_token=%s' %(media_id,APP_ACCESS_TOKEN)
    user_comment = requests.get(request_url).json()
    if user_comment['meta']['code']==200:
      if len(user_comment['data']):

        length=len(user_comment['data'])
        i=0
        while(length):
            print "comment:%d %s" % (i+1,user_comment['data'][i]['text'])
            i=i+1
            length=length-1
      else:
        print 'no comments'
    else:
      print 'Status code other than 200 received!'



#generates list of the people who have liked the media
def people_list(username):
  media_id = get_media_id(username)
  if media_id == None:
    print "Post does not exist"
    exit()
  else:
    request_url = BASE_URL + 'media/%s/likes?access_token=%s' % (media_id, APP_ACCESS_TOKEN)
    likes = requests.get(request_url).json()
    if likes['meta']['code'] == 200:
      if len(likes['data']):

        length = len(likes['data'])
        i = 0
        print "Total no of likes %s" %(length)
        while (length):
          print "username:%d %s" % (i + 1, likes['data'][i]['username'])
          i = i + 1
          length = length - 1
      else:
        print 'no comments'
    else:
      print 'Status code other than 200 received!'



# funtion to post a comment
def post_a_comment(username):
    media_id = get_media_id(username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url, payload).json()

    if make_comment['meta']['code'] == 200:
        print "Successfully added a new comment!"
    else:
      print "Unable to add comment. Try again!"




# empty list
hash_tag_name=[]
count=[]

#function to search media over instagram having similar tags
def hash_tag(name_of_tag):
  request_url=BASE_URL+'tags/search?q=%s&access_token=%s' %(name_of_tag,APP_ACCESS_TOKEN)
  info = requests.get(request_url).json()
  if info['meta']['code']==200:
    if len(info['data']):
       length = len(info['data'])
       print 'Total no of tags found %s' %(length)
       i = 0
       while (length):
          print "name = %s    count=%s " % (info['data'][i]['name'], info['data'][i]['media_count'])
          hash_tag_name.append(info['data'][i]['name'])
          count.append(info['data'][i]['media_count'])

          i = i + 1
          length = length - 1


       tuple(hash_tag_name)

       y_pos = np.arange(len(hash_tag_name))


       plt.bar(y_pos, count, align='center', alpha=0.5)
       plt.xticks(y_pos, hash_tag_name, rotation=90)
       plt.ylabel('Media Counts')
       plt.title('Types of media with similar hashtag ')
       plt.show()
    else:
      print "No media with such hashtag is found"


  else:
    print 'Status code other than 200 received!'
    exit()



#function to find recently uploaded media having tag entered by the user
def hash_tag1(name_of_tag):


  request_url=BASE_URL+'tags/%s/media/recent?access_token=%s' %(name_of_tag,APP_ACCESS_TOKEN)
  info = requests.get(request_url).json()
  if info['meta']['code']==200:



      no_of_images=0
      no_of_videos=0
      other_media=0
      i=0
      if len(info['data']):
          total_length=len(info['data'])

          while (total_length):
              if (info['data'][i]['type']=="image"):
                 no_of_images=no_of_images+1
              elif(info['data'][i]['type']=="video"):
                 no_of_videos=no_of_videos+1
              else:
                 other_media=other_media+1
              total_length=total_length-1
              i=i+1
          objects = ('images', 'videos', 'other')
          # tuple(objects)
          counts = [no_of_images, no_of_videos, other_media]
          y_pos = np.arange(len(objects))

          plt.bar(y_pos, counts, align='center', alpha=0.5)
          plt.xticks(y_pos, objects, rotation=90)
          plt.ylabel('Media Counts')
          plt.title("Types of media ")
          plt.show()
          print "Total number of images %s" %(no_of_images)
          print "Total number of videos %s" % (no_of_videos)
          print "Total number of other media %s" % (other_media)
      else:
       print "No media with such hashtag is found"


  else:
     print 'Status code other than 200 received!'
     exit()




def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get the recent post of a user by username\n"
        print "e.Get a list of people who have liked the recent post of a user\n"
        print "f.Like the recent post of a user\n"
        print "g.Get a list of comments on the recent post of a user\n"
        print "h.Make a comment on the recent post of a user\n"
        print "i.To generate bar graph depicting media having similar hashtag\n"
        print "j.To generate bar graph depicting types of media(recently added) having enetered  hashtag\n"
        print "k.Exit"

        choice = raw_input("Enter your choice: ")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            if insta_username=="":
                print 'enter a valid username'
            else:
                another_user_detail(insta_username)
        elif choice == "c":
            user_recent_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            if insta_username=="":
                print 'enter a valid username'
            else:
                user_recent_media(insta_username)
        elif choice=="e":
           insta_username = raw_input("Enter the username of the user: ")
           if insta_username == "":
               print 'enter a valid username'
           else:
               people_list(insta_username)
        elif choice=="f":
           insta_username = raw_input("Enter the username of the user: ")
           if insta_username == "":
               print 'enter a valid username'
           else:
               like_a_post(insta_username)
        elif choice=="g":
           insta_username = raw_input("Enter the username of the user: ")
           if insta_username == "":
               print 'enter a valid username'
           else:
               get_comments_list(insta_username)
        elif choice=="h":
           insta_username = raw_input("Enter the username of the user: ")
           if insta_username == "":
               print 'enter a valid username'
           else:
               post_a_comment(insta_username)
        elif choice=="i":
           hashtag = raw_input("Enter the hashtag: ")
           if hashtag == "":
               print 'enter a valid tag'
           else:
              hash_tag(hashtag)
        elif choice=="j":
            hashtag = raw_input("Enter the hashtag: ")
            if hashtag=="":
                print 'enter a valid tag'
            else:
              hash_tag1(hashtag)
        elif choice == "k":
            exit()
        else:
            print "wrong choice"



start_bot()









