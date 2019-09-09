import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'
import { Link } from 'react-router-dom'

class Register extends React.Component {

  constructor() {
    super()
    this.state = {
      formData: {
        meals: []
      },
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(e) {
    console.log(this.state.formData)
    const formData = { ...this.state.formData, [e.target.name]: e.target.value }
    const errors = { ...this.state.errors, [e.target.name]: '' }
    this.setState({ formData, errors })
  }

  handleSubmit(e) {
    e.preventDefault()
    axios.post('/api/register/', this.state.formData)
      .then(res => {
        console.log(res)
        this.props.history.push('/login/')
      })
      .catch(err => this.setState({ errors: err.response.data }))
  }

  render() {
    return (
      <section className="section register-background">
        <div className="container">
          <div className="box tableBorder">
            <h2 className="title is-3 has-white-text">Register</h2>
            <p>Have your scorecards ready.</p>
          </div>
          <div className="box tableBorder">
            <form onSubmit={this.handleSubmit}>
              <div className="field">
                <label className="label">Username</label>
                <div className="control">
                  <input
                    className="input"
                    name="username"
                    placeholder="eg: Tiger Woods"
                    onChange={this.handleChange}
                  />
                </div>
                {this.state.errors.username && <small className="help is-danger">{this.state.errors.username}</small>}
              </div>
              <div className="field">
                <label className="label">Email</label>
                <div className="control">
                  <input
                    className="input"
                    type="email"
                    name="email"
                    placeholder="eg: tigerprawns@golf.com"
                    onChange={this.handleChange}
                  />
                </div>
                {this.state.errors.email && <small className="help is-danger">{this.state.errors.email}</small>}
              </div>
              <div className="field">
                <label className="label">Password</label>
                <div className="control">
                  <input
                    className="input"
                    type="password"
                    name="password"
                    placeholder="eg: ••••••••"
                    onChange={this.handleChange}
                  />
                </div>
                {this.state.errors.password && <small className="help is-danger">{this.state.errors.password}</small>}
              </div>
              <div className="field">
                <label className="label">Password Confirmation</label>
                <div className="control">
                  <input
                    className="input"
                    type="password"
                    name="password_confirmation"
                    placeholder="eg: ••••••••"
                    onChange={this.handleChange}
                  />
                </div>
                {this.state.errors.password_confirmation && <small className="help is-danger">{this.state.errors.password_confirmation}</small>}
              </div>
              <div className="field">
                <label className="label">handicap</label>
                <div className="control">
                  <input
                    className="input"
                    name="handicap"
                    placeholder="5.5"
                    onChange={this.handleChange}
                  />
                </div>
                {this.state.errors.image && <small className="help is-danger">{this.state.errors.image}</small>}
              </div>
              <hr />
              <button className="button">Submit</button>
              <div>Already registered? Login Here:
                {!Auth.isAuthenticated() && <Link to="/login" className="">Login</Link>}
              </div>
            </form>
          </div>
        </div>
      </section>
    )
  }
}

export default Register
