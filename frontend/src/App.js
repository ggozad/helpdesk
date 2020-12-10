import React from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'

import Login from './views/agentlogin'
import Register from './views/register'
import Home from './views/home'

export default function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact={true} component={Home} />
        <Route
          path="/agent/register/:token"
          exact={true}
          component={Register}
        />
        <Route path="/agent/" exact={true} component={Login} />
      </Switch>
    </Router>
  )
}
