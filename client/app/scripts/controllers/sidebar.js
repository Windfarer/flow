'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:NavbarCtrl
 * @description
 * # NavbarCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('SidebarCtrl', function ($scope, $location, restAPI, $mdSidenav) {
    $scope.projects = restAPI.projects.query();
    $scope.editProject = function (project) {
      $location.path('/project/'+project.id);
      $mdSidenav('sidebar').close()
    };
    $scope.goToProject = function (project) {
      $location.path('/task/project/'+project.id);
      $mdSidenav('sidebar').close()
    };
    $scope.goToPersonal = function () {
      $location.path('/task');
      $mdSidenav('sidebar').close()
    };
    $scope.createProject = function () {
      $location.path("/project/new");
      $mdSidenav('sidebar').close();
    };
  });
