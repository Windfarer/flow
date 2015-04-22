'use strict';

/**
 * @ngdoc overview
 * @name flowApp
 * @description
 * # flowApp
 *
 * Main module of the application.
 */
angular
  .module('flowApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'ngMaterial',
    'ngMessages'
  ])
  .config(function ($routeProvider, ACCESS_LEVELS) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/task.html',
        controller: 'TaskCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/login', {
        templateUrl: 'views/login.html',
        controller: 'LoginCtrl',
        access_level: ACCESS_LEVELS.pub
      })
      .when('/register', {
        templateUrl: 'views/register.html',
        controller: 'RegisterCtrl',
        access_level: ACCESS_LEVELS.pub
      })
      .when('/group', {
        templateUrl: 'views/group.html',
        controller: 'GroupCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/task', {
        templateUrl: 'views/task.html',
        controller: 'TaskCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/user', {
        templateUrl: 'views/user.html',
        controller: 'UserCtrl',
        access_level: ACCESS_LEVELS.user
      })
      .when('/landing', {
        templateUrl: 'views/landing.html',
        controller: 'LandingCtrl',
        access_level: ACCESS_LEVELS.pub
      })
      .otherwise({
        redirectTo: '/'
      });
  });
