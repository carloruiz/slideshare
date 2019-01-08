import "@babel/polyfill"
import React from "react";
import ReactDOM from "react-dom";


import Select from "react-select";
import Formol, { Field } from 'formol';
import '../css/login.css';


var options = {
  'Chocolate': 'chocolate',
  'Strawberry': 'strawberry' ,
  'Vanilla': 'vanilla'
};

class Tester extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      selectedOption: null,
      options: []
    }
    this.handleChange = this.handleChange.bind(this)
  }

  handleChange(selectedOption) {
    this.setState({ selectedOption });
    console.log(`Option selected:`, selectedOption);
  }

  render() {
    return(
      <Formol>
        <h1>Select with a huge number of choice</h1>
        <Field name="stressed" type="select-menu" choices={options}>
          Stressed select
        </Field>
        <Field
          name="multiClassSelect"
          type="select-menu"
          choices={options}
          multiple
        >
          Multi Stressed select
        </Field>
      </Formol>
    );

    /*
    return (
      <Select
        isMulti
        value={selectedOption}
        onChange={this.handleChange}
        options={options}
      />
    );
    */


  }
}

ReactDOM.render(
  React.createElement(Tester, window.props),
  document.getElementById('react'),
);


