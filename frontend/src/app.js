import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'

import {HashRouter, Route, Switch } from 'react-router-dom'

import Home from './components/pages/Home'
import Register from './components/auth/Register'
import Login from './components/auth/Login'
import Navbar from './components/common/Navbar'
import CoursesIndex from './rounds/CoursesIndex'
// import CoursesShow from './rounds/CoursesShow' #<Route path="/courses/:id" component={CoursesShow} />
import 'bulma'


class App extends React.Component {
  componentDidMount() {
    axios.get('/api/rounds/')
      .then(res => console.log(res.data))
  }

  render() {
    return(
      <HashRouter>
        <Navbar/>
        <Switch>
          <Route path="/courses" component={CoursesIndex} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/" component={Home} />
        </Switch>
      </HashRouter>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
