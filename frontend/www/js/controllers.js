

angular.module('starter.controllers',['ionic','ionic-datepicker','ui.rCalendar','ui.bootstrap','ngAnimate'])

.controller('AppCtrl', function() {
   
 var authToken;
 var username;
 var isAuthenticated;
})

.controller('Logincontroller', function($rootScope,$state, $scope, $timeout, $http, AuthService) {


   var isAuthenticated = false;
   var authToken = '';

  $scope.submit = function( ) { 
       AuthService.login(this.username, this.Password).then(function(){
           $state.go('app.search');
       });       
    }
})

.controller('PlaylistsCtrl', function($scope) {
  $scope.playlists = [
    { title: 'Reggae', id: 1 },
    { title: 'Chill', id: 2 },
    { title: 'Dubstep', id: 3 },
    { title: 'Indie', id: 4 },
    { title: 'Rap', id: 5 },
    { title: 'Cowbell', id: 6 }
  ];
})

.controller('eventdetailController', function($scope,$http) {

  $http.get("http://localhost:8000/api/eventDetails")
      .then(function (response) {
               alert("response");
        })
 

})
 



.controller('ExampleController', function($rootScope,$scope, $http, $state) {

   $scope.submit = function(){
  
   
    $http.post("http://localhost:8000/api/add_address",{"address_line1":this.Addressline1,"address_line2":this.Addressline2,"landmark":this.Landmark,"area":this.Area,"city":this.City,"state":this.State, "country":this.country, "postal_code":this.Postalcode, "phone_number1":this.Phonenumber1, "phone_number2":this.Phonenumber2})
    .then(function(response){
        
          
          $rootScope.addressId = response.data["id"];
          alert($rootScope.addressId);
          $state.go('app.Member');
    });
  }
  
})
.controller('upcomingEventsController', function($rootScope,$scope, $http, $state) {

     'use strict';

       


        $scope.calendar = {};
        $scope.monthviewEventDetailTemplateUrl = "";
        $scope.changeMode = function (mode) {
            $scope.calendar.mode = mode;
        };

        $scope.loadEvents = function () {
             createRandomEvents();
            
        };

        $scope.selectedDate = {};

        $scope.onEventSelected = function (event) {
            console.log('Event selected:' + event.startTime + '-' + event.endTime + ',' + event.title + ',' + event.discription);
        };

        $scope.onViewTitleChanged = function (title,discription) {
            $scope.viewTitle = title;
            $scope.viewDiscription = discription;
        };

        $scope.today = function () {
            $scope.calendar.currentDate = new Date();
        };

        $scope.isToday = function () {
            var today = new Date(),
                currentCalendarDate = new Date($scope.calendar.currentDate);

            today.setHours(0, 0, 0, 0);
            currentCalendarDate.setHours(0, 0, 0, 0);
            return today.getTime() === currentCalendarDate.getTime();
        };

        $scope.onTimeSelected = function (selectedTime, events, disabled) {
            //console.log('Selected time: ' + selectedTime + ', hasEvents: ' + (events !== undefined && events.length !== 0) + ', disabled: ' + disabled);            
            $scope.selectedDate.events = events;
        };

        function createRandomEvents() {

           var startTime;
           
           $http.get("http://localhost:8000/api/eventDetails/6/")
            .then(function (response) {
              $scope.events=response.data;

              $scope.calendar.eventSource=displayEvent($scope.events);

           })     
        }

        function displayEvent(events){
           var startTime;
           var endTime;

           var event1 = [];

           angular.forEach(events, function(event,key){

              console.log(event);
               console.log(event[3]);
               startTime = new Date(event[3]);
               console.log(startTime);
              
               endTime = new Date(event[4]);
               

              event1.push({
                title: event[1],
                discription:event[2],
                startTime: startTime,
                endTime: endTime,
              }) 

           })
           return event1;
        }


  
})

