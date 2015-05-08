'use strict';

/**
 * @ngdoc service
 * @name flowApp.Config
 * @description
 * # Config
 * Constant in the flowApp.
 */
angular.module('flowApp')
  .constant('Config', {
    api: "http://192.168.59.103:20010/api/v1",
    open_api: "http://192.168.59.103:20010/open_api"
  });
