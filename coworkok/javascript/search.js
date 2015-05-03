var app = angular.module('coworkok', [
    'ui.router',
    'restangular'
])
/*
app.config(function ($stateProvider, $urlRouterProvider, RestangularProvider) {
    // For any unmatched url, send to /route1
    $urlRouterProvider.otherwise("/");
    $stateProvider
        .state('index', {

            url: "/",
            templateUrl: "/coworkok/templates/search.html",
            controller: "JobList"
        })
})
*/
app.controller("SearchDeskCtrl", ['$scope', '$http'],
function ($scope, $http) {
    $http.get('/search.json').success(function(data, status, headers, config) {
        $scope.results = data;

}])