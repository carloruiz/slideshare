import React, { Component } from 'react';

import styles from '../css/header.module.css'

class Header extends Component {
  render() {
    return (
      <div className={styles.header}>
        <img className={styles.logo} src="logo.svg"/>
        <span className={styles.company}> SlideShare </span>
        <input className={styles.search} type="text" placeholder="Search.."/>
      </div>
    );
  }
}

export default Header;
