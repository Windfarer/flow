'use strict';

/**
 * @ngdoc service
 * @name flowApp.auth
 * @description
 * # auth
 * Service in the flowApp.
 */
angular.module('flowApp')
  .factory('Auth', function ($cookieStore, ACCESS_LEVELS) {
    var _user = $cookieStore.get('user');
    //if (!_user) {
    //  var _user = {};
    //  _user.role = ACCESS_LEVELS.pub;
    //}
    var setUser = function(user) {
      if (!user.role || user.role < 0) {
        user.role = ACCESS_LEVELS.pub;
      }
      _user = user;
      $cookieStore.put('user', _user);
    };

    return {
      isAuthoized: function(level) {
        console.log('current_user:');
        console.log(_user);
        if (!_user) {
          return false;
        }
        return _user.role >= level;
      },
      setUser: setUser,
      isLoggedIn: function() {
        return _user ? true : false;
      },
      getUser: function() {
        return _user;
      },
      getId: function() {
        return _user ? _user._id : null;
      },
      getToken: function() {
        return _user ? _user.token : ''
      },
      logout: function() {
        $cookieStore.remove('user');
        _user = null;
      }
    };
  });
