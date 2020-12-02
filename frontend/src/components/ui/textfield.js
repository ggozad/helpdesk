import React from 'react'
import PropTypes from 'prop-types'
import { v4 as uuidv4 } from 'uuid'

function TextField({
  id = uuidv4(),
  name = '',
  type = 'text',
  value = '',
  label = '',
  className = '',
  placeholder = '',
  error = '',
  onChange,
}) {
  return (
    <div className={className}>
      {label ? (
        <label
          className="block text-grey-darker text-sm font-bold mb-2"
          htmlFor={id}
        >
          {label}
        </label>
      ) : (
        ''
      )}
      <input
        className={`shadow appearance-none border ${
          error ? 'border-red-400 mb-3' : ''
        } rounded w-full py-2 px-3 text-grey-darker`}
        id={id}
        name={name}
        type={type}
        value={value}
        placeholder={placeholder}
        onChange={(ev) => onChange(ev.target.value)}
      />
      {error ? <p className="text-red-400 text-xs italic">{error}</p> : ''}
    </div>
  )
}

TextField.propTypes = {
  id: PropTypes.string,
  name: PropTypes.string,
  type: PropTypes.string,
  value: PropTypes.string,
  label: PropTypes.string,
  error: PropTypes.string,
  className: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.arrayOf(PropTypes.string),
  ]),
  placeholder: PropTypes.string,
  onChange: PropTypes.func,
}
export default TextField
