const createError = require('http-errors')
const express = require('express')
const cookieParser = require('cookie-parser')
const logger = require('morgan')
const app = express()
const mongoose = require('mongoose')
const passport = require('passport')
const cors = require('cors')

app.use(cors())

// Routes
const indexRouter = require('./routes/index')


app.use(logger('dev'))
app.use(express.json())
app.use(express.urlencoded({ extended: false }))
app.use(cookieParser())


// Passport middleware
app.use(passport.initialize())


// Passport config
require('./config/passport')(passport)

// DB Config
var path = require('path')
let db
const MONGO_TEST = 'mongodb://travis:test@localhost:27017/mydb_test'

path.exists('./config/keys.js', function(exists) { 
  if (exists) { 
	db= path.mongoURI
  }
  else{
	db=MONGO_TEST
  } 
});


// Connect to MongoDB
mongoose.connect(db, { useNewUrlParser: true })
	.then(() => console.log('MongoDB successfully connected'))
	.catch(err => console.log(err))

// Router
app.use('/', indexRouter)

// catch 404 and forward to error handler
app.use(function (req, res, next) {
	next(createError(404))
})

// error handler
app.use(function (err, req, res) {
	// set locals, only providing error in development
	res.locals.message = err.message
	res.locals.error = req.app.get('env') === 'development' ? err : {}

	// render the error page
	res.status(err.status || 500)
	res.render('error')
})

module.exports = app
