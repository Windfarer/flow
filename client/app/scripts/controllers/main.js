'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('MainCtrl', function ($scope, Auth, $location, $mdSidenav, $mdUtil, $log) {
    $scope.showComponent = function () {
      return Auth.isLoggedIn();
    };
    $scope.goToUserProfile = function () {
      $location.path('/user')
    };
    $scope.logout = function () {
      Auth.logout();
      $location.path("/login");
    };
    $scope.toggleSidebar = buildToggler('sidebar');
    function buildToggler(navID) {
      var debounceFn =  $mdUtil.debounce(function(){
        $mdSidenav(navID)
          .toggle()
      },300);
      return debounceFn;
    }
  });
