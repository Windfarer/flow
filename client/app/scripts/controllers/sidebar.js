'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:NavbarCtrl
 * @description
 * # NavbarCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('SidebarCtrl', function ($scope, $location) {
    $scope.btns = [
      {"name":"INBOX"},
      {"name":"DOING"},
      {"name":"DONE"}
    ];
    $scope.projects = [{
      avatar : '/images/60.jpeg',
      name: 'ProjectA',
      _id: "aaaaatestid"
    }, {
      avatar : '/images/60.jpeg',
      name: 'ProjectA',
      _id: "aaaaatestid"
    }, {
      avatar : '/images/60.jpeg',
      name: 'ProjectA',
      _id: "aaaaatestid"
    }, {
      avatar : '/images/60.jpeg',
      name: 'ProjectA',
      _id: "aaaaatestid"
    }, {
      avatar : '/images/60.jpeg',
      name: 'ProjectA',
      _id: "aaaaatestid"
    }];

    $scope.goToProject = function (project) {
      $location.path('/project/'+project._id)
    }
  });
