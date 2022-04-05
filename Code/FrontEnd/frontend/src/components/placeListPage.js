import React, { Component } from "react";

import MyNavbar from './navbar.js'
import PlaceList from './placeList'
import Footer from './footer.js'

import { withRouter } from "react-router";
import '../static/css/style.css'

export default class PlaceListPage extends Component {
    constructor(props) {
        super(props);
        console.log("From PlaceListPage");
        console.log(props);
        this.state = {
            fdata :  [],
        };

    };
    render() {
        const type = this.props.match.params.type;
        return (
        <div>
            <MyNavbar/>
            <PlaceList type={type}/>
            <Footer/>
        </div>

        )
    }
}