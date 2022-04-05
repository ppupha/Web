import React, { Component } from "react";

import MyNavbar from './navbar.js'
import Place from './place.js'
import Footer from './footer.js'
import ReviewList from './Review.js'


//import { Row, Column } from 'react-foundation';

export default class PlacePage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            fdata :  [],
            activeItem : {
                Name : "",
            },
        };
    };

    render() {
        const id = this.props.match.params.id;
        return (
            <>
                <MyNavbar/>
                <Place placeid={id}></Place>
                <ReviewList placeid={id}></ReviewList>
                <Footer/>
            </>
        )
    }
}