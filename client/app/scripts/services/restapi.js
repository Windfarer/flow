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
      tasks: (function () {
        return $resource(api+'/tasks');
      })(),
      task: (function () {
        return $resource(api+'/task/:task_id',{
          task_id: '@'
        })
      })(),
      groups: (function () {
        return $resource(api+'/groups');
      })(),
      group: (function () {
        return $resource(api+'/group/:group_id',{
          group_id: '@'
        })
      })()
    };
  });
