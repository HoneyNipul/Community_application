angular.module('starter')

.constant('USER_ROLES',{
	admin:'admin_role',
	public: 'public'
})

.constant('AUTH_EVENTS',{
	notAuthenticated: 'auth-not-authenticated',
	notAuthroized: ' auth-not-authorized'
});
