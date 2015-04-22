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
    api: "http://localhost:5000/api/v1/",
    open_api: "http://localhost:5000/open_api"
  })
  .config(function($mdThemingProvider) {
    $mdThemingProvider.theme('blue')
      .primaryPalette('blue')
      .accentPalette('red')
      .backgroundPalette('grey')
  });

