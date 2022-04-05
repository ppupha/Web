import React, { Component } from "react";
import PlaceList from './placeList'
import Footer from './footer.js'
import MyNavbar from './navbar.js'
import {MyImg} from './place'



export default class HomePage extends Component {
    render() {
        return (
        <>

            <MyNavbar />
            <img src = "https://image.shutterstock.com/z/stock-photo-outfit-of-traveler-on-the-wooden-background-548661166.jpg" style={{maxWidth:'100%', height: '80%'}}/>
            <Footer />

        </>
    );
    }
}
