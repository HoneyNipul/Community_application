angular.module('starter')

.service('AuthService',function($q, $http) {
	var token = '';
	var username ='';
	var isAuthenicated = false;
	var role = '';
	var authToken;

   var userCredentials = function(token){
		isAuthenticated = true;
		authToken = token;

		$http.defaults.headers.common.Authorization = authToken;

	}

   /*function loadUserCredentials(){
   	 var token =windows.localStorage.getItem(currentUser.MycommunityT);
   	 if (token){
   	 	userCredentials(token);
   	 }
   }*/
   var storeUserCredentials = function(token,username){
		localStorage.setItem('currentUser', JSON.stringify({ MycommunityU:username, MycommunityT:token }));
		userCredentials(token);
	}

	function destroyUserCredentials(){
		authToken = undefined;
		username = '';
		isAuthenticated = false;
		$http.defaults.headers.common.Authorization = undefined;
		windows.localStorage.removeItem('currentUser');

	}

   this.login = function(username, password){
   	         return $q(function(resolve,reject){
   	              alert(username);
   	              $http.post("http://localhost:8000/api/api-token-auth/",{"username": username, "password": password, "test":"test"})
                  .success(function(response){ 
        	         token = response.token;
                     storeUserCredentials(token, username);
                     resolve('login success');
                   }).error(function(){
                           reject('login failed');
                      })
   	         })
            
	 }
     

	 this.logout =function(){
	 	destroyUserCredentials();
	 }
     
      this.isLoggedIn = function(){
     	return localStorage.getItem('currentUser') != null ? true : false;
     }



         

	// return{
	// 	login:login,
	// 	logout:logout,

	// 	//isAuthorized: isAuthorized,
	// 	//isAuthenticated: function(){return isAuthenticated;},
	// 	//username: function(){return username;}
	// 	};
})

.service('relationManager',function($q,$http){

    var currentMember = {};

    this.setCurrentMember = function(member){
    	this.currentMember = member;
    }

    this.getCurrentMember = function(){
    	return this.currentMember;
    }

})