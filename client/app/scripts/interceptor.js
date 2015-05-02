'use strict';

angular.module('flowApp')

  .constant('ACCESS_LEVELS', {
    pub: 1,
    user: 2
  })

  .config(function($httpProvider){
    var intercepter = function($q, $rootScope, Auth, Config, $location){
      return {
        'response': function(resp) {
          if (resp.config.url == Config.open_api+'/login') {
            Auth.setUser(resp.data);
            //console.log("savvvvvvvvvvvvving")
          }
          return resp;
        },
        'responseError': function(rejection) {
          console.log(rejection);
          switch(rejection.status) {
            case 401:
              if (rejection.config.url !== Config.open_api+'/login')
                Auth.logout();
                console.log("login_required");
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
      .interceptors.push(intercepter);
  })

  .config(function($httpProvider) {
    var intercepter = function($q, $rootScope, Auth) {
      return {
        'request': function(req) {
          req.params = req.params || {};
          if (Auth.isAuthoized() && !req.params.token) {
            req.params.token = Auth.getToken();
          }
          return req;
        },
        'requestError': function(reqErr) {
          return reqErr;
        }
      }
    };
    $httpProvider
      .interceptors.push(intercepter);
  });
