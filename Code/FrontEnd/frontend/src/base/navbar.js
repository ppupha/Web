import React, { Component } from "react";


export default class NavBar extends Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    render() {
        return (
        <div className="" >
            <nav className="navbar navbar-inverse navbar-static-top navbar-fixed-top">
                <div className="container" style="">
                    <div className="navbar-header ">
                        <button type="button" className="navbar-toggle" data-toggle="collapse" data-target="#menu">
                            <span className="sr-only">Toggle navigation</span>
                            <span className="icon-bar"></span>
                            <span className="icon-bar"></span>
                            <span className="icon-bar"></span>
                        </button>
                    </div>
                </div>
            </nav>
	    </div>
        );
    }
}