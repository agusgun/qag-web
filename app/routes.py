from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm, CrawlForm
from .crawler import TwitterAPI

@app.route('/')

@app.route('/index')
def index():
	user = {'username': 'Agus'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in portland'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember me={}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)

@app.route('/twittercrawl', methods=['GET', 'POST'])
def twittercrawl():
	form = CrawlForm()
	if form.validate_on_submit():
		user = form.username.data;
		twitter = TwitterAPI(app)
		results = twitter.fetchUserTimeline(user)

		return render_template('crawl.html', title='Twitter Crawler Result', form=form, results=results)
	return render_template('crawl.html', title='Twitter Crawler', form=form)