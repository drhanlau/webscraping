var casper = require('casper').create({
	pageSettings: {
         userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'
    },
    viewportSize: {
        width: 1024,
        height: 768
    }
});


var url = "https://myjobstreet.jobstreet.com.my/home/login.php";
// var url = 'http://www.nba.com/'

casper.start(url, function() {
    //this.echo(this.getTitle());   
    this.capture('jobstreet.png');

    this.fill('form#login', {
        login_id: 'andy.qut@gmail.com',
        password: 'a12875883'
    }, true);
}).waitForSelector('span.header-login-name', function(){
	//this.echo("evaluating...")
    this.echo("Page Title " + this.getTitle());
    this.capture('jobstreet-1.png');
}).thenOpen('http://www.jobstreet.com.my/en/job-search/job-vacancy.php', function(){
	this.capture('jobstreet-2.png');

    this.echo(this.getHTML());
});
// casper.thenOpen('http://phantomjs.org', function() {
//     this.echo(this.getTitle());
// });

casper.run();