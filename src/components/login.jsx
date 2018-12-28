import React, { Component } from 'react';
import ReactDOM from 'react-dom';

const institutions_url = 'http://localhost:8000/institutions'

class LoginContainer extends Component {
  constructor(props) {
    super(props)

    this.state = {
      newUser: {
        firstName: '',
        lastName: '',
        email: '',
        confirmEmail: '',
        userType: '',
        affiliations: []
      },
      userTypeOptions: ['student', 'instructor']
    }

    fetch(institutions_url)
    .then(response => response.json())
    .then(institutions => {
      this.setState({"institutions": institutions})
    })
    .catch(error => console.log(error))

    this.handleFormSubmit = this.handleFormSubmit.bind(this)
    this.handleInput = this.handleInput.bind(this)
  }

  handleFormSubmit() {

  }

  // change setState to simpler form
  handleInput(e) {
    let value = e.target.value
    let name = e.target.name
    this.setState( prevState => {
      return {
        newUser: {
          ...prevState.newUser,
          [name]: value
        }
      }
    }, () => console.log(this.state))
  }

  handleAffiliations(e) {
    let aff = e.target.value
    // last = affs.split(',')
    // if len(last) > 3: check against db and show matches in drop down
  }

  handleAffiliationSubmit(e) {
    let aff = e
  }

  render() {
    return (
      <form className="container" onSubmit={this.handleFormSubmit}>
        <Input
          title="First name"
          name="firstName"
          type="text"
          value={this.state.newUser.firstName}
          handleChange = {this.handleInput}
        />
        <Input
          title="Last name"
          name="lastName"
          type="text"
          value={this.state.newUser.lastName}
          handleChange = {this.handleInput}
        />
        <Input
          title="email"
          name="email"
          type="text"
          value={this.state.newUser.email}
          handleChange = {this.handleInput}
        />
        <Input
          title="Confirm email"
          name="confirmEmail"
          type="text"
          value={this.state.newUser.confirmEmail}
          handleChange = {this.handleInput}
        />
        <Select
          title="User Type"
          name="userType"
          type=""
          options={this.state.userTypeOptions}
          handleChange = {this.handleInput}
        />
        <Input
          title="Affiliations"
          name="affiliations"
          type="text"
          value={this.state.newUser.affiliations}
          handleChange = {this.handleAffiliations}
        />
      </form>
    )
  }
}


const Select = (props) =>
  <div className="form-group">
    <label htmlFor={props.name}> {props.title} </label>
    <select
      name={props.name}
      value={props.value}
      onChange={props.handleChange}
    >
      {props.options.map(option => {
        return (
          <option
            key={option}
            value={option}
            label={option}> {option}
          </option>
        )
      })}
    </select>
  </div>

const Input = (props) =>
  <div className="form-group">
    <label htmlFor={props.name} className='form-label'>
      {props.title}
    </label>
    <input
      className="form-input"
      id={props.name}
      name={props.name}
      type={props.type}
      value={props.value}
      onChange={props.handleChange}
    />
  </div>


export default LoginContainer;


ReactDOM.render(
  React.createElement(LoginContainer, window.props),
  document.getElementById('react'),
);





















