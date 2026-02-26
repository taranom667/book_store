import time
from http.client import HTTPResponse


class CustomMiddleware(object):
     def __init__(self,get_response):
         self.get_response = get_response


     def __call__(self, request):


        start_time=time.time()

        response = self.get_response(request)
        duration=time.time()-start_time
        print(f"request time:{duration}")

        return response







'''  def process_request(self, request):
        # Check if the request is for the login or logout views
        if request.path == '/login/':
            # Handle login logic
            print("Login Request")
            # You can perform any additional actions related to login here

        elif request.path == '/logout/':
            # Handle logout logic
            print("Logout Request")
            # You can perform any additional actions related to logout here
        elif request.path == '/admin/':
            print("Admin")
'''
'''     def process_request(self,request):
         if request.path == '/login/':
             return print('login request')
         elif request.path == '/logout/':
             print("Logout Request")
         elif request.path == '/admin/':
             print("Admin")

     def process_response(self,request,response):
         pass
'''