.controller('DashboardController', function($rootScope,$scope, $http, $state) {
   
      $scope.destroyCredentials = function(){
        $rootScope.authToken = undefined;
        $rootScope.username = '';
        $rootScope.isAuthenticated = false;
        $http.defaults.headers.common.Authorization = undefined;
        alert(window.localStorage.removeItem('currentUser'));


      }
   $scope.logout = function(){
    $scope.destroyCredentials();
   }
})



.controller('MemberController', function($rootScope,$scope,$stateParams, $http, $state,$base64,ionicDatePicker) {

    var ipObj1 = {
        callback: function (val) {  
          console.log('Return value from the datepicker popup is : ' + val, new Date(val));
        },
        disabledDates: [            //Optional
          new Date(2016, 2, 16),
          new Date(2015, 3, 16),
          new Date(2015, 4, 16),
          new Date(2015, 5, 16),
          new Date('Wednesday, August 12, 2015'),
          new Date("08-16-2016"),
          new Date(1439676000000)
        ],
        from: new Date(1800, 1, 1), //Optional
        to: new Date(2017, 10, 30), //Optional
        inputDate: new Date(),      //Optional
        mondayFirst: true,          //Optional
        disableWeekdays: [],       //Optional
        closeOnSelect: false,       //Optional
        templateType: 'popup'       //Optional
    };

    $scope.openDatePicker = function(){
        ionicDatePicker.openDatePicker(ipObj1);
    };

    $scope.showMemberform=true;
    var addressId=null;
     $scope.newForm = function(){ 
        $scope.showMemberform=false;
        console.log("yes",$scope.showMemberform);
     } 
    $scope.addressSubmit = function(){
      $http.post("http://localhost:8000/api/add_address",{"address_line1":this.Addressline1,"address_line2":this.Addressline2,"landmark":this.Landmark,"area":this.Area,"city":this.City,"state":this.State, "country":this.country, "postal_code":this.Postalcode, "phone_number1":this.Phonenumber1, "phone_number2":this.Phonenumber2})
      .then(function(response){
            addressId = response.data["id"];
            alert(addressId);
            $scope.showMemberform=true;      
      });
    }
     
    $scope.isMemberExist=false;
      if($stateParams.memberId>0)
        {
          $scope.isMemberExist=true
        }

    function getDataUriFromImg(file,callback){
      var filesSelected = document.getElementById("inputFileToLoad").files;
      if (filesSelected.length > 0)
      {
          var fileToLoad = filesSelected[0];
   
          var fileReader = new FileReader();
   
          fileReader.onload = function(fileLoadedEvent) 
          {
             callback(fileLoadedEvent.target.result);
          };
   
          fileReader.readAsDataURL(fileToLoad);
      }
    }

    function saveProfileData(dataUri){
        data = {"address":addressId, "first_name":$scope.First_name, "middle_name": $scope.Middle_name, "last_name": $scope.Last_name, "username": $scope.Username, "password": $scope.Password, "gender" :$scope.gender, "birth_date": $scope.Birthdate, "email": $scope.Email, "occupation": $scope.Occupation, "marital_status": $scope.status, "mobile_number1": $scope.Phonenumber1, "mobile_number2":$scope.Phonenumber2, "office_number": $scope.officenumber};
        if( dataUri )
            data['photo'] = dataUri;
        if($scope.isMemberExist){
           data['relation'] = $scope.relation;
           data['currentMemberId'] = parseInt($stateParams.memberId);
        }

        $http.post("http://localhost:8000/api/add_member",data)
        .then(function(response){
            $state.go('app.Detail',{id:response.data["id"]});
        });
    }

    $scope.submit = function(){        

        //$scope.myFile =$base64.encode($scope.myFile);

        if( document.getElementById("inputFileToLoad").files.length > 0 ){
          this.Myfile = getDataUriFromImg($scope.myFile,saveProfileData);  
        }        
        else
          saveProfileData();
    }

  })




 .controller('DetailController', function($rootScope, $scope, $stateParams, $http, $state,$stateParams,relationManager) {
      alert($stateParams.id);
      $http.get("http://localhost:8000/api/member_detail/"+$stateParams.id+"/")
      .then(function (response) {
        $scope.member = response.data; 
        $http.post("http://localhost:8000/api/searchRelation",{"member":$scope.member.id})
        .then(function(response){
          $scope.relationCount = response.data;
        })
       
      })
      
        $scope.showRelations = function(){
          relationManager.setCurrentMember($scope.member);
          window.setTimeout(function(){
            $state.go('app.relation',{'id':$scope.member.id});
          },0);
        }

        $scope.newFamilyMember = function(){            
         $state.go('app.Member',{memberId:$stateParams.id})
        }  
  })


  .controller('searchController', function($scope, $stateParams, $http) {
    $scope.shows=[];  
    //for converting array into object
    function toObject(arr) {
      var rv = {};
      for (var i = 0; i < arr.length; ++i)
        rv[i] = arr[i];
      return rv;
    } 
    $scope.submit = function(){
      $http.post("http://localhost:8000/api/search",{"first_name":this.Name, "middle_name":this.Name, "last_name":this.Name})
      .then(function(response){
        //for converting array into object
       /* angular.forEach(response.data,function(value,index){
          $scope.shows.push(toObject(value));
        });*/
       $scope.shows=response.data;
        console.log($scope.shows);
        
        return false;
      })
    }
  })

