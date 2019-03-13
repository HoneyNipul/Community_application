// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.controllers' is found in controllers.js
angular.module('starter', ['ionic', 'starter.controllers' , 'ionic-datepicker','base64'])

.directive('fileModel', ['$parse', function ($parse) {
            return {
               restrict: 'A',
               link: function(scope, element, attrs) {
                  var model = $parse(attrs.fileModel);
                  var modelSetter = model.assign;
                  
                  element.bind('change', function(){
                     scope.$apply(function(){
                        modelSetter(scope, element[0].files[0]);
                     });
                  });
               }
            };
         }])

.config(function (ionicDatePickerProvider) {
    var datePickerObj = {
      inputDate: new Date(),
      titleLabel: 'Select a Date',
      setLabel: 'Set',
      todayLabel: 'Today',
      closeLabel: 'Close',
      mondayFirst: false,
      weeksList: ["S", "M", "T", "W", "T", "F", "S"],
      monthsList: ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"],
      templateType: 'popup',
      from: new Date(1800, 8, 1),
      to: new Date(2018, 8, 1),
      showTodayButton: true,
      dateFormat: 'dd MMMM yyyy',
      closeOnSelect: false,
      disableWeekdays: []
    };
    ionicDatePickerProvider.configDatePicker(datePickerObj);
  })


.run(function($ionicPlatform, $rootScope, $state,$animate, AuthService) {

  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);

    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
     'use strict';
        $animate.enabled(false);
    

  });
  
  $rootScope.$on('$stateChangeStart', function (event, toState, toParams) {
    
    if( !AuthService.isLoggedIn() && toState.name != "app.login" )
    {  
      
      event.preventDefault();
      return $state.transitionTo('app.login');
    }
    if( AuthService.isLoggedIn() && toState.name == "app.login" )
    {  
      
      event.preventDefault();
      return $state.transitionTo('app.search');
    }

    

  });

  



})

.config(function($stateProvider, $urlRouterProvider) {
  $stateProvider

    .state('app', {
    url: '/app',
    abstract: true,
    templateUrl: 'templates/menu.html',
    controller: 'AppCtrl',
  

  })

  .state('app.search', {
    cache: false,
    url: '/search',
    views: {
      'menuContent': {
        templateUrl: 'templates/search.html',
        controller:'searchController'
      }
    }
  })

  .state('app.relation', {
    cache: false,
    url: '/relation/:id',
    views: {
      'menuContent': {
        templateUrl: 'templates/relation.html',
        controller:'relationController'
      }
    }
  })

  .state('app.browse', {
      url: '/browse',
      views: {
        'menuContent': {
          templateUrl: 'templates/browse.html'
        }
      }
    })
    .state('app.playlists', {
      url: '/playlists',
      views: {
        'menuContent': {
          templateUrl: 'templates/playlists.html',
          controller: 'PlaylistsCtrl'
        }
      }
    })

     .state('app.eventdetail', {
      url: '/eventdetail',
      views: {
        'menuContent': {
          templateUrl: 'templates/eventdetail.html',
          controller: 'eventdetailController'
        }
      }
    })

    .state('app.Address', {
      url: '/Address',
      views: {
        'menuContent': {
          templateUrl: 'templates/Address.html',
          controller: 'ExampleController'
        }
      }
    })
    .state('app.Dashboard', {
      url: '/Dashboard/:token',
      // data: {
      //   requireLogin:true
      // },
      // params: {
      //   'token':null
      // },
      views: {
        'menuContent': {
          templateUrl: 'templates/Dashboard.html',
          controller: 'DashboardController'
        }
      } 
      
    })
    
   .state('app.Member', {
      url: '/Member/:memberId?',
      views: {
        'menuContent': {
          templateUrl: 'templates/Member.html',
          controller: 'MemberController'
        }
      }
    })

   .state('app.login', {
      url: '/login',
      views: {
        'menuContent': {
          templateUrl: 'templates/login.html',
          controller: 'Logincontroller'
        }
      }

    })
   .state('app.eventRegister', {
      url: '/eventRegister',
      // data:{
      //   requireLogin:true
      // },
      views: {
        'menuContent': {
          templateUrl: 'templates/eventRegister',
          controller: 'eventRegisterController'
        }
      }

    })
   .state('app.invitedList', {
      url: '/invitedList',
      // data:{
      //   requireLogin:true
      // },
      views: {
        'menuContent': {
          templateUrl: 'templates/invitedList',
          controller: 'invitedListController'
        }
      }

    })

  .state('app.single', {
    url: '/playlists/:playlistId',
    views: {
      'menuContent': {
        templateUrl: 'templates/playlist.html',
        controller: 'PlaylistCtrl'
      }
    }
  })
  .state('app.upcomingEvents', {
    url: '/upcomingEvents',
    views: {
      'menuContent': {
        templateUrl: 'templates/upcomingEvents.html',
        controller: 'upcomingEventsController'
      }
    }
  })
  .state('app.Detail', {
    cache: false,
    url: '/Detail/:id',
    views: {
      'menuContent': {
        templateUrl: 'templates/Detail.html',
        controller: 'DetailController'
      }
    }
  });
  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/app/login');
});
