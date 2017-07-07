import requests


global APP_ACCESS_TOKEN
APP_ACCESS_TOKEN='5689237295.0705f6a.21cd24d2701a46a5a625358c35071320'
global BASE_URL
BASE_URL='https://api.instagram.com/v1/'


#function to fetch user's details
# https://api.instagram.com/v1/users/{user-id}/?access_token=ACCESS-TOKEN
def self_info():
  request_url=BASE_URL+'users/self/?access_token=%s' % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
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

# function to fetch another user's details
# https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
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
# https://api.instagram.com/v1/users/{user-id}/?access_token=ACCESS-TOKEN
def another_user_detail(username):
  if username==None:
    print "Entered username is invalid"
  else:
    user_id=get_user_id(username)
    if user_id == None:
      print "Username not found"
    else:
      request_url = BASE_URL + 'users/%s/?access_token=%s' % (user_id,APP_ACCESS_TOKEN)
      print 'GET request url : %s' % (request_url)
      user_info = requests.get(request_url).json()
      if user_info['meta']['code'] == 200:
        if len(user_info['data']):
          print 'Username = %s' % (user_info['data']['username'])
          print 'Full Name =%s' % (user_info['data']['full_name'])
          print 'Bio =%s' % (user_info['data']['bio'])
          print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
          print 'No. of people following %s: %s' % ((user_info['data']['full_name']),user_info['data']['counts']['follows'])
          print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
          print 'No data is available for the searched user'

      else:
        print 'Status code other than 200 received'