.controller('relationController', function($scope, $stateParams, $state,$http,relationManager) {
    $scope.current = relationManager.getCurrentMember(); 

    window.setTimeout(function(){
           $http.post("http://localhost:8000/api/findRelatedPerson",{"member":$scope.current.id})
           .then(function(response){
            $scope.relatedPersonDetails = response.data;
            console.log($scope.relatedPersonDetails);
          })
    },0);

    $scope.callDetails = function(example){
          $state.go('app.Detail',{id:example});
    }     
})

.controller('eventRegisterController', function($scope, $stateParams, $state,ionicDatePicker) {

    var ipObj1 = {
        callback: function (val) {  
          console.log('Return value from the datepicker popup is : ' + val, new Date(val));
        },
        disabledDates: [            //Optional
          new Date(2016, 2, 16),
          new Date(2015, 3, 16),
          new Date(2015, 4, 16),
          new Date(2015, 5, 16),
          new Date('Wednesday, August 12, 2015'),
          new Date("08-16-2016"),
          new Date(1439676000000)
        ],
        from: new Date(1800, 1, 1), //Optional
        to: new Date(2017, 10, 30), //Optional
        inputDate: new Date(),      //Optional
        mondayFirst: true,          //Optional
        disableWeekdays: [],       //Optional
        closeOnSelect: false,       //Optional
        templateType: 'popup'       //Optional
    };

    $scope.openDatePicker = function(){
        ionicDatePicker.openDatePicker(ipObj1);
    };
   
    $scope.add = function(){
      $state.go('app.invitedList');
    }
    $scope.submit = function(){
       $http.post("http://localhost:8000/api/search",{"event_name":this.event_name,"event_description":this.event_description,"event_type":this.event_type,"start_date":this.startDate,"end_date":this.endDate})

    }
   

})

.controller('invitedListController', function($scope, $stateParams) {

   $scope.submit = function(){
      $http.post("http://localhost:8000/api/search",{"first_name":this.Name, "middle_name":this.Name, "last_name":this.Name})
      .then(function(response){
        //for converting array into object
       /* angular.forEach(response.data,function(value,index){
          $scope.shows.push(toObject(value));
        });*/
       $scope.shows=response.data;
        //console.log($scope.shows);
        
        return false;
      })
    }
     $scope.list=[];
    $scope.add = function(show){
      alert(show);
      $scope.list.push(this.show);
      console.log($scope.list);
      http.post("http://localhost:8000/api/",{"first_name":this.Name, "middle_name":this.Name, "last_name":this.Name})
    }
    

})
.controller('PlaylistCtrl', function($scope, $stateParams) {
});
