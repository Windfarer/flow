'use strict';

/**
 * @ngdoc function
 * @name flowApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the flowApp
 */
angular.module('flowApp')
  .controller('ToolbarCtrl', function ($scope, $timeout, $mdSidenav, $log) {
    $scope.toggleLeft = buildToggler('left');
    /**
     * Build handler to open/close a SideNav; when animation finishes
     * report completion in console
     */
    function buildToggler(navID) {
      return function() {
        return $mdSidenav(navID).toggle()
          .then(function () {
            $log.debug("toggle " + navID + " is done");
          });
      }
    }
  });
