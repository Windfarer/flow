'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:NavbarCtrl
 * @description
 * # NavbarCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('SidebarCtrl', function ($scope, Auth) {
    $scope.btns = [
      {"name":"INBOX"},
      {"name":"DOING"},
      {"name":"DONE"}
    ];
    $scope.projects = [{
      avatar : '/images/60.jpeg',
      name: 'ProjectA'
    }, {
      avatar : '/images/60.jpeg',
      name: 'ProjectB'
    }, {
      avatar : '/images/60.jpeg',
      name: 'ProjectC'
    }, {
      avatar : '/images/60.jpeg',
      name: 'ProjectD'
    }, {
      avatar : '/images/60.jpeg',
      name: 'ProjectE'
    }];

  });
