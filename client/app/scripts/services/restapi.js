'use strict';

/**
 * @ngdoc service
 * @name flowApp.restAPI
 * @description
 * # restAPI
 * Factory in the flowApp.
 */
angular.module('flowApp')
  .factory('restAPI', function ($resource,Config) {
    // Service logic
    // ...
    var api = Config.api;
    var open_api = Config.open_api;
    // Public API here
    return {
      login: (function () {
        return $resource(open_api+'/login')
      })(),
      register: (function() {
        return $resource(open_api+'/register')
      })(),
      user: (function() {
        return $resource(api+'/users/:user_id',{
          user_id: '@user_id'
        },{
          update: {
            method: 'PUT'
          }
        })
      })(),
      tasks: (function () {
        return $resource(api+'/tasks/:task_id',{
          task_id: '@id'
        },{
          update: {
            method: 'PUT'
          }
        })
      })(),
      projects: (function () {
        return $resource(api+'/projects/:project_id',{
          project_id: '@id'
        },{
          update: {
            method: 'PUT'
          }
        })
      })()
    };
  });
