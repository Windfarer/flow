'use strict';

angular.module('flowApp')

  .constant('ACCESS_LEVELS', {
    pub: 1,
    user: 2
  })

  .config(function($httpProvider){
    var interceptor = function($q, $rootScope, Auth, Config, $location){
      return {
        'response': function(resp) {
          if (resp.config.url === Config.open_api+'/login') {
            console.log(resp);
            Auth.setUser(resp.data);
          }
          return resp;
        },
        'responseError': function(rejection) {
          switch(rejection.status) {
            case 401:
              if (rejection.config.url !== Config.open_api+'/login')
                Auth.logout();
                console.log("login_required");
                $location.path("login");
                $rootScope.$broadcast('auth:loginRequired');
              break;
            case 403:
              $rootScope.$broadcast('auth:forbidden');
              console.log("forbidden");
              break;
            case 404:
              $rootScope.$broadcast('page:notFound');
              console.log("notfound");
              break;
            case 500:
              $rootScope.$broadcast('server:error');
              console.log("error");
              break;
            }
          return $q.reject(rejection);
        }
      }
    };
    $httpProvider
      .interceptors.push(interceptor);
  })


  .config(function($httpProvider) {
    var interceptor = function($q, $rootScope, Auth) {
      return {
        'request': function(req) {
          req.headers = req.headers || {};
          if (Auth.isLoggedIn() && !req.headers.Authorization) {
            req.headers.Authorization = Auth.getToken();
          }

          return req;
        },
        'requestError': function(reqErr) {
          return reqErr;
        }
      }
    };
    $httpProvider
      .interceptors.push(interceptor);
  });
