import React, { useEffect, useState } from 'react'
import { useHistory } from 'react-router-dom'

import TextField from '../components/ui/textfield'
import { Api } from '../api'

export default function Register({ match }) {
  const [email, setEmail] = useState('')
  const [fullname, setFullname] = useState('')
  const [password, setPassword] = useState('')
  const [fullnameError, setFullnameError] = useState('')
  const [passwordError, setPasswordError] = useState('')

  const history = useHistory()

  const token = match.params.token

  useEffect(() => {
    const validateToken = async () => {
      const baseUrl = 'https://api.local.helpdesk.health:8080'
      const api = new Api(baseUrl)
      try {
        const res = await api.get(`/agent/invitation/${token}`)
        setEmail(res.email)
      } catch (error) {
        history.push('/')
      }
    }
    validateToken()
  }, [token, history])

  const onSubmit = (ev) => {
    ev.preventDefault()
    setFullnameError('')
    setPasswordError('')
    if (!fullname) {
      setFullnameError('Fullname is required')
    }
    if (!password) {
      setPasswordError('Password is required')
    }
    if (!fullname || !password) return
  }

  return (
    <div>
      <h1>Register Agent</h1>
      <span>{email}</span>
      <form
        onSubmit={onSubmit}
        className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col"
      >
        <TextField
          className="mb-4"
          id="fullname"
          label="Full name"
          placeholder="Your fullname"
          value={fullname}
          onChange={setFullname}
          error={fullnameError}
        />
        <TextField
          className="mb-6"
          id="password"
          label="Password"
          type="password"
          value={password}
          onChange={setPassword}
          error={passwordError}
        />
        <div className="flex items-center justify-between">
          <button
            className="bg-blue-400 hover:bg-blue-dark text-white font-bold py-2 px-4 rounded"
            type="submit"
          >
            Sign In
          </button>
          <a
            className="inline-block align-baseline font-bold text-sm text-blue hover:text-blue-darker"
            href="/"
          >
            Forgot Password?
          </a>
        </div>
      </form>
    </div>
  )
}
