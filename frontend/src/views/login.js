import React, { useState } from 'react'

import TextField from '../components/ui/textfield'

function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [emailError, setEmailError] = useState('')
  const [passwordError, setPasswordError] = useState('')

  const onSubmit = (ev) => {
    ev.preventDefault()
    setEmailError('')
    setPasswordError('')
    if (!email) {
      setEmailError('Email address is required')
    }
    if (!password) {
      setPasswordError('Password is required')
    }
    if (!email || !password) return
    console.log(email, password)
  }

  return (
    <form
      onSubmit={onSubmit}
      className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 flex flex-col"
    >
      <TextField
        className="mb-4"
        id="email"
        label="Username"
        placeholder="Your email"
        value={email}
        onChange={setEmail}
        error={emailError}
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
  )
}

export default Login
