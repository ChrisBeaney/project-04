import React from 'react'
import ReactDOM from 'react-dom'
// import axios from 'axios'

import {HashRouter, Route, Switch } from 'react-router-dom'

import Home from './components/pages/Home'
import Register from './components/auth/Register'
import Login from './components/auth/Login'
import Navbar from './components/common/Navbar'
// import New from './components/rounds/New' # <Route path="/rounds/new" component={New}/>

class App extends React.Component {
  // componentDidMount() {
  //   axios.get('/api/rounds/')
  //     .then(res => console.log(res.data))
  // }

  render() {
    return(
      <HashRouter>
        <Navbar/>
        <Switch>
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/" component={Home}/>
        </Switch>
      </HashRouter>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
