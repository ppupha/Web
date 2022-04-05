import React, { Component } from "react";

import Container from 'react-bootstrap/Container';
import { Dropdown, Navbar, Nav, NavDropdown } from 'react-bootstrap';

//import 'bootstrap/dist/css/bootstrap.css';


export default class MyNavbar extends Component {
    render() {
        return (
        <>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
                integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
                 crossorigin="anonymous" />

            <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark" fixed="top">
                  <Container>
                  <Navbar.Brand href="/home">K-Travel</Navbar.Brand>
                  <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                  <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link href="/placeList/All/">All</Nav.Link>
                        <Nav.Link href="/placeList/Restauran/">Restauran</Nav.Link>
                        <Nav.Link href="/placeList/Museum">Museum</Nav.Link>
                        <Nav.Link href="/placeList/Sight">Sight</Nav.Link>
                        <Nav.Link href="/profile/">Account</Nav.Link>

                    </Nav>

                  </Navbar.Collapse>
                  </Container>
                </Navbar>
        </>
        )
    }
}