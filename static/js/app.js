window.HlaApp = Ember.Application.create();

HlaApp.Router.map(function () {
   this.resource('index', {path: '/'});
});
