from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, CrawlForm, PassageForm
from .crawler import TwitterAPI
from .qag.qag_app import QuestionGenerator


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'World'}
    form = PassageForm()
    if form.validate_on_submit():
        passage = form.passage.data

        qg = QuestionGenerator(passage)
        questions = qg.process(top_sentences=2)

        return render_template('index.html', title='Home', user=user, form=form, questions=questions, sentences=passage.split('.'))
    return render_template('index.html', title='Home', user=user, form=form)


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
