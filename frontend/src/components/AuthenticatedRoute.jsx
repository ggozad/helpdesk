import React from 'react'
import { Route, Redirect } from 'react-router-dom'

export default function AuthenticatedRoute({ component: Component, children, ...rest }) {
    return React.createElement(Route, {
      ...rest,
      render: (routeProps) => {
        const isAuthenticated=false
        if (!isAuthenticated) {
          return <Redirect to={{ pathname: '/agent/login', state: { from: routeProps.location } }} />
        } else  {
          return <Component {...routeProps}>{children}</Component>
        }
      },
    })
  }

