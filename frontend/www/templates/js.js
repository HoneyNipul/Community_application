 * detailController
 $http.get("http://localhost:8000/api/member_detail/"+$rootScope.id)
   .then(function (response) {
    $scope.Member = response.data; 
  })

   $scope.newMember = function(id){
        $rootScope.currentMember = response.data["id"];
         $state.go('app.Member');
      /* $window.variable1=true;
      //$rootScope.addNewMember = true;
       //$rootScope.addNewMember = dataService.addNewMember;
       // addNewMember=true;
      
     
      console.log($window.variable1);
       
      
      //$location.path('/Member');
      // $window.location= '/Member';
     
    } 
   $scope.newForm = function(){
    $state.go('app.Address');
     /*$location.path('/Address');*/
     
    } 

    $scope.submit = function(){
     
     /*alert($rootScope.addressId);*/
   
     data = {"address":this.addressId, "first_name":this.First_name, "middle_name": this.Middle_name, "last_name": this.Last_name, "username": this.Username, "password": this.Password, "gender" :this.gender, "birth_date": this.Birthdate, "email": this.Email, "occupation": this.Occupation, "marital_status": this.status, "mobile_number1": this.Phonenumber1, "mobile_number2":this.Phonenumber2, "office_number": this.officenumber, "photo": this.photo};
     //console.log(data); 
     $http.post("http://localhost:8000/api/add_member",data)
    .then(function(response){

      console.log(response);  
      $rootScope.id = response.data["id"];
      alert($rootScope.id);
       // $state.go('app.Detail');
    })
    

    **Membercontroller
      // console.log($rootScope.addNewMember);
    // $rootScope.addNewMember = dataService.addNewMember;
     //alert(addNewMember)
    
   $scope.newForm = function(){
    $state.go('app.Address');
     /*$location.path('/Address');*/
     
    } 
    /* $scope.showdiv = function(){
      $scope.templateUrl ='templates/Address.html'
    };*/
        
    $scope.submit = function(){
     
     /*alert($rootScope.addressId);*/
    
     data = {"address":this.addressId, "first_name":this.First_name, "middle_name": this.Middle_name, "last_name": this.Last_name, "username": this.Username, "password": this.Password, "gender" :this.gender, "birth_date": this.Birthdate, "email": this.Email, "occupation": this.Occupation, "marital_status": this.status, "mobile_number1": this.Phonenumber1, "mobile_number2":this.Phonenumber2, "office_number": this.officenumber, "photo": this.photo};
     //console.log(data); 
     $http.post("http://localhost:8000/api/add_member",data)
    .then(function(response){

      console.log(response);  
      $rootScope.id = response.data["id"];
        $state.go('app.Detail');



      /*var person1 ={};
       person1=response.data["id"];
      alert(person1 );
       //alert($rootScope.id);
       data ={"member_id":this.person1.id}
       console.log(data);
       $http.post("http://localhost:8000/api/add_relation")
       $scope.Member = response.data;
       //$scope.MemberForm.$setPristine();
       //$scope.MemberForm.$setUntouched();*/
    

    });
    }

   /*  console.log($window.variable1);
    if($window.variable1 == true){

      $scope.Member.first_name='';   
    }*/

    **add detailController

    $scope.submit = function(){
  
    /*console.log(jObj)*/
    $http.post("http://localhost:8000/api/add_address",{"address_line1":this.Addressline1,"address_line2":this.Addressline2,"landmark":this.Landmark,"area":this.Area,"city":this.City,"state":this.State, "country":this.country, "postal_code":this.Postalcode, "phone_number1":this.Phonenumber1, "phone_number2":this.Phonenumber2})
    .then(function(response){
        
          
          $rootScope.addressId = response.data["id"];
          alert($rootScope.addressId);
          $state.go('app.Member');
    });
  }